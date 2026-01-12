from django.shortcuts import render, get_object_or_404, redirect
from django.template.context_processors import request

from django.views.generic import TemplateView
from .forms import PostForm, PostEditForm
from .models import Post

class Home(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['greeting'] = """Блог -работающее веб-приложение с простыми и динамическими маршрутами,
                               где пользователи смогут просматривать посты, создавать новые и навигировать между
                               страницами."""
        return context


def new_post(request):
    template_name = 'PostForm.html'
    if (request.method == 'POST'):
        form = PostForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            post = Post(title=title, content = content)
            post.save()
            return redirect('list_posts')
#            return render(request, 'thanks.html', {'context':'Спасибо за информацию'})
    else:
        form = PostForm()
        return render(request, 'PostForm.html', {'form': form})



class list_post(TemplateView):
    template_name = 'list_posts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.all()
        return context


class detail_post(TemplateView):
    template_name = 'detail_post.html'

    def get_context_data(self,  **kwargs):
        context = super().get_context_data(**kwargs)
        post_id = kwargs['id']
#        print(post_id)
        try:
            post = Post.objects.get(id=post_id)
            context['title'] = post.title
            context['content'] = post.content
            return context
        except:
            print('error post not found')





class delete_post(TemplateView):
    template_name = 'thanks_delete.html'

    def get_context_data(self,  **kwargs):
        context = super().get_context_data(**kwargs)
        post_id = kwargs['id']
        post = get_object_or_404(Post, pk=post_id)
        post.delete()

#        return render(request, 'thanks_delete.html', {'context':context})
        return context

class edit_post(TemplateView):
    template_name = 'PostEditForm.html'

    def get_context_data(self,  **kwargs):
        context = super().get_context_data(**kwargs)
        post_id = kwargs['id']
        try:
            post = Post.objects.get(id=post_id)
            context['id'] = post.id
            context['title'] = post.title
            context['content'] = post.content
            return context
        except:
            print('post with id not found')

class update_post_classs(TemplateView):
    template_name = 'update_post_result.html'

    def get_context_data(self,  **kwargs):
        context = super().get_context_data(**kwargs)

        if (request.method == 'POST'):
            form = PostForm(request.POST)
            if form.is_valid():
                title = form.cleaned_data['title']
                content = form.cleaned_data['content']
                post_id = form.cleaned_data['post_id']
        # post_id = kwargs['id']
        # title  = kwargs['title']
        # content  = kwargs['content']

        Post.objects.filter(id=post_id).update(content=content, title=title)
        return context


def update_post(request):
    if (request.method == 'POST'):
        form = PostEditForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            post_id = int(form.cleaned_data['post_id'])
            Post.objects.filter(id=post_id).update(content=content, title=title)
#            return render(request, 'update_post_result.html')
            return render(request, 'thanks.html', {'context': 'Спасибо, пост обновлен'})
    else:

        return render(request, 'edit_post.html')












