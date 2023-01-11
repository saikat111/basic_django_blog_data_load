from django.shortcuts import render,HttpResponse
from .models import RecentPost



def members(request):
    post_ = RecentPost.objects.all()

   # print(post_)
    return  render(request,"index.html", {'posts' : post_})