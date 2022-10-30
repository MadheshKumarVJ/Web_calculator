from django.shortcuts import render
from .forms import Calculator
from django.http import HttpResponse


def getInputValuesFromWeb(request):
    num1 = 0
    num2 = 0
    operation = ""
    if request.method == "POST":
        form = Calculator(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            num1 = cd["number_one"]
            num2 = cd["number_two"]
            operation = cd["operation"]

        else:
            return HttpResponse("Give some Valide Inputs")
    else:
        form = Calculator()
    return render(
        request,
        "calc/calcy.html",
        {
            "form": form,
            "number_one": num1,
            "number_two": num2,
            "operation": operation,
        },
    )
