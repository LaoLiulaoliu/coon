# -*- coding: utf-8 -*-
#from django.test import TestCase
from datetime import datetime
from datetime import timedelta
from critique.pgutils import DBUtils
from critique.data import data

db_u = DBUtils('unit')
db_i = DBUtils('info')

def insert_person():
    """
    db_u.execute("insert into person (email, password) values (%s, %s)", ('q_0_0_p@163.com', 'asdf1234'))
    db_u.execute("insert into person (email, password) values (%s, %s)", ('q_0_0_p@yahoo.com', 'asdf1234'))
    """
    sqls = []
    sql = 'insert into person (email, password) values (%s, %s)'
    for item in data['person']:
        sqls.append( sql % (item['email'], item['password']) )
    db_u.batch(sqls)
        

def insert_company():
    """
db_u.execute("insert into company (name, brief, dept) values (%(name)s, %(brief)s, %(dept)s)",
             {'name': '盛大', 'brief': '互联网文化内容提供商', 'dept': ['盛大网络','盛大文学','盛大游戏','酷6传媒',]})
db_u.execute("insert into company (name, brief, dept) values (%(name)s, %(brief)s, %(dept)s)",
        {'name': 'favbuy', 'brief': 'A taobao data company', 'dept': []})
db_u.execute("insert into company (name, brief, dept) values (%(name)s, %(brief)s, %(dept)s)",
        {'name': '南京烽火', 'brief': '电信服务提供商', 'dept': []})
db_u.execute("insert into company (name, brief, dept) values (%(name)s, %(brief)s, %(dept)s)",
        {'name': '百度', 'brief': '恶心的中文搜索引擎', 'dept': []})
db_u.execute("insert into company (name, brief, dept) values (%(name)s, %(brief)s, %(dept)s)",
        {'name': '阿里巴巴', 'brief': '最大的电商生态系统', 'dept': []})
db_u.execute("insert into company (name, brief, dept) values (%(name)s, %(brief)s, %(dept)s)",
        {'name': '腾讯', 'brief': '个人IM巨头', 'dept': []})
db_u.execute("insert into company (name, brief, dept) values (%(name)s, %(brief)s, %(dept)s)",
        {'name': '拾衣网', 'brief': '对年轻女性进行个性化服饰推荐', 'dept': []})
db_u.execute("insert into company (name, brief, dept) values (%(name)s, %(brief)s, %(dept)s)",
        {'name': '豆瓣', 'brief': '音乐、读书、同城活动等文艺类生活交友网站', 'dept': []})
db_u.execute("insert into company (name, brief, dept) values (%(name)s, %(brief)s, %(dept)s)",
        {'name': 'google', 'brief': '', 'dept': []})
db_u.execute("insert into company (name, brief, dept) values (%(name)s, %(brief)s, %(dept)s)",
        {'name': '艾瑞咨询', 'brief': '非常牛掰的互联网咨询工作，收集了大量的数据，反应中国网民的上网和使用科技产品的情况。艾瑞咨询还和很多公司形成战略合作关系，当然战略投资也是不少的。有时我觉得这些数据不一定有太大用，也许是要付费的版本才会有更多数据挖掘与分析的东西。免费版的信息太少。一些分析也许可以专门定制付费的去做。', 'dept': []})
    """
    sqls = []
    sql = 'insert into company (name, brief, dept) values (%(name)s, %(brief)s, %(dept)s)'
    for item in data['company']:
        sqls.append( sql % item )
    db_u.batch(sqls)

def insert_comment():
    """
    db_i.execute("insert into comment (cid, uid, rating, nick, content) values (3, 1, 3, 'lotus', '百度的搜索引擎技术还不错，但和google没得比。这么大一家公司，居然很少有创新和颠覆性的行为，只是吃着老本，搞一搞关系。');")
    """
    sqls = []
    sql = 'insert into comment (cid, uid, rating, nick, content) values (%(cid)s, %(uid)s, %(rating)s, %(nick)s, %(content)s)'
    for item in data['comment']:
        sqls.append( sql % item )
    db_u.batch(sqls)


#db_u.execute("update company set class='{\"互联网\", \"娱乐化\"}', webpage='http://www.baidu.com', build_time=%s, address='北京市海淀区东北旺西路8号中关村软件园12号', portrait='http://www.baidu.com/img/bdlogo.gif', tag='{\"搜索\", \"娱乐化\", \"竞价排名\", \"百度知道\"}' where name='百度';", (datetime.utcnow().date() - timedelta(days=365), ))
#db_u.execute("update company set dept='{\"销售部\", \"研发部\", \"市场部\", \"人事\", \"财务\", \"战略\"}' where name='百度';")


# db_u.execute("select email, regist_time from person;", result=True)
# [('q_0_0_p@163.com', datetime.datetime(2014, 3, 1, 19, 40, 35, 343862)), ('email', datetime())]

ret = db_u.execute("select name, dept, brief, portrait, rating, class, webpage, build_time, address, tag from company;", result=True)
print isinstance(ret.results[0][0].decode('utf-8'), unicode)
#for i in ret.results:
#    print dict(zip(ret.columns, i))

