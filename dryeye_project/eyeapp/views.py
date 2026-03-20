from django.shortcuts import render

# Create your views here.

def home(request):

    message = ""

    if request.method == "POST":
        time = int(request.POST.get("time"))

        if time > 40:
            message = "Your eyes need rest! Follow the 20-20-20 rule."
        else:
            message = "Screen time is safe."

    return render(request, "home.html", {"message": message})