from django.http import HttpResponse

def landing_page(request):
    return HttpResponse("<h1>Welcome to the Plane API Landing Page</h1><p>This is the root endpoint.</p>")
