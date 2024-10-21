from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from django.http import JsonResponse


def note_list(request):
    post = Post.objects.filter(is_deleted=False).first()
    notes = Note.objects.filter(deleted=False)
    photo = Photo.objects.filter(is_deleted=False).first()

    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('note_list')
    else:
        form = NoteForm()

    if request.method == 'POST':
        form_photo = PhotoForm(request.POST)
        if form_photo.is_valid():
            form_photo.save()
            return redirect('note_list')
    else:
        form_photo = PhotoForm()
    return render(request, 'myapp/firststep/post_list.html',
                  {'notes': notes, 'form': form, 'post': post, "form_photo": form_photo, "photo": photo})


def second_page(request):
    post = Post.objects.filter(is_deleted=False).first()
    notes = Note.objects.filter(deleted=False)
    photo = Photo.objects.filter(is_deleted=False).first()

    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('second_page')
    else:
        form = NoteForm()

    if request.method == 'POST':
        form_photo = PhotoForm(request.POST)
        if form_photo.is_valid():
            form_photo.save()
            return redirect('second_page')
    else:
        form_photo = PhotoForm()
    return render(request, 'myapp/firststep/second_page.html',
                  {'notes': notes, 'form': form, 'post': post, "form_photo": form_photo, "photo": photo})


def third_page(request):
    post = Post.objects.filter(is_deleted=False)
    notes = Note.objects.filter(deleted=False)
    photo = Photo.objects.filter(is_deleted=False).first()

    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('third_page')
    else:
        form = NoteForm()

    if request.method == 'POST':
        form_photo = PhotoForm(request.POST)
        if form_photo.is_valid():
            form_photo.save()

            return redirect('third_page')
    else:
        form_photo = PhotoForm()
    return render(request, 'myapp/firststep/thirdpage.html',
                  {'notes': notes, 'form': form, 'post': post, "form_photo": form_photo, "photo": photo})


def second_step_page_first(request):
    post = Post.objects.filter(is_deleted=False).first()
    notes = Note.objects.filter(deleted=False)
    photo = Photo.objects.filter(is_deleted=False).first()

    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('second_step_page_second')
    else:
        form = NoteForm()

    if request.method == 'POST':
        form_photo = PhotoForm(request.POST)
        if form_photo.is_valid():
            form_photo.save()
            return redirect('second_step_page_second')
    else:
        form_photo = PhotoForm()
    return render(request, 'myapp/secondstep/pagefirst.html',
                  {'notes': notes, 'form': form, 'post': post, "form_photo": form_photo, "photo": photo})


def second_step_page_second(request):
    post = Post.objects.filter(is_deleted=False).first()
    return render(request, "myapp/secondstep/page2.html", {"post": post})


def second_step_page_third(request):
    photo = Photo.objects.filter(is_deleted=False).first()
    if request.method == 'POST':
        form_photo = PhotoForm(request.POST)
        if form_photo.is_valid():
            form_photo.save()
            return redirect('second_step_page_third')
    else:
        form_photo = PhotoForm()
    return render(request, "myapp/secondstep/page3.html", {"form_photo": form_photo, "photo": photo})


def second_step_page_forth(request):
    post = Post.objects.filter(is_deleted=False).first()
    notes = Note.objects.filter(deleted=True)
    photo = Photo.objects.filter(is_deleted=False).first()

    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('second_step_page_forth')
    else:
        form = NoteForm()

    if request.method == 'POST':
        form_photo = PhotoForm(request.POST)
        if form_photo.is_valid():
            form_photo.save()
            return redirect('second_step_page_forth')
    else:
        form_photo = PhotoForm()
    return render(request, 'myapp/secondstep/page4.html',
                  {'notes': notes, 'form': form, 'post': post, "form_photo": form_photo, "photo": photo})


def third_step_page_one(request):
    post = Post.objects.filter(is_deleted=False).first()
    notes = Note.objects.filter(deleted=False)
    photo = Photo.objects.filter(is_deleted=False).first()

    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('third_step_page_one')
    else:
        form = NoteForm()

    if request.method == 'POST':
        form_photo = PhotoForm(request.POST)
        if form_photo.is_valid():
            form_photo.save()
            return redirect('third_step_page_one')
    else:
        form_photo = PhotoForm()
    return render(request, 'myapp/thirdstep/page1.html',
                  {'notes': notes, 'form': form, 'post': post, "form_photo": form_photo, "photo": photo})


