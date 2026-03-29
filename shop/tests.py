from decimal import Decimal

from django.test import TestCase
from django.urls import reverse

from .models import Cart, Food, Order


class ShopFlowTests(TestCase):
    def setUp(self):
        self.food = Food.objects.create(
            name='Pizza',
            description='Loaded with cheese and veggies',
            price='299.00',
            image='https://example.com/pizza.jpg',
        )

    def test_home_page_lists_food(self):
        response = self.client.get(reverse('home'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Pizza')

    def test_add_to_cart_increments_quantity(self):
        add_url = reverse('add_to_cart', args=[self.food.id])

        self.client.post(add_url)
        self.client.post(add_url)

        cart_item = Cart.objects.get(food=self.food)
        self.assertEqual(cart_item.quantity, 2)

    def test_manage_food_page_adds_menu_item_without_login(self):
        response = self.client.post(
            reverse('manage_food'),
            data={
                'name': 'Burger',
                'description': 'Crispy patty with fresh lettuce',
                'price': '149.00',
                'image': 'https://example.com/burger.jpg',
            },
        )

        self.assertRedirects(response, reverse('manage_food'))
        self.assertTrue(Food.objects.filter(name='Burger').exists())

    def test_checkout_creates_order_and_clears_cart(self):
        Cart.objects.create(food=self.food, quantity=2)

        response = self.client.post(
            reverse('checkout'),
            data={
                'customer_name': 'Shivam',
                'phone_number': '9876543210',
                'address': 'Food Street, Kolkata',
            },
        )

        order = Order.objects.get()
        self.assertRedirects(response, reverse('order_success', args=[order.id]))
        self.assertEqual(order.total_amount, Decimal('598.00'))
        self.assertEqual(order.items.count(), 1)
        self.assertFalse(Cart.objects.exists())
