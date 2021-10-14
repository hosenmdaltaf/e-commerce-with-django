from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm     #UserCreationForm,
from django.contrib.auth import login,logout
from django.contrib import messages
from .forms import UserRegisterForm
from accounts.models import Profile
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import (
      DetailView,
    #   CreateView,
      UpdateView,
      DeleteView
)

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import get_object_or_404







# @method_decorator(login_required, name='dispatch')
class ProfileDetailView(DetailView):
    model = Profile
    context_object_name = 'profiles'
    template_name = 'accounts/detailpage.html' 

    def get_object(self,**kwargs):
        pk= self.kwargs.get('pk')
        view_profile = Profile.objects.get(pk=pk)
        return view_profile


# def profiledetail(request):
#     profile=get_object_or_404(Profile, user=request.user)
#     return render(request,'accounts/detailpage.html',{'profile':profile})



@method_decorator(login_required, name='dispatch')
class ProfileUpdateView(UpdateView):
    model = Profile
    # context_object_name = 'accounts'
    fields=['profile_picture','bio','full_name','loaction','email']
    template_name='accounts/profile_update_form.html'
    success_url = reverse_lazy("forntpage:home")

    # def form_valid(self,form):
    #     form.instance = self.request.user
    #     return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class ProfileDeleteView(DeleteView):
    model=Profile
    # context_object_name = 'profile_delete'
    template_name='accounts/profile_delete_form.html'
    success_url = reverse_lazy("forntpage:home")



def signup(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            messages.success(request,f'Your account has created ! You are now able to log in')
            return redirect ('accounts:login')
    else:
        form =UserRegisterForm()
    return render (request,'accounts/signup.html',{'form':form})



def login_view(request):
    if request.method == 'POST':
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            #login the user
            user=form.get_user()
            login(request,user)
            return redirect('products:allproduct')
    else:
        form=AuthenticationForm()
    return render(request,'accounts/login.html',{'form':form})


@login_required(login_url ='/accounts/login/')
def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('accounts:logout')
    return render(request,'accounts/logout.html')