def third_step_page_four(request):
    post = Post.objects.filter(is_deleted=False).first()
    photo = Photo.objects.filter(is_deleted=False).first()
    images = Image.objects.all()

    return render(request, "./myapp/thirdstep/page4.html", {"post": post, "photo": photo, "images": images})


def third_step_page_prefour(request):
    post = Post.objects.filter(is_deleted=False).first()
    photo = Photo.objects.filter(is_deleted=False).first()
    images = Image.objects.all()

    return render(request, "./myapp/thirdstep/pagepre4.html", {"post": post, "photo": photo, "images": images})


def delete_photo_third_step_page_one(request):
    photo = get_object_or_404(Photo, is_deleted=False)
    photo.is_deleted = True
    photo.save()
    return redirect('third_step_page_one')


def restore_photo_third_step_page_one(request):
    photo = get_object_or_404(Photo, is_deleted=True)
    photo.is_deleted = False
    photo.save()
    return redirect('third_step_page_one')


def delete_post_third_step_page_one(request):
    post = get_object_or_404(Post, is_deleted=False)
    post.is_deleted = True
    post.save()
    return redirect('third_step_page_one')


def restore_post_third_step_page_one(request):
    post = get_object_or_404(Post, is_deleted=True)
    post.is_deleted = False
    post.save()
    return redirect('third_step_page_one')


def third_step_page_two(request):
    post = Post.objects.filter(is_deleted=False).first()
    notes = Note.objects.filter(deleted=False)
    photo = Photo.objects.filter(is_deleted=False).first()

    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('third_step_page_two')
    else:
        form = NoteForm()

    if request.method == 'POST':
        form_photo = PhotoForm(request.POST)
        if form_photo.is_valid():
            form_photo.save()
            return redirect('third_step_page_two')
    else:
        form_photo = PhotoForm()
    return render(request, 'myapp/thirdstep/page2.html',
                  {'notes': notes, 'form': form, 'post': post, "form_photo": form_photo, "photo": photo})


def delete_photo_third_step_page_two(request):
    photo = get_object_or_404(Photo, is_deleted=False)
    photo.is_deleted = True
    photo.save()
    return redirect('third_step_page_two')


def restore_photo_third_step_page_two(request):
    photo = get_object_or_404(Photo, is_deleted=True)
    photo.is_deleted = False
    photo.save()
    return redirect('third_step_page_two')


def delete_post_third_step_page_two(request):
    post = get_object_or_404(Post, is_deleted=True)
    post.is_deleted = False
    post.save()
    return redirect('third_step_page_two')


def restore_post_third_step_page_two(request):
    post = get_object_or_404(Post, is_deleted=False)
    post.is_deleted = True
    post.save()
    return redirect('third_step_page_two')


def third_step_page_three(request):
    post = Post.objects.filter(is_deleted=False).first()
    notes = Note.objects.filter(deleted=False)
    photo = Photo.objects.filter(is_deleted=False).first()

    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('third_step_page_three')
    else:
        form = NoteForm()

    if request.method == 'POST':
        form_photo = PhotoForm(request.POST)
        if form_photo.is_valid():
            form_photo.save()
            return redirect('third_step_page_three')
    else:
        form_photo = PhotoForm()
    return render(request, 'myapp/thirdstep/page3.html',
                  {'notes': notes, 'form': form, 'post': post, "form_photo": form_photo, "photo": photo})


def delete_photo_third_step_page_three(request):
    photo = get_object_or_404(Photo, is_deleted=False)
    photo.is_deleted = True
    photo.save()
    return redirect('third_step_page_three')


def restore_photo_third_step_page_three(request):
    photo = get_object_or_404(Photo, is_deleted=True)
    photo.is_deleted = False
    photo.save()
    return redirect('third_step_page_three')


def delete_post_third_step_page_three(request):
    post = get_object_or_404(Post, is_deleted=True)
    post.is_deleted = False
    post.save()
    return redirect('third_step_page_three')


def restore_post_third_step_page_three(request):
    post = get_object_or_404(Post, is_deleted=False)
    post.is_deleted = True
    post.save()
    return redirect('third_step_page_three')


def delete_photo_second_step_page_fifth(request):
    photo = get_object_or_404(Photo, is_deleted=False)
    photo.is_deleted = True
    photo.save()
    return redirect('second_step_page_fifth')


