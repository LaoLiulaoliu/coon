from django.shortcuts import render

from critique.dbutils import DBUtils

db_u = DBUtils('unit')
db_i = DBUtils('info')


def homepage(request):
    context = []
    db_u.execute("select id, name, dept, brief, portrait, rating, class, webpage, build_time, address, tag, comments from company order by rating desc;")
    ret = db_u.fetch()
    for i in ret.results:
        context.append( dict( zip(ret.columns, i) ) )
    return render(request, 'homepage.html', {'context': context})

def suggest(request):
    return render(request, 'suggest.html', {})


def company(request, company_id):
    db_u.execute("select name, dept, brief, portrait, rating, class, webpage, build_time, address, tag, comments from company where id=%s;", (company_id, ))
    ret = db_u.fetch()
    context = dict( zip(ret.columns, ret.results[0]) )
    context.update({'id': company_id})

    comments = []
    db_i.execute("select uid, pub_time, rating, nick, content from comment where cid=%s order by pub_time desc;", (company_id,))
    ret = db_i.fetch()
    for i in ret.results:
        comments.append( dict(zip(ret.columns, i)) )
    return render(request, 'company.html', {'context': context, 'comments': comments})


def coedit(request, company_id):
    context = {}
    context.update({'id': company_id})
    return render(request, 'coedit.html', context)

def pop(requests, company_id, user_id):
    context = {}
    context.update({'cid': company_id})
    context.update({'uid': user_id})
    return render(request, 'pop.html', context)
