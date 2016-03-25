from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from messageboard.models import *
from  messageboard.forms import *
from django.contrib.auth.decorators import login_required
# from django.views.generic import list_detail

items_per_page=10
"""
def msg_list_page(request):
    return list_detail.object_list(request,
                                   queryset=MsgPost.objects.order_by('-id'),
                                   paginate_by=items_per_page,
                                   page=1,
                                   template_name='main.html',
                                   template_object_name='main.html'
                                   )
"""
def main(request):
    posts = MsgPost.objects.all()#get all records
    return render_to_response('messageboard/main.html',{'posts':posts})

def register_page(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user( username=form.cleaned_data['username'],
                                             email=form.cleaned_data['email'],
                                             password=form.cleaned_data['password1'])
            return HttpResponseRedirect('/main/register/success/')
    else:
        form = RegistrationForm()
    variables = RequestContext(request,{'form':form})
    return render_to_response('registration/register.html', variables)

def register_success(request):
    return render_to_response('registration/register_success.html')

@login_required
def msg_post_page(request):
    if request.method=='POST':
        form = MsgPostForm(request.POST)
        if form.is_valid():
            newmessage = MsgPost(title=form.cleaned_data['title'],
                             content=form.cleaned_data['content'],
                             #user=request.user
                             )
            newmessage.save()
        return HttpResponseRedirect('/main/')
    else:
        form=MsgPostForm()
    variables=RequestContext(request,{'form':form})
    return render_to_response('messageboard/msg_post_page.html',variables)