def restore_photo_second_step_page_fifth(request):
    photo = get_object_or_404(Photo, is_deleted=True)
    photo.is_deleted = False
    photo.save()
    return redirect('second_step_page_fifth')


def delete_post_second_step_page_fifth(request):
    post = get_object_or_404(Post, is_deleted=True)
    post.is_deleted = False
    post.save()
    return redirect('second_step_page_fifth')


def restore_post_second_step_page_fifth(request):
    post = get_object_or_404(Post, is_deleted=False)
    post.is_deleted = True
    post.save()
    return redirect('second_step_page_fifth')


def second_step_page_fifth(request):
    post = Post.objects.filter(is_deleted=False).first()
    notes = Note.objects.filter(deleted=False)
    photo = Photo.objects.filter(is_deleted=False).first()

    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('second_step_page_fifth')
    else:
        form = NoteForm()

    if request.method == 'POST':
        form_photo = PhotoForm(request.POST)
        if form_photo.is_valid():
            form_photo.save()
            return redirect('second_step_page_fifth')
    else:
        form_photo = PhotoForm()
    return render(request, 'myapp/secondstep/page5.html',
                  {'notes': notes, 'form': form, 'post': post, "form_photo": form_photo, "photo": photo})


def restore_photo_second_step_page_third(request):
    photo = get_object_or_404(Photo, is_deleted=True)
    photo.is_deleted = False
    photo.save()
    return redirect('second_step_page_third')


def delete_photo_second_step_page_third(request):
    photo = get_object_or_404(Photo, is_deleted=False)
    photo.is_deleted = True
    photo.save()
    return redirect('second_step_page_third')


def delete_photo_second_step_page_first(request):
    photo = get_object_or_404(Photo, is_deleted=False)
    photo.is_deleted = True
    photo.save()
    return redirect('second_step_page_first')


def restore_photo_second_step_page_first(request):
    photo = get_object_or_404(Photo, is_deleted=True)
    photo.is_deleted = False
    photo.save()
    return redirect('second_step_page_first')


def delete_post_second_step_page_first(request):
    post = get_object_or_404(Post, is_deleted=False)
    post.is_deleted = True
    post.save()
    return redirect('second_step_page_first')


def restore_post_second_step_page_first(request):
    post = get_object_or_404(Post, is_deleted=True)
    post.is_deleted = False
    post.save()
    return redirect('second_step_page_first')


def delete_photo(request):
    photo = get_object_or_404(Photo, is_deleted=False)
    photo.is_deleted = True
    photo.save()
    return redirect('note_list')


def restore_photo(request):
    photo = get_object_or_404(Photo, is_deleted=True)
    photo.is_deleted = False
    photo.save()
    return redirect('note_list')


def delete_post(request):
    post = get_object_or_404(Post, is_deleted=False)
    post.is_deleted = True
    post.save()
    return redirect('note_list')


def restore_post(request):
    post = get_object_or_404(Post, is_deleted=True)
    post.is_deleted = False
    post.save()
    return redirect('note_list')


def delete_photo_second_page(request):
    photo = get_object_or_404(Photo, is_deleted=False)
    photo.is_deleted = True
    photo.save()
    return redirect('second_page')


def restore_photo_second_page(request):
    photo = get_object_or_404(Photo, is_deleted=True)
    photo.is_deleted = False
    photo.save()
    return redirect('second_page')


def delete_post_second_page(request):
    post = get_object_or_404(Post, is_deleted=True)
    post.is_deleted = False
    post.save()
    return redirect('second_page')


def delete_photo_second_step_page_forth(request):
    photo = get_object_or_404(Photo, is_deleted=False)
    photo.is_deleted = True
    photo.save()
    return redirect('second_step_page_forth')


def restore_photo_second_step_page_forth(request):
    photo = get_object_or_404(Photo, is_deleted=True)
    photo.is_deleted = False
    photo.save()
    return redirect('second_step_page_forth')


def delete_post_second_step_page_forth(request):
    post = get_object_or_404(Post, is_deleted=False)
    post.is_deleted = True
    post.save()
    return redirect('second_step_page_forth')


def restore_post_second_step_page_forth(request):
    post = get_object_or_404(Post, is_deleted=False)
    post.is_deleted = True
    post.save()
    return redirect('second_step_page_forth')


def restore_post_second_page(request):
    post = get_object_or_404(Post, is_deleted=False)
    post.is_deleted = True
    post.save()
    return redirect('second_page')


