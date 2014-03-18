#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Yuande Liu <miracle (at) gmail.com>
# Add a connection pool for postgresql

import Queue
import psycopg2
from collections import namedtuple
from contextlib import contextmanager

QueryResult = namedtuple('RowResult', ('columns', 'results'))

class DBUtils(object):

    def __init__(self, dbname='postgres',
                 user='bishop',
                 poolsize=3,
                 maxretries=5,
                 fetch_size=400):
        self.dbname = dbname
        self.user = user
        self.poolsize = poolsize
        self.maxretries = maxretries
        self.fetch_size = fetch_size
        self.queue = Queue.Queue(self.poolsize)
        self.connection_in_use = 0


    def clear(self):
        while not self.queue.empty():
            self.queue.get().close()

    def get(self):
        if self.queue.empty() and self.connection_in_use < self.poolsize:
            self.connection_in_use += 1
            return self._create_connection()
        return self.queue.get()

    def put(self, conn):
        if self.queue.full():
            conn.close()
        self.queue.put(conn)

    def _create_connection(self):
        """ If we hava several hosts, we can random choice one to connect
        """
        return psycopg2.connect(database=self.dbname, user=self.user)

    @contextmanager
    def connection(self):
        yielded = False
        retry = 0
        while yielded is False and retry < self.maxretries:
            try:
                conn = self.get()
                cur = conn.cursor()
                yield cur
            except Exception as e:
                conn = None
                retry += 1
                print e
            else:
                yielded = True
                retry = 0
                conn.commit() # commit `insert` and `update`
            finally:
                if conn is not None:
                    cur.close()
                    self.put(conn)

        if yielded is False:
            raise Exception('Could not obtain cursor, max retry {} reached.'.format(retry))


    def execute(self, query, vars=None, result=False):
        """.. :py:method::

        :param bool result: whether query return result
        :rtype: bool

        .. note::
            True for `select`, False for `insert` and `update`
        """
        with self.connection() as cur:
            resp = cur.execute(query, vars)

            if result == False:
                return resp

            else:
                columns = [i[0] for i in cur.description]
                results = cur.fetchall()
                return QueryResult(columns, results)



    def batch(self, sqls):
        """ batch execute queries.
            only support `insert` and `update`, have more efficiency
        """
        with self.connection() as cur:
            for sql in sqls:
                cur.execute(query)


class DataUtils(object):
    """
        read data from data file, not postgresql.

        This class can parse `select`
    """
    def __init__(self, dbname='postgres'):
        self.dbname = dbname

    def execute(self, query, vars=None, result=None):
        results = []
        if vars:
            query = query % vars
        query = query.lower()

        # from the query string, get table name
        field, table = query.split('from')
        table_name = table.strip().split()[0]

        # get query condition
        keys, values = [], []
        if 'where' in table and '=' in table:
            table = table.split('order by')[0].split('group by')[0]
            conditions = table.split('where')[1].strip().split(',')
            conditions = map(lambda x: x.strip(), conditions)
            for condition in conditions:
                key, value = condition.split('=')
                keys.append(key.strip())
                values.append(value.strip(';').strip())

        # get query field
        fields = field.lstrip('select').strip().split(',')
        fields = map(lambda x: x.strip(), fields)

        # read data from data file, based on query field return results
        m = __import__('critique.data', fromlist=['data'])
        for line in m.data[table_name]:

            skip_flag = True
            for i, key in enumerate(keys):
                if str(line[key]) != values[i]:
                    break
            else:
                skip_flag = False
            if skip_flag: continue


            record = []
            for field in fields:
                temp = line[field] if field in line else ''
                record.append(temp)
            results.append( tuple(record) )

        return QueryResult(fields, results)

