from pos.models import *
import graphene
from graphene_django.types import DjangoObjectType
from graphene import ObjectType, String,Field

class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = ['name']


class SubCategoryType(DjangoObjectType):
    class Meta:
        model = SubCategory
        fields = "__all__"


class ProductType(DjangoObjectType):
    image_url=graphene.String()
    class Meta:
        model = Product
        fields = "__all__"
    
    def resolve_image_url(self,args):
        if self.image:
            return self.image.url 
        ""



class RestaurantType(DjangoObjectType):
    class Meta:
        model = Restaurant
        fields = "__all__"

class UserType(DjangoObjectType):
   

    class Meta:
        model = User
        fields = ['name', 'phone', 'email', 'user_type', 'resturant']


class CustomerType(DjangoObjectType):
    class Meta:
        model = Customer
        fields = "__all__"


class OrderType(DjangoObjectType):
    class Meta:
        model = Order
        fields = "__all__"


class OrderItemType(DjangoObjectType):
    class Meta:
        model = OrderItem
        fields = "__all__"