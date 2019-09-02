from django import forms
from .models import Category, SubCategory, Product, Restaurant, User, Customer, Order, OrderItem


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']


class SubCategoryForm(forms.ModelForm):
    class Meta:
        model = SubCategory
        fields = ['name', 'cat_name']


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'image', 'slug', 'available', 'featured', 'stock', 'updated_at', 'cat_name', 'sub_cat_name']


class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = ['name', 'address', 'product']


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'phone', 'email', 'user_type', 'resturant']


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'phone']

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['order_total', 'customer', 'resturant']


class OrderItemForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = ['price', 'quantity', 'order', 'product']

