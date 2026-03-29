from decimal import Decimal

from django.contrib import messages
from django.db import transaction
from django.shortcuts import get_object_or_404, redirect, render

from .forms import CheckoutForm, FoodForm
from .models import Cart, Food, Order, OrderItem


def cart_summary():
    items = Cart.objects.select_related('food').all()
    total = sum((item.total_price() for item in items), start=Decimal('0.00'))
    cart_count = sum(item.quantity for item in items)
    return items, total, cart_count


def home(request):
    query = request.GET.get('q', '').strip()
    foods = Food.objects.all()

    if query:
        foods = foods.filter(name__icontains=query)

    _, _, cart_count = cart_summary()
    return render(
        request,
        'home.html',
        {
            'foods': foods,
            'query': query,
            'cart_count': cart_count,
        },
    )


def manage_food(request):
    _, _, cart_count = cart_summary()

    if request.method == 'POST':
        form = FoodForm(request.POST)
        if form.is_valid():
            food = form.save()
            messages.success(request, f'{food.name} added to the menu.')
            return redirect('manage_food')
    else:
        form = FoodForm()

    foods = Food.objects.all()
    return render(
        request,
        'manage_food.html',
        {
            'form': form,
            'foods': foods,
            'cart_count': cart_count,
        },
    )


def add_to_cart(request, id):
    if request.method != 'POST':
        return redirect('home')

    food = get_object_or_404(Food, id=id)
    cart_item, created = Cart.objects.get_or_create(food=food)

    if not created:
        cart_item.quantity += 1
        cart_item.save(update_fields=['quantity'])

    messages.success(request, f'{food.name} added to cart.')
    return redirect('home')


def cart(request):
    items, total, cart_count = cart_summary()
    return render(
        request,
        'cart.html',
        {
            'items': items,
            'total': total,
            'cart_count': cart_count,
        },
    )


def update_cart(request, item_id, action):
    if request.method != 'POST':
        return redirect('cart')

    item = get_object_or_404(Cart, id=item_id)

    if action == 'increase':
        item.quantity += 1
        item.save(update_fields=['quantity'])
    elif action == 'decrease':
        if item.quantity > 1:
            item.quantity -= 1
            item.save(update_fields=['quantity'])
        else:
            item.delete()
    elif action == 'remove':
        item.delete()

    return redirect('cart')


def checkout(request):
    items, total, cart_count = cart_summary()

    if not items.exists():
        messages.info(request, 'Your cart is empty. Add some food first.')
        return redirect('home')

    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            with transaction.atomic():
                order = Order.objects.create(
                    customer_name=form.cleaned_data['customer_name'],
                    phone_number=form.cleaned_data['phone_number'],
                    address=form.cleaned_data['address'],
                    total_amount=total,
                )
                OrderItem.objects.bulk_create(
                    [
                        OrderItem(
                            order=order,
                            food_name=item.food.name,
                            quantity=item.quantity,
                            unit_price=item.food.price,
                        )
                        for item in items
                    ]
                )
                items.delete()

            messages.success(request, 'Order placed successfully.')
            return redirect('order_success', order_id=order.id)
    else:
        form = CheckoutForm()

    return render(
        request,
        'checkout.html',
        {
            'form': form,
            'items': items,
            'total': total,
            'cart_count': cart_count,
        },
    )


def order_success(request, order_id):
    order = get_object_or_404(Order.objects.prefetch_related('items'), id=order_id)
    return render(
        request,
        'order_success.html',
        {
            'order': order,
            'cart_count': 0,
        },
    )
