# from django.shortcuts import render

# # Create your views here.
# def showMessage(request):
#     return render(request, 'message/message.html');

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponseForbidden
from django.shortcuts import render
from django.urls import reverse
from django.views.generic.edit import FormMixin

from django.views.generic import DetailView, ListView

from .forms import ComposeForm
from .models import Thread, ChatMessage
from cse312.users.models import User

class InboxView(LoginRequiredMixin, ListView):
    template_name = 'message/message.html'
    def get_queryset(self):
        return Thread.objects.by_user(self.request.user)


class ThreadView(LoginRequiredMixin, FormMixin, DetailView):
    template_name = 'message/message.html'
    form_class = ComposeForm
    success_url = './'

    def get_queryset(self):
        return Thread.objects.by_user(self.request.user)

    def get_object(self):
        other_username  = self.kwargs.get("username")
        obj, created    = Thread.objects.get_or_new(self.request.user, other_username)
        if obj == None:
            raise Http404
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.get_form()
        return context

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseForbidden()
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        thread = self.get_object()
        user = self.request.user
        message = form.cleaned_data.get("message")
        ChatMessage.objects.create(user=user, thread=thread, message=message)
        return super().form_valid(form)

@login_required
def GetThread(request, username):
    other_username  = User.objects.get(user_name=username)
    obj, created = Thread.objects.get_or_new(request.user, other_username)
    if obj == None:
        raise Http404
    messages = ChatMessage.objects.filter(thread=obj)
    form = ComposeForm(request.POST or None)
    args = {
    'thread':obj,
    'messages':messages,
    'form':form
    }
    if request.method == 'POST':
        if form.is_valid():
            f = form.save(commit = False)
            f.thread = obj
            f.user = request.user
            f.save()
            return HttpResponseRedirect(request.path_info)
        else:
            form = ComposeForm()
    return render(request, 'message/message.html', args)
    # return obj
