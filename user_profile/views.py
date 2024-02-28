from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return render(request, "index.html")

def user_page(request, name):
    context = {
        "route_name": name,
        "favorite_color": "Blue",
        "age": 31,
        "hobbies":["basketball", "lifting weights", "coding"]
    }
    return render(request, "name_route.html", context)