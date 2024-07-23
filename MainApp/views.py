
from django.http import Http404, HttpResponse
from django.shortcuts import render, redirect
from MainApp.models import Snippet
from django.core.exceptions import ObjectDoesNotExist
from MainApp.forms import SnippetForm


def index_page(request):
    context = {'pagename': 'PythonBin'}
    return render(request, 'pages/index.html', context)


def add_snippet_page(request):
    #  создаем пустую форму при запросе get
    if request.method == "GET":
        form = SnippetForm()
        context = {
            'pagename': 'Добавление нового сниппета',
            'form': form
            }
        return render(request, 'pages/add_snippet.html', context)
#  получаем данные из формы 
    if request.method == "POST":
        form = SnippetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("snippets-list")
        return render(request,'pages/add_snippet.html',{'form': form})
       


def snippets_page(request):
    snippets = Snippet.objects.all()
    context = {
        'pagename': 'Просмотр сниппетов',
        'snippets': snippets,
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


def delete_snippet(request, snippet_id):
    form = Snippet.objects.get(id=snippet_id)
    if request.method == "POST":
        form.delete()
    return redirect("snippets-list")


# def change_snippet(request, snippet_id):
#     if request.method == "POST":
#         form = SnippetForm(request.POST)
#         if form.is_valid():
#             form.save()
#             # url = snippet.get_url()
#             # return HttpResponse(url)
#             return redirect("snippets-detail")
#     return redirect("snippets-list")


def change_snippet(request, snippet_id):
    snippet = Snippet.objects.get(id=snippet_id)
    if request.method == "POST":
        form = SnippetForm(request.POST, instance=snippet)
        if form.is_valid():
            snippet = form.save()
            snippet.save()
            return redirect("snippets-detail")
    else:
        # form = SnippetForm()
        # context = {
        #     'form': form
        #     }
        # return render(request, 'pages/view_snippets.html', context)
        snippets = Snippet.objects.all()
        context = {
            'pagename': 'Просмотр сниппетов',
            'snippets': snippets,
            }
        return render(request, 'pages/view_snippets.html', context)
