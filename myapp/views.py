from django.shortcuts import render
from django.http import HttpResponse
from .models import Menu
from .models import Contact


# Create your views here for menu.
def about(request):
    about_content = {'about': "Little Lemon is a family-owned Mediterranean restaurant, focused on traditional recipes served with a modern twist. The chefs draw inspiration from Italian, Greek, and Turkish culture and have a menu of 12–15 items that they rotate seasonally. The restaurant has a rustic and relaxed atmosphere with moderate prices, making it a popular place for a meal any time of the day."}
    return render(request, "about.html", {'content': about_content})


def menu(request):
    # menu_items are all the objects in the Menu model
    menu_items = Menu.objects.all()
    items_dict = {"menu": menu_items}
    return render(request, "menu.html", items_dict)


def home(request):
    return render(request, "home.html")


def book(request):
    return render(request, "book.html")


def display_menu_items(request, pk=None):
    if pk:
        menu_item = Menu.objects.get(pk=pk)
    else:
        menu_item = ''
    return render(request, 'menu_item.html', {"menu_item": menu_item})


def contact_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Save to the database
        contact = Contact(email=email, message=message)
        contact.save()

        # Optionally, send an email
        # send_mail(
        #     'Contact Form Submission',
        #     message,
        #     email,
        #     [settings.DEFAULT_FROM_EMAIL],
        #     fail_silently=False,
        # )
        #
        # return redirect('thank_you')  # Redirect to a thank-you page or somewhere

    return render(request, 'partials/_footer.html')