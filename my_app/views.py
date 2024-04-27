from django.shortcuts import render
from django.http import HttpResponse
from .models import Madel, Product
# Create your views here.
def object (requests):
    queryset = Madel.objects.only()
    print("\n", queryset.only)
    str_data = ""
    for i in queryset:
        str_data+= f"""<li> <a href="/product">{i}</a></li>"""

    return HttpResponse(f"<ul> {str_data}</ul>")
def product (requests):
    queryset =Product.objects.all()
    str_data = ""
    for i in queryset:
        str_data += f"""{i}"""
    return HttpResponse(f"{str_data}")
