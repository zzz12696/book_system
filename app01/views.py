from django.views import View
from django.shortcuts import render, redirect, HttpResponse

from app01 import models


# =========Class Based View==================
class AddPublisher(View):
    def get(self, request):
        return render(request, 'add_publisher.html')

    def post(self, request):
        new_name = request.POST.get('publisher_name', None)
        if new_name:
            models.Publisher.objects.create(name=new_name)
            return redirect('/publisher_list/')
        error_msg = '出版社名字不能为空'
        return render(request, 'add_publisher.html', {'error_msg': error_msg})


# =========Function Based View==================
def publisher_list(request):
    ret = models.Publisher.objects.all()
    return render(request, 'publisher_list.html', {'publisher_list': ret})


def add_publisher(request):
    error_msg = ''
    if request.method == 'POST':
        new_name = request.POST.get('publisher_name', None)
        if new_name:
            models.Publisher.objects.create(name=new_name)
            return redirect('/publisher_list/')
        error_msg = '出版社名字不能为空'
    return render(request, 'add_publisher.html', {'error': error_msg})


def delete_publisher(request, del_id):
    if del_id:
        models.Publisher.objects.get(id=del_id).delete()
        return redirect('/publisher_list/')
    else:
        return HttpResponse('要删除的数据不存在')


def edit_publisher(request, edit_id):
    error_msg = ''
    if request.method == 'POST':
        new_name = request.POST.get('publisher_name')
        if new_name:
            edit_pub = models.Publisher.objects.get(id=edit_id)
            edit_pub.name = new_name
            edit_pub.save()
            return redirect('/publisher_list/')
        else:
            error_msg = '出版社名不能为空'
    publisher_obj = models.Publisher.objects.get(id=edit_id)
    return render(request, 'edit_publisher.html', {'publisher': publisher_obj, 'error_msg': error_msg})


def book_list(request):
    all_book = models.Book.objects.all()
    return render(request, 'book_list.html', {'books': all_book})


def add_book(request):
    error_msg = ''
    ret = models.Publisher.objects.all()
    if request.method == 'POST':
        new_title = request.POST.get('book_title')
        if new_title:
            select_publisher_id = request.POST.get('publisher')
            models.Book.objects.create(title=new_title, publisher_id=select_publisher_id)
            return redirect('/book_list/')
        else:
            error_msg = '书名不能为空'
    return render(request, 'add_book.html', {'publisher_list': ret, 'error_msg': error_msg})


def delete_book(request, del_id):
    models.Book.objects.get(id=del_id).delete()
    return redirect('/book_list/')


def edit_book(request, edit_id):
    error_msg = ''
    if request.method == 'POST':
        new_title = request.POST.get('book_title')
        if new_title:
            new_publisher_id = request.POST.get('publisher')
            edit_book_obj = models.Book.objects.get(id=edit_id)
            edit_book_obj.title = new_title
            edit_book_obj.publisher_id = new_publisher_id
            edit_book_obj.save()
            return redirect('/book_list/')
        else:
            error_msg = '书名不能为空'
    edit_book_obj = models.Book.objects.get(id=edit_id)
    publisher_list = models.Publisher.objects.all()
    return render(request, 'edit_book.html', {'publisher_list': publisher_list, 'edit_book_obj': edit_book_obj, 'error_msg': error_msg})


def author_list(request):
    all_author = models.Author.objects.all()
    return render(request, 'author_list.html', {'author_list': all_author})


def add_author(request):
    error_msg = ''
    if request.method == 'POST':
        new_author = request.POST.get('author_name')
        if new_author:
            books = request.POST.getlist('books')  # POST提交的数据是多个值，如多选框，需要用getlist
            new_author_obj = models.Author.objects.create(name=new_author)
            new_author_obj.book.set(books)
            return redirect('/author_list/')
        else:
            error_msg = '作者姓名不能为空'
    books = models.Book.objects.all()
    return render(request, 'add_author.html', {'books': books, 'error_msg': error_msg})


def delete_author(request, del_id):
    models.Author.objects.get(id=del_id).delete()
    return redirect('/author_list/')


def edit_author(request, edit_id):
    error_msg = ''
    if request.method == 'POST':
        new_author_name = request.POST.get('author_name')
        if new_author_name:
            books = request.POST.getlist('books')
            edit_author_obj = models.Author.objects.get(id=edit_id)
            edit_author_obj.name = new_author_name
            edit_author_obj.book.set(books)
            edit_author_obj.save()
            return redirect('/author_list/')
        else:
            error_msg = '作者姓名不能为空'
    edit_author_obj = models.Author.objects.get(id=edit_id)
    books = models.Book.objects.all()
    return render(request, 'edit_author.html', {'edit_author_obj': edit_author_obj, 'books': books, 'error_msg': error_msg})


def index(request):
    return render(request, 'index.html')
