from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from article.models import Article
from article.forms import ArticleForm, CommentForm
from django.template.context_processors import csrf

# Create your views here.

# Artiles function list all
def articles(request):

    """
     Este metodo sera responsavel em
     poder listar todos os artigos
     disponiveis no blog

    :param request:
    :return:
    """

    language = 'pt-br'
    session_language = 'pt-br'

    if 'lang' in request.COOKIES:
        language = request.COOKIES['lang']

    if 'lang' in request.session:
        session_language = request.session['lang']

    #data = {}
    data  = Article.objects.all()

    return render(request, "body/articles.html", {
                    'articles': data,
                    'language': language,
                    'sess_lang' : session_language,
    })

def create(request):

    form = ArticleForm(request.POST, request.FILES)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/articles/all')
    else:

        form = ArticleForm()

    return render(request, 'body/create.html', {'form':form})
    #return render(request, 'body/create.html', {'form' : form})
# ge simlge articl
def article(request, article_id = 1):

    """
    Este metodo sera responsavel em
    poder fornecer a pagina unica de
    leitura do artigos publicados.

    :param request:
    :param article_id:
    :return:
    """
    data = Article.objects.get(id=article_id)

    return render(request, 'body/single.html', {'article': data })

def like_article(request, article_id):
    """

    :param request:
    :param article_id:
    :return:
    """
    if article_id:
        a = Article.objects.get(id=article_id)
        count = a.likes
        count += 1
        a.likes = count
        a.save()
    return HttpResponseRedirect('/articles/get/%s' % article_id)

def add_comment(request, article_id):
    pass

def search_tile(request):

    if request.method == 'POST':

        search_text = request.POST['search_text']

    else:
        search_text = ''
    a = Article.objects.filter(title__contains=search_text)

    return render(request, 'body/ajax_search.html', {'article': a})

def language(request, lang='en-US'):

    """
     Este metodo sera responsavel em poder
     providencia ligua de apreentacao

    :param request:
    :param lang:
    :return:
    """
    response = HttpResponse("setting language to %s" % lang)

    response.set_cookie('lang', lang)
    request.session['lang'] = lang

    return response