def delete_photo_third_page(request):
    photo = get_object_or_404(Photo, is_deleted=False)
    photo.is_deleted = True
    photo.save()
    return redirect('third_page')


def restore_photo_third_page(request):
    photo = get_object_or_404(Photo, is_deleted=True)
    photo.is_deleted = False
    photo.save()
    return redirect('third_page')


def delete_post_third_page(request):
    post = get_object_or_404(Post, is_deleted=True)
    post.is_deleted = False
    post.save()
    return redirect('third_page')


def restore_post_third_page(request):
    post = get_object_or_404(Post, is_deleted=False)
    post.is_deleted = True
    post.save()
    return redirect('third_page')


def forth_page(request):
    photo = Photo.objects.filter(is_deleted=False).first()

    if request.method == 'POST':
        form_photo = PhotoForm(request.POST)
        if form_photo.is_valid():
            form_photo.save()
            return redirect('forth_page')
    else:
        form_photo = PhotoForm()
    return render(request, 'myapp/firststep/forth_page.html',
                  {"form_photo": form_photo, "photo": photo})


def delete_photo_forth_page(request):
    photo = get_object_or_404(Photo, is_deleted=False)
    photo.is_deleted = True
    photo.save()
    return redirect('forth_page')


def restore_photo_forth_page(request):
    photo = get_object_or_404(Photo, is_deleted=True)
    photo.is_deleted = False
    photo.save()
    return redirect('forth_page')


def third_step_page_four(request):
    return render(request, "myapp/thirdstep/page4.html")


def third_step_page_five(request):
    return render(request, "myapp/thirdstep/page5.html")


# def index(request):
#     texts = Text.objects.all()
#     current_index = request.session.get('current_index', -1)
#
#     if request.method == 'POST':
#         current_index += 1
#
#     # بررسی اینکه آیا متنی برای نمایش وجود دارد یا خیر
#     if current_index < 0 or current_index >= len(texts):
#         display_text = None  # Reset if index is out of bounds
#         request.session['current_index'] = -1  # Reset the index
#     else:
#         if current_index < len(texts):  # Ensure the index is within bounds
#             request.session['current_index'] = current_index  # Update the session index
#             current_text = texts[current_index]
#             display_text = [
#                 current_text.x,
#                 current_text.y,
#                 current_text.z,
#                 current_text.m,
#             ][current_index % 4]  # Cycle through the texts
#         else:
#             display_text = None  # No more texts to display
#
#     return render(request, 'myapp/thirdstep/mafoolStage/page1.html', {'display_text': display_text})


# click_count = 0

#
def mafool_first_page(request):
    return render(request, 'myapp/thirdstep/mafoolStage/page1.html')
    # global click_count
    # data = Text.objects.first()  # فرض بر این است که فقط یک رکورد داریم
    # response_data = ""
    #
    # if click_count == 0:
    #     response_data = data.x
    # elif click_count == 1:
    #     response_data = data.y
    # elif click_count == 2:
    #     response_data = data.z
    # elif click_count == 3:
    #     response_data = data.m
    #
    # click_count += 1
    # if click_count > 3:
    #     click_count = 0
    #
    # return JsonResponse({'data': response_data})
# def mafool_first_page(request):
#
#
#   return render(request, 'myapp/thirdstep/mafoolStage/page1.html')
#
# return render(request, 'myapp/thirdstep/mafoolStage/page1.html',
#               { 'form': form, 'post_item': post_item})


# def delete_mafool_one(request):
#     post_item = get_object_or_404(Post, is_deleted=True)
#     post_item.is_deleted = False
#     post_item.save()
#     return redirect('mafool_first_page')
#
#
# def restore_mafool_one(request):
#     post_item = get_object_or_404(Post, is_deleted=False)
#     post_item.is_deleted = True
#     post_item.save()
#     return redirect('mafool_first_page')
def mafool_second_page(request):
    post = Post.objects.filter(is_deleted=False)
    notes = Note.objects.filter(deleted=False)
    photo = Photo.objects.filter(is_deleted=False).first()

    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mafool_second_page')
    else:
        form = NoteForm()

    if request.method == 'POST':
        form_photo = PhotoForm(request.POST)
        if form_photo.is_valid():
            form_photo.save()
            return redirect('mafool_second_page')
    else:
        form_photo = PhotoForm()

    return render(request, "myapp/thirdstep/mafoolStage/page2.html",
                  {'notes': notes, 'form': form, 'post': post, "form_photo": form_photo, "photo": photo})


