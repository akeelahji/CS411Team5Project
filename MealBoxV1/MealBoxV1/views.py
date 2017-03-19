# add to the top
from .forms import ContactForm, SearchForm, SearchResult
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse

# add to your views
def contact(request):
  form_class = ContactForm

  return render(request, 'search.html', {'form': form_class,})


def search(request):
  # if this is a POST request we need to process the form data
  if request.method == 'POST':
    # create a form instance and populate it with data from the request:
    form = SearchForm(request.POST)
    # check whether it's valid:
    if form.is_valid():
      # process the data in form.cleaned_data as required
      print (form)
      # redirect to a new URL:
      html = ("<Hi>%s</Hi>", request.POST.get('search', None))
      return HttpResponse(html)
    #  return render(request, 'search.html', {'form': form})

  # if a GET (or any other method) we'll create a blank form
  else:
    form = SearchForm()

  return render(request, 'search.html', {'form': form})
