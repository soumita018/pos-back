from django.contrib import admin
from pos.models import *
from django.utils.safestring import mark_safe
# Register your models here.

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']

class OrderItem(admin.ModelAdmin):
    readonly_fields = ('order_total',)
    list_display = ['customer','status',]
    list_editable = [ 'status',]
    inlines = [OrderItemInline]

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price','stock', 'available','featured',mark_safe('thumb')]
    
admin.site.register(User)
admin.site.register(Customer)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Product,ProductAdmin)
admin.site.register(Restaurant)
# admin.site.register(OrderItemInline)
admin.site.register(Order,OrderItem)




# extra
# class OrderItemInline(admin.TabularInline):
#     model = OrderItem
#     raw_id_fields = ['product']


# class OrderAdmin(admin.ModelAdmin):
#     def get_billing_address(self, obj):
#         return "{address_type}\n{line1}\n{line2}\n{city}\n{state}, {postal}\n{country}".format(
#             address_type = obj.billing_address.address_type,
#             line1 = obj.billing_address.address_line_1,
#             line2 = obj.billing_address.address_line_2 or "",
#             city = obj.billing_address.city,
#             state = obj.billing_address.state,
#             postal = obj.billing_address.postal_code,
#             country = obj.billing_address.country
#         )
#     get_billing_address.allow_tags = True
#     get_billing_address.short_description = 'Billing Address display'

#     def get_shipping_address(self, obj):
#         return "{address_type}\n{line1}\n{line2}\n{city}\n{state}, {postal}\n{country}".format(
#             address_type = obj.shipping_address.address_type,
#             line1 = obj.shipping_address.address_line_1,
#             line2 = obj.shipping_address.address_line_2 or "",
#             city = obj.shipping_address.city,
#             state = obj.shipping_address.state,
#             postal = obj.shipping_address.postal_code,
#             country = obj.shipping_address.country
#         )
#     get_shipping_address.allow_tags = True
#     get_shipping_address.short_description = 'Shipping Address display'

#     readonly_fields = ('ordered_id','id','order_total','payment','final_price','total_savings','coupon','created','shipping_total','get_billing_address','get_shipping_address','billing_profile')
#     list_display = ['ordered_id','status','final_price','payment_status','payment','created']
#     list_filter = [ 'created', 'status']
#     list_filter = ('status', 'payment_status','payment','created','final_price','total_savings','shipping_total','order_total')
#     list_editable = ['payment_status', 'status',]

#     fieldsets = (
#         (None, {
#             'fields': ('ordered_id', 'id', 'coupon','billing_profile','created')
#         }),
#         ('All Prices', {
#             'fields': ('order_total','total_savings','shipping_total','final_price')
#         }),
#         ('All Status', {
#             'fields': ('status', 'payment_status','payment')
#         }),
#         ('All Addresses', {
#             'fields': ('shipping_address','get_shipping_address', 'billing_address','get_billing_address')
#         }),
#     )
   

#     inlines = [OrderItemInline]

# # @admin.register(OrderAdmin)



# admin.site.register(Order, OrderAdmin)
