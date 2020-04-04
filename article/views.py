from django.shortcuts import render,get_object_or_404
from .models import  Article
from django.http import  HttpResponse,Http404


# Create your views here.

def article_detail(request,article_id):
    try:
        #article = Article.objects.get(id=article_id)
        article = get_object_or_404(Article,pk = article_id)
        context = {}
        context["article_obj"] = article
        return render(request, "article_detail.html", context=context)
    except Article.DoesNotExist:
        #主动刨出一个异常
        #很想知道源码怎么写？
        #为什么服务端不会有问题？
        raise Http404("Sorry,ID Not Exist");
        #return HttpResponse("sorry",status=404)
    #return HttpResponse("<h2>文章标题是:%s</h2> <br>文章内容是:%s" % (article.title,article.content))

def article_list(request):
    articles = Article.objects.all()
    context = {}
    context["articles"] = articles
    return render(request,"article_list.html",context=context)

