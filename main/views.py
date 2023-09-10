from django.shortcuts import render
from main.models import Item

# Create your views here.
def show_main(request):
    item = Item.objects.all()
    context = {
        'list_of_item': item,
    }

    return render(request, "main.html", context)