def delete_photo_third_step_page_second_mafool(request):
    photo = get_object_or_404(Photo, is_deleted=False)
    photo.is_deleted = True
    photo.save()
    return redirect('mafool_second_page')


def restore_photo_third_step_page_second_mafool(request):
    photo = get_object_or_404(Photo, is_deleted=True)
    photo.is_deleted = False
    photo.save()
    return redirect('mafool_second_page')


def delete_post_third_step_page_second_mafool(request):
    post = get_object_or_404(Post, is_deleted=True)
    post.is_deleted = False
    post.save()
    return redirect('mafool_second_page')


def restore_post_third_step_page_second_mafool(request):
    post = get_object_or_404(Post, is_deleted=False)
    post.is_deleted = True
    post.save()
    return redirect('mafool_second_page')


def mafool_third_page(request):
    post = Post.objects.filter(is_deleted=False).first()
    return render(request,"myapp/thirdstep/mafoolStage/page3.html",{"post":post})

def mafool_fourth_page(request):
    post = Post.objects.filter(is_deleted=False).first()
    notes = Note.objects.filter(deleted=False)
    photo = Photo.objects.filter(is_deleted=False).first()

    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mafool_fourth_page')
    else:
        form = NoteForm()

    if request.method == 'POST':
        form_photo = PhotoForm(request.POST)
        if form_photo.is_valid():
            form_photo.save()
            return redirect('mafool_fourth_page')
    else:
        form_photo = PhotoForm()

    return render(request, "myapp/thirdstep/mafoolStage/page4.html",
                  {'notes': notes, 'form': form, 'post': post, "form_photo": form_photo, "photo": photo})

def delete_photo_third_step_page_fourth_mafool(request):
    photo = get_object_or_404(Photo, is_deleted=False)
    photo.is_deleted = True
    photo.save()
    return redirect('mafool_fourth_page')


def restore_photo_third_step_page_fourth_mafool(request):
    photo = get_object_or_404(Photo, is_deleted=True)
    photo.is_deleted = False
    photo.save()
    return redirect('mafool_fourth_page')


def delete_post_third_step_page_fourth_mafool(request):
    post = get_object_or_404(Post, is_deleted=True)
    post.is_deleted = False
    post.save()
    return redirect('mafool_fourth_page')


def restore_post_third_step_page_fourth_mafool(request):
    post = get_object_or_404(Post, is_deleted=False)
    post.is_deleted = True
    post.save()
    return redirect('mafool_fourth_page')

def mafool_fifth_page(request):
    post = Post.objects.filter(is_deleted=False).first()
    notes = Note.objects.filter(deleted=False)
    photo = Photo.objects.filter(is_deleted=False).first()
    if request.method == 'POST':
        form_photo = PhotoForm(request.POST)
        if form_photo.is_valid():
            form_photo.save()
            return redirect('mafool_fourth_page')
    else:
        form_photo = PhotoForm()

    return render(request, "myapp/thirdstep/mafoolStage/page5.html",
                  {'notes': notes, 'post': post, "form_photo": form_photo, "photo": photo})


def mafool_sixth_page(request):
        post = Post.objects.filter(is_deleted=False).first()
        notes = Note.objects.filter(deleted=False)
        photo = Photo.objects.filter(is_deleted=False).first()

        if request.method == 'POST':
            form = NoteForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('mafool_sixth_page')
        else:
            form = NoteForm()

        if request.method == 'POST':
            form_photo = PhotoForm(request.POST)
            if form_photo.is_valid():
                form_photo.save()
                return redirect('mafool_sixth_page')
        else:
            form_photo = PhotoForm()

        return render(request, "myapp/thirdstep/mafoolStage/page6.html",
                      {'notes': notes, 'form': form, 'post': post, "form_photo": form_photo, "photo": photo})
def delete_photo_third_step_page_sixth_mafool(request):
        photo = get_object_or_404(Photo, is_deleted=True)
        photo.is_deleted = False
        photo.save()
        return redirect('mafool_sixth_page')

def restore_photo_third_step_page_sixth_mafool(request):
        photo = get_object_or_404(Photo, is_deleted=False)
        photo.is_deleted = True
        photo.save()
        return redirect('mafool_sixth_page')

def delete_post_third_step_page_sixth_mafool(request):
        post = get_object_or_404(Post, is_deleted=True)
        post.is_deleted = False
        post.save()
        return redirect('mafool_sixth_page')

