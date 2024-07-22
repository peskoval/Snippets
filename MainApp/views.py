from django.http import Http404
from django.shortcuts import render, redirect
from MainApp.models import Snippet


def index_page(request):
    context = {'pagename': 'PythonBin'}
    return render(request, 'pages/index.html', context)


def add_snippet_page(request):
    context = {'pagename': 'Добавление нового сниппета'}
    return render(request, 'pages/add_snippet.html', context)


def snippets_page(request):
    snipps = Snippet.objects.all()
    context = {
        'pagename': 'Просмотр сниппетов',
        'snipps': snipps,
    }
    return render(request, 'pages/view_snippets.html', context)


def snippet_detail(request, snippet_id):
    context = {'pagename': 'Просмотр сниппета'}
    try:
        snippet = Snippet.objects.get(id=snippet_id)
    except ObjectDoesNotExist:
        return render(request, "pages/errors.html", context | {"error": f"Snippet with id={snippet_id} not found"})
    else:
        context["snippet"] = snippet
        return render(request, "pages/snippet_detail.html", context)




# def remove_snippet(request, snippet_id):
#     Snippet.objects.get(id=snippet_id).delete()
#     return(render(request, 'pages/snippet_page.html', context))
# clear or remove??
