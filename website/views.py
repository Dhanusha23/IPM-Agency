from django.shortcuts import render
from . forms import ContactForm


# Create your views here.
def home(request):
    return render(request, 'home.html')
def services(request):
    return render(request, 'services.html')
#def contact(request):
  #  return render(request, 'contact.html')
def works(request):
    return render(request, 'works.html')
def about(request):
    return render(request, 'about.html')


def contact(request):
    success = False

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            success = True
            form = ContactForm()  # clear form
    else:
        form = ContactForm()

    return render(request, "contact.html", {
        "form": form,
        "success": success
    })
