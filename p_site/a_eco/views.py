from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, View, DetailView, CreateView
from django.contrib import messages
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout


from .models import *
from .forms import *
import requests


class ecohome(ListView):
    model = ecologiya

    template_name = "a_eco/base.html"

    context_object_name = "model_list"



class search(ListView):
    template_name = "a_eco/partials.html"
    context_object_name = "search_list"
    paginate_by = 5

    def get_queryset(self):
        get_search = self.request.GET.get("q")
        if get_search.endswith(" "):
            get_search = get_search.rstrip()
            
        return ecologiya.objects.filter(title__icontains=get_search)
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["q"] = self.request.GET.get("q")
        return context
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        value_of_search = self.request.GET.get("q")
        context.update({
            "search_value": value_of_search,

        })
        return context
    
class plug(ListView):
    template_name = "a_eco/aboutus.html"
    context_object_name = "pass_list"

    def get_queryset(self):
        pass

class contacts_plug(ListView):
    template_name = "a_eco/contacts.html"
    context_object_name = "contacts_plug_list"

    def get_queryset(self):
        pass

class product(ListView):
    model = ecologiya
    template_name = "a_eco/products.html"
    context_object_name = "products_list"
    allow_empty = False
    
    def get_context_data(self, **kwargs):
        post = get_object_or_404(ecologiya, slug=self.kwargs['slug'])

        content_model = ecologiya.objects.get(slug=self.kwargs['slug'])

        context = {
            "title": post.title,
            "price": post.price,
            "content_model": content_model.content,
            "foto": content_model.foto,
            "price_for_sell": "КУПИТЬ ЗА " + str(post.price) + " ₽",
        }

        return context
    
class link(ListView):
    model = ecologiya
    template_name = "a_eco/link.html"
    context_object_name = "link_list"

    def get_context_data(self, **kwargs):
        pass

class technical_support(LoginRequiredMixin, View):
    form = support_admin()
    template_name = "a_eco/support.html"
    context_object_name = "support_list"
    login_url = reverse_lazy("home")
    raise_exception = True

    def get(self, request):
        context = {
            'form': self.form
        }
        return render(request, self.template_name, context)
    
    def post(self, request):
        form = support_admin(request.POST, request.FILES)
        context = {
            "form": form,
        }

        if form.is_valid():
            form.save()
            context.update({
                'text_after_post': "Ваш вопрос был сформирован и отправлен",
                'form': support_admin(),
            })
    
        return render(request, self.template_name, context)
    
class register_user(CreateView):
    form_class = register_user_form
    template_name = "a_eco/register.html"
    context_object_name = "register_list"
    success_url = reverse_lazy('login')

class login_user(LoginView):
    form_class = login_user_form
    template_name = "a_eco/login.html"
    context_object_name = "register_list"
    

    def get_success_url(self):
        return reverse_lazy('home')

    

    # def get_queryset(self):
    #     pass

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['form'] = support_admin()
    #     return context

    # def upload_file(self, request, *args, **kwargs):
    #     if request.method == 'POST':
    #         form = support_admin(request.POST, request.FILES)
    #         if form.is_valid():
    #             print(form.cleaned_data)
    #             form.save()
    #             return redirect('home')
    #     else:
    #         form = support_admin()
    #         context = {'form': form}
    #         return context
        

def logout_user(request):
    logout(request)
    return redirect('login')

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
