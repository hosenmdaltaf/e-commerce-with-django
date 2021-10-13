from django.shortcuts import render,get_object_or_404,redirect,HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import(
    ListView,DetailView,UpdateView,CreateView,DeleteView
) 
from products.models import Product
from django.core.paginator import Paginator

    

def home(request):
    products=Product.objects.all()
    paginator = Paginator( products , 3) # Show 6 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'products/products.html',{'products':page_obj})

# class ProductListView(ListView):
#     model = Product
#     # paginate_by = 10
#     context_object_name = 'products'
#     template_name ='products/products.html'

class CreateProductView(CreateView):
    model = Product
    fields= '__all__'
    context_object_name = 'product_details'
    template_name ='products/productcreate.html'
    success_url = reverse_lazy("products:allproduct")

class UpdateProductView(UpdateView):
    model = Product
    fields= '__all__'
    context_object_name = 'product_details'
    template_name ='products/productupdate.html'
    success_url = reverse_lazy("products:allproduct")

class ProductDetailsView(DetailView):
    model = Product
    context_object_name = 'product_details'
    template_name ='products/productdetails.html'

class DeleteProductView(DeleteView):
    model = Product
    # context_object_name = 'product_details'
    template_name ='products/productdelete.html'
    success_url = reverse_lazy("products:allproduct")

# @login_required(login_url ='/profiles/login/')
def favourite_list(request):
    new = Product.objects.filter(favourites=request.user)
    return render(request,
                  'products/favourites.html',
                  {'new': new})


# @login_required(login_url ='/profiles/login/')
def favourite_add(request, id):
    post = get_object_or_404(Product, id=id)
    if post.favourites.filter(id=request.user.id).exists():
        post.favourites.remove(request.user)
    else:
        post.favourites.add(request.user)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])
