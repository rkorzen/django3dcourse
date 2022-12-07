from django.shortcuts import render
from django.http import HttpResponse
from .models import Math

# Create your views here.

def hello_world(request, name="World"):
    return HttpResponse(f"Hello {name}")

def add(a: int, b: int) -> int:
    return a + b

def sub(a: int, b: int) -> int:
    return a - b


def mul(a: int, b: int) -> int:
    return a * b


def div(a: int, b: int) -> int | str:
    if b == 0:
        return "Dzielenie przez 0"
    return a / b


operations = {
    "add": add,
    "sub": sub,
    "div": div,
    "mul": mul
}


class Data:
    a = 10
    b = 20


def do_math(request, op, a, b):
    result = operations[op](a, b)
    maths = Math.objects.all()
    return render(
        request,
        "main.html",
        {
            "result": result,
            "lista": ["a", "b", "c"],
            "dictionary": {"Ala": "Kot"},
            "dane": Data(),
            "maths": maths,

        }
        )

    