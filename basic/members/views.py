from django.shortcuts import render,HttpResponse



def members(request):
    return  render(request,"index.html")