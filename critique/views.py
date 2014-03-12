from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.utils import simplejson
from django.core import serializers

from critique.dbutils import DBUtils

db_u = DBUtils('unit')
db_i = DBUtils('info')


class QuerySetEncoder(simplejson.JSONEncoder):
    """
        Encoding QuerySet into JSON format.
    """
    def default(self, object):
        try:
            return serializers.serialize( "python",
                                          object,
                                          ensure_ascii = False )
        except:
            return simplejson.JSONEncoder.default(self, object)


def suggest(request):
    if request.method == 'POST':
        opinion = request.POST['opinion']
        print opinion
        # TODO  need add user id
        db_u.execute("insert into suggestion (uid, suggestion) values (%s, %s)", (2, opinion))
        data = {'status': 1}
        return HttpResponse(simplejson.dumps(data, cls=QuerySetEncoder), content_type="application/json")
    return render(request, 'suggest.html', {})



def homepage(request):
    context = []
    db_u.execute("select id, name, dept, brief, portrait, rating, class, webpage, build_time, address, tag, comments from company order by rating desc;")
    ret = db_u.fetch()
    for i in ret.results:
        context.append( dict( zip(ret.columns, i) ) )
    return render(request, 'homepage.html', {'context': context})


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
