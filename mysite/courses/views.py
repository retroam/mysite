from models import *
from mysite.blog.models import Blog, Post
from django import forms
from django.http import HttpResponseForbidden, Http404
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.sites.models import Site
from django.core.paginator import Paginator, InvalidPage, EmptyPage
import datetime

def info(request, slug, year, semester):
    o = {}
    o['course'] = get_object_or_404(
        Course, slug=slug, year=year, semester=semester)
    return render_to_response('info.html', o)

def schedule(request, slug, year, semester):
    o = {}
    o['course'] = get_object_or_404(
        Course, slug=slug, year=year, semester=semester)
    o['meetings'] = list(o['course'].meetings.all())
    o['holidays'] = list(o['course'].holidays.all())
    assignments = {}
    for i, assignment in enumerate(o['course'].assignments.all()):
        assignment.number = (i + 1)
        assignments[assignment.due_date] = assignment
    for meeting in o['meetings']:
        meeting.assignment_due = assignments.get(meeting.date, None)
    
    o['schedule'] = o['meetings'] + o['holidays']
    o['schedule'].sort(key=lambda x: x.date)
    today = datetime.date.today()
    for item in o['schedule']:
        if item.date >= today:
            item.next = True
            break
    o['user_is_authorized'] = o['course'].is_authorized(request.user)
    return render_to_response('schedule.html', o,
                              context_instance=RequestContext(request))

def guidelines(request, slug, year, semester):
    o = {}
    o['course'] = get_object_or_404(
        Course, slug=slug, year=year, semester=semester)
    return render_to_response('guidelines.html', o)

def assignments(request, slug, year, semester):
    o = {}
    o['course'] = get_object_or_404(
        Course, slug=slug, year=year, semester=semester)
    return render_to_response('assignments.html', o)

class DiscussionForm(forms.Form):
    questions = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 20, 'cols':80}))

@login_required
def discussion(request, discussion_id):
    o = {}
    o['assigned'] = get_object_or_404(
        ReadingAssignment, id=discussion_id)
    o['course'] = o['assigned'].meeting.course
    if not o['course'].is_authorized(request.user):
        return HttpResponseForbidden()
    if o['assigned'].discussion_leader == request.user:
        if request.method == 'POST':
            form = DiscussionForm(request.POST)
            if form.is_valid():
                o['assigned'].discussion_questions = form.cleaned_data['questions']
                o['assigned'].save()
                messages.add_message(
                    request, messages.SUCCESS, 'Your questions have been saved.')
        else:
            form = DiscussionForm(
                { 'questions': o['assigned'].discussion_questions })
        o['form'] = form
    return render_to_response('discussion.html', o,
                              context_instance=RequestContext(request))

def get_current_course(slug):
    today = datetime.date.today()
    if today.month in range(1,5):
        current_semester = 'sp'
    elif today.month in range(5,8):
        current_semester = 'su'
    else:
        current_semester = 'fa'
    return Course.objects.get(
        slug=slug, year=today.year, semester=current_semester)

def blog(request, slug, post_slug=None):
    o = {}
    o['blog'] = get_object_or_404(Blog, slug=slug)
    o['domain'] = Site.objects.get_current().domain
    o['course'] = get_current_course(slug)
    o['user_is_authorized'] = o['course'].is_authorized(request.user)
    if post_slug:
        posts = o['blog'].posts.filter(slug=post_slug, published=True)
        if len(posts) == 0:
            raise Http404
        o['show_comment_form'] = True
        o['next'] = posts[0].get_absolute_url()
    elif 'mine' in request.GET:
        posts = o['blog'].posts.filter(author=request.user).order_by('-updated_at')
    else:
        posts = o['blog'].posts.filter(published=True)
    paginator = Paginator(posts, 10)
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1
    try:
        o['page'] = paginator.page(page)
    except (EmptyPage, InvalidPage):
        o['page'] = paginator.page(paginator.num_pages)
    return render_to_response('blog.html', o,
                              context_instance=RequestContext(request))

def post(request, slug, post_slug):
    pass

class BlogPostForm(forms.Form):
    title = forms.CharField(max_length=80)
    slug = forms.CharField(max_length=50)
    content = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 20, 'cols':80}))
    display_name = forms.CharField(required=False, max_length=32)

@login_required
def edit_post(request, slug, post_slug=None):
    o = {}
    o['blog'] = get_object_or_404(Blog, slug=slug)
    o['course'] = get_current_course(slug)
    if post_slug: # editing existing post
        post = o['blog'].posts.get(slug=post_slug)
        if not post.author == request.user:
            return HttpResponseForbidden()
        if request.method == 'POST':
            form = BlogPostForm(request.POST)
            if form.is_valid():
                post.content = form.cleaned_data['content']
                post.display_name = form.cleaned_data['display_name']
                if post.published:
                    message = 'Your post has been updated.'
                    next = post.get_absolute_url()
                else:
                    post.title = form.cleaned_data['title']
                    post.slug = form.cleaned_data['slug']
                    if 'publish' in request.POST:
                        post.published = True
                        post.published_at = datetime.datetime.now()
                        message = 'Your post has been published.'
                        next = post.get_absolute_url()
                    else:
                        message = 'Your draft has been saved.'
                        next = post.get_edit_url()
                post.save()
                messages.add_message(request, messages.SUCCESS, message)
                return redirect(next)
        else:
            form = BlogPostForm({ 'title': post.title,
                                  'slug': post.slug,
                                  'content': post.content,
                                  'display_name': post.display_name })
            if post.published:
                o['post_published'] = True
                for field in ['title', 'slug']:
                    form.fields[field].widget.attrs['readonly'] = True
    else:         # creating new post
        if not o['course'].is_authorized(request.user):
            return HttpResponseForbidden()
        if request.method == 'POST':
            form = BlogPostForm(request.POST)
            if form.is_valid():
                post = Post(blog=o['blog'], author=request.user)
                post.title = form.cleaned_data['title']
                post.slug = form.cleaned_data['slug']
                post.content = form.cleaned_data['content']
                post.display_name = form.cleaned_data['display_name']
                if 'publish' in request.POST:
                    post.published = True
                    post.published_at = datetime.datetime.now()
                    message = 'Your post has been published.'
                    next = post.get_absolute_url()
                else:
                    message = 'Your draft has been saved.'
                    next = post.get_edit_url()
                post.save()
                messages.add_message(request, messages.SUCCESS, message)
                return redirect(next)
        else:
            form = BlogPostForm(initial={ 
                    'display_name': (request.user.get_full_name() or 
                                     request.user.username) })
    o['form'] = form
    return render_to_response('edit_post.html', o,
                              context_instance=RequestContext(request))
        
                
            

