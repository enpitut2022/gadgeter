from django.shortcuts import render
from django.http import HttpResponse
from .models import Image,ImageTag,Tag, ImageUrl,Desk
from .form import FindForm

def index(request):
    msg = "search words"
    form = FindForm()
    data = Image.objects.raw("select distinct * from show_design_image")
    tags = Tag.objects.raw("select distinct * from show_design_tag")
    desk = Desk.objects.raw("select distinct * from show_design_desk")
    title = "一覧"
    params = {
        'title' : title,
        'message': msg,
        'form' : form,
        'data' : data,
        'tags' : tags,
        'desk': desk,
    }
    return render(request,'showdesign/index.html',params)

def find(request):
    if (request.method == "POST"):
        form = FindForm(request.POST)
        find = request.POST['find']
        size = request.POST['desk']
        msg = str(find)
        print(1111111)
        print(size)
        title = "検索結果"
        tags = Tag.objects.raw("select distinct * from show_design_tag")
        desk = Desk.objects.raw("select distinct * from show_design_desk")
        urls = Tag.objects.raw("select distinct * from show_design_imageurl inner join show_design_tag on show_design_imageurl.tagid = show_design_tag.tagid")
        # data = Image.objects.raw((f"select distinct * from  show_design_imagetag left join show_design_image on show_design_imagetag.imageid = show_design_image.imageid left join show_design_tag on show_design_imagetag.tagid = show_design_tag.tagid left join show_design_imageurl on show_design_imagetag.imageid = show_design_imageurl.imageid where show_design_tag.tagname = '{msg}'"))
        if size == "指定無し":
            data = Image.objects.raw((f"select distinct * from  show_design_imagetag inner join show_design_image on show_design_imagetag.imageid = show_design_image.imageid inner join show_design_tag on show_design_imagetag.tagid = show_design_tag.tagid where show_design_tag.tagname = '{msg}'"))
        else:
            data = Image.objects.raw((f"select distinct * from  show_design_imagetag inner join show_design_image on show_design_imagetag.imageid = show_design_image.imageid inner join show_design_tag on show_design_imagetag.tagid = show_design_tag.tagid inner join show_design_desk on show_design_imagetag.imageid = show_design_desk.imageid where show_design_tag.tagname = '{msg}' and show_design_desk.sizename = '{size}'"))
        print(data)
    params = {
        'title' : title,
        'message': "ガジェット: " + msg + ", デスクのサイズ: " + size,
        'form':form,
        'data':data,
        'tags' : tags,
        'desk': desk,
        'urls' : urls,
    }
    return render(request,'showdesign/find.html',params)

# Create your views here.
