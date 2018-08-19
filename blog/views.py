from django.shortcuts import render,redirect,get_object_or_404
from . models import Post,Profile,Comments
from . forms import (UserRegistrationForm,
						Login_Form,Profile_Form,User_form,
                        PostForm,PostEditForm,CommentForm
					)
from django.template.loader import render_to_string
from django.http import HttpResponseRedirect,JsonResponse,HttpResponse
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User

# Create your views here.
def Index_View(request):
    return render(request,'blog/index.html',{})

def Post_List_View(request):
	posts = Post.objects.all().order_by('-id')
	context ={
		'posts' : posts
	}
	return render(request,'blog/post_list.html',context)

def Create_Post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.authour=(request.user)
            post.save()
            print(form.cleaned_data)
            return redirect('posts')
    else:
        form = PostForm()
        context  = {
            'form':form
        } 
    return render(request,'blog/create_post.html',context)


def Post_Edit(request,id):
    post = get_object_or_404(Post,id=id)
    if request.method == 'POST':
        form = PostEditForm(request.POST,instance=post)
        if form.is_valid():
            form.save()
            return redirect('posts')
    else:
        form = PostEditForm(instance=post)
        context = {
         'form': form,
         # 'post': post,
        }
    return render(request, 'blog/post_edit.html', context)

def Post_Delete(request,id):
    post = get_object_or_404(Post,id=id)
    post.delete()
    return redirect('posts')

def Post_Detail_View(request,id):
    post    = get_object_or_404(Post,id=id)
    is_liked = False
    if post.likes.filter(id=request.user.id).exists():
        is_liked = True
    comments = Comments.objects.filter(post=post).order_by('-id')
    if request.method == 'POST':
        form = CommentForm(request.POST)
        form.is_valid()
        content = request.POST.get('comment')
        comment = Comments.objects.create(post=post,user=request.user,
                                                            comment=content) 
        comment.save()
        # return redirect(post.get_absolute_url())
    form = CommentForm()
    context = {

        'post':post,
        'is_liked':is_liked,
        'likes_count':post.likes_count(),
        'comments':comments,
        'form' : form
    }
    if request.is_ajax():
        html = render_to_string('blog/comments.html',context,request=request)
        return JsonResponse({'form':html})
    return render(request,'blog/post_details.html',context)

def Like_Post(request):
    # post = get_object_or_404(Post,id=request.POST.get('post_id'))
    post = get_object_or_404(Post,id=request.POST.get('id'))
    is_liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        is_liked = False
    else:    
        post.likes.add(request.user)
        is_liked = True
    # print(is_liked)
    context = {
        'post':post,
        'is_liked':is_liked,
        'likes_count':post.likes_count()
    }
    if request.is_ajax():
        html = render_to_string('blog/like_section.html',context,request=request)
        return JsonResponse({'form':html})
    # return HttpResponseRedirect(post.get_absolute_url())


def Create_User_View(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST or None)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            UserProfile.objects.create(user=new_user)
            return redirect('index')
    else:
        form = UserRegistrationForm()
    context = {
        'form': form,
    }
    return render(request, 'registration/user_creation.html', context)

def Login_view(request):
    if request.method == 'POST':
        form = Login_Form(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    login(request,user)
                    return redirect('posts')
                else:
                    return HttpResponse("User is not active")
            else:
                return HttpResponse("not valid")
    else:
        form = Login_Form()
        return render(request,'registration/login.html',{'form':form})

def Log_Out(request):
    logout(request)
    return redirect('posts')


def Profile_View(request):
    user     = request.user
    profile  = request.user.profile    
    context ={
        'user'    : user,
        'profile' : profile
    }
    return render(request,'registration/profile.html',context)


def Profile_Update(request):
    if request.method == 'POST':
        userform = User_form(data=request.POST or None,
        									 instance=request.user)
        profileform = Profile_Form(data=request.POST , 
        				instance=request.user.profile, files=request.FILES)
        if userform and profileform.is_valid():
            userform.save()
            profileform.save()
            return redirect('posts')
    else:
        userform   = User_form(instance=request.user)
        profileform  = Profile_Form(instance=request.user.profile)

        context  = {      
                'userform' : userform,
                'profileform'  : profileform
        }
     

        return render(request,'registration/update.html',context)













