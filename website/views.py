from django.shortcuts import render
from . forms import ContactForm
#from . models import WorkSection

# Create your views here.
def home(request):
    return render(request, 'home.html')
def services(request):
    return render(request, 'services.html')

def works(request):
    return render(request, 'works.html')
'''
def test(request):
    instagram_section = WorkSection.objects.filter(
        section_type='instagram',
        is_active=True
    ).first()

    reels_section = WorkSection.objects.filter(
        section_type='reels',
        is_active=True
    ).first()

    website_section = WorkSection.objects.filter(
        section_type='website',
        is_active=True
    ).first()

    context = {
        "instagram_posts": instagram_section.instagram_posts.all() if instagram_section else [],
        "reels": reels_section.reels.all() if reels_section else [],
        "websites": website_section.websites.all() if website_section else [],
    }

    return render(request, "test.html", context)

'''


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


