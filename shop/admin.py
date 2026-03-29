from django.contrib import admin

from .models import Cart, Food, Order, OrderItem


@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    search_fields = ('name', 'description')


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('food', 'quantity', 'added_at')
    list_select_related = ('food',)


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    can_delete = False
    readonly_fields = ('food_name', 'quantity', 'unit_price')


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer_name', 'phone_number', 'total_amount', 'created_at')
    search_fields = ('customer_name', 'phone_number', 'address')
    inlines = [OrderItemInline]
