from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.utils.decorators import method_decorator
from django.views import View
from django.urls import reverse

from myapp.forms import UserSettings, ProductForm
from myapp.models import Product


def index_page(request):
    context = {
        'pagename': 'Главная',
        'products': Product.objects.all()
    }
    return render(request, 'pages/index.html', context)


class ProductView(View):
    context = {
        'pagename': 'Новый товар',
    }
    new_product = False
    list_product = False

    @method_decorator(login_required)
    def get(self, request, id=-1):
        self.context['success'] = False
        if self.new_product:
            product = Product()
        elif self.list_product:
            self.context['products'] = Product.objects.filter(user=request.user)
            return render(request, 'pages/product/list.html', self.context)
        else:
            product = get_object_or_404(Product, id=id)
            if product.user == request.user:
                self.context['del'] = True
            self.context['product'] = product
            return render(request, 'pages/product/view.html', self.context)
        return render(request, 'pages/product/create.html', self.context)

    @method_decorator(login_required)
    def post(self, request, id=-1):
        if self.new_product:
            product = Product()
        else:
            product = get_object_or_404(Product, id=id)

        if request.POST.get('buy', None):
            pass
        elif request.POST.get('delete', None):
            if product.user == request.user:
                product.delete()
                return redirect('product_list')
            else:
                raise PermissionDenied
        else:
            form = ProductForm(request.POST)
            if form.is_valid():
                self.context['success'] = True
                product = form.save(commit=False)
                product.user = request.user
                product.save()
        return render(request, 'pages/product/create.html', self.context)


def profile_page(request, id):
    context = {
        'pagename': "Профиль",
        'user': get_object_or_404(User, id=id),
    }
    return render(request, 'pages/profile/profile.html', context)


class ProfileSettingView(View):
    context = {
        'pagename': "Настроки профиля",
    }

    @method_decorator(login_required)
    def get(self, request):
        self.context['name'] = request.user
        self.context['form'] = UserSettings(instance=request.user)
        return render(request, 'pages/profile/profilsetting.html', self.context)

    @method_decorator(login_required)
    def post(self, request):
        form = UserSettings(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
        return redirect(reverse('profile', kwargs={"id": request.user.id}))