def restore_post_third_step_page_sixth_mafool(request):
        post = get_object_or_404(Post, is_deleted=False)
        post.is_deleted = True
        post.save()
        return redirect('mafool_sixth_page')

def mafool_seventh_page(request):
    post = Post.objects.filter(is_deleted=False).first()
    return render(request,"myapp/thirdstep/mafoolStage/page7.html",{"post":post})

def mafool_eighth_page(request):
    post = Post.objects.filter(is_deleted=False).first()
    return render(request,"myapp/thirdstep/mafoolStage/page8.html",{"post":post})

def mafool_nineth_page(request):

    return render(request,"myapp/thirdstep/mafoolStage/page9.html")


def mafool_tenth_page(request):

    return render(request,"myapp/thirdstep/mafoolStage/page10.html")

def mafool_eleventh_page(request):

    return render(request,"myapp/thirdstep/mafoolStage/page11.html")

def preposition_p_1(request):
    photo=Photo.objects.filter(is_deleted=False).first()
    post_item=Post.objects.filter(is_deleted=False).first()
    return render(request,"myapp/forthstep/preposition_part/p1.html",{"post_item":post_item , "photo":photo })
def preposition_p_2(request):
    photo=Photo.objects.filter(is_deleted=False).first()
    post_item=Post.objects.filter(is_deleted=False).first()
    return render(request,"myapp/forthstep/preposition_part/p2.html",{"post_item":post_item , "photo":photo })


def preposition_p_3(request):
    photo=Photo.objects.filter(is_deleted=False).first()
    post_item=Post.objects.filter(is_deleted=False).first()
    return render(request,"myapp/forthstep/preposition_part/p3.html",{"post_item":post_item , "photo":photo })

def preposition_p_4(request):
    photo=Photo.objects.filter(is_deleted=False).first()
    post_item=Post.objects.filter(is_deleted=False).first()
    return render(request,"myapp/forthstep/preposition_part/p4.html",{"post_item":post_item , "photo":photo })


def preposition_p_5(request):
    photo=Photo.objects.filter(is_deleted=False).first()
    post_item=Post.objects.filter(is_deleted=False).first()
    return render(request,"myapp/forthstep/preposition_part/p5.html",{"post_item":post_item , "photo":photo })



def preposition_p_6(request):

    post_item=Post.objects.filter(is_deleted=False).first()
    return render(request,"myapp/forthstep/preposition_part/p6.html",{"post_item":post_item  })



def preposition_p_7(request):

    post_item=Post.objects.filter(is_deleted=False).first()
    return render(request,"myapp/forthstep/preposition_part/p7.html",{"post_item":post_item  })



def preposition_p_8(request):

    post_item=Post.objects.filter(is_deleted=False).first()
    return render(request,"myapp/forthstep/preposition_part/p8.html",{"post_item":post_item  })

def preposition_p_9(request):

    post_item=Post.objects.filter(is_deleted=False).first()
    return render(request,"myapp/forthstep/preposition_part/p9.html",{"post_item":post_item  })

def adverb_p_1(request):

    post_item=Post.objects.filter(is_deleted=False).first()
    return render(request,"myapp/fifthstep/adverb/p1.html",{"post_item":post_item  })

def adverb_p_2(request):

    post_item=Post.objects.filter(is_deleted=False).first()
    return render(request,"myapp/fifthstep/adverb/p2.html",{"post_item":post_item  })


def adverb_p_3(request):

    post_item=Post.objects.filter(is_deleted=False).first()
    return render(request,"myapp/fifthstep/adverb/p3.html",{"post_item":post_item  })
def adverb_p_4(request):

    post_item=Post.objects.filter(is_deleted=False).first()
    return render(request,"myapp/fifthstep/adverb/p4.html",{"post_item":post_item  })

def final_p1(request):

    photo=Photo.objects.filter(is_deleted=False).first()
    post_item=Post.objects.filter(is_deleted=False).first()
    return render(request,"myapp/sixthstep/p1.html",{"post_item":post_item , "photo":photo  })





def select_images(request):
    images = Image.objects.all()  # تمام تصاویر را از دیتابیس می‌خوانیم

    return render(request, './myapp/thirdstep/select_images.html' , {'images': images})


def select_images1(request):
    images = Image.objects.all()  # تمام تصاویر را از دیتابیس می‌خوانیم

    return render(request, './myapp/thirdstep/select_images.html' , {'images': images})