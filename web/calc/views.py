from django.shortcuts import render
from .forms import Calculator
from django.http import HttpResponse


def addition(request):
    result = None
    if request.method == "POST":
        form = Calculator(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            number_one = cd["number_one"]
            number_two = cd["number_two"]
            result = number_one + number_two
        else:
            return HttpResponse("Give some Valide Inputs")
    else:
        form = Calculator()
    return render(request, "calc/calcy.html", {"form": form, "result": result})
