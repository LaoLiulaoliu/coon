#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Yuande Liu <miracle (at) gmail.com>

import psycopg2
from collections import namedtuple

QueryResult = namedtuple('RowResult', ('columns', 'results'))

class DBUtils(object):

    def __init__(self, dbname='postgres', user='bishop', fetch_size=400):
        self.dbname = dbname
        self.user = user
        self.fetch_size = fetch_size
        self.conn = self.get_conn()
        self.cur = self.get_cur()

    def get_conn(self):
        return psycopg2.connect(database=self.dbname, user=self.user)
    
    def get_cur(self):
        return self.conn.cursor()


    def execute(self, sql, *args, **kwargs):
        self.cur.execute(sql, *args, **kwargs)

    def fetch(self, size=None):
#        if size == None:
#            size = self.fetch_size
#        while True:
#            ret = self.cur.fetchmany(size)
#            if ret == []: break
#            yield ret
        columns = [i[0] for i in self.cur.description]
        results = self.cur.fetchall()
        return QueryResult(columns, results)


    def commit(self):
        self.conn.commit()

    def close(self):
        self.cur.close()
        self.conn.close()

