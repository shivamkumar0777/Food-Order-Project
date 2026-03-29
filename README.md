# 🍕 Food Order Project

A Django-based web application for managing online food orders. Built with Django, SQLite, and HTML/CSS templates.

## Features

✨ **Core Features:**

- Browse food items with images, prices, and descriptions
- Add items to shopping cart
- Update cart quantities or remove items
- Secure checkout process
- Order confirmation with success page
- Admin panel for managing food items and orders

## Project Structure

```
foodproject/          # Main Django project
  ├── settings.py     # Project configuration
  ├── urls.py         # Project URL routing
  └── wsgi.py         # WSGI configuration

shop/                 # Main Django app
  ├── models.py       # Database models (Food, Order, Cart)
  ├── views.py        # View logic
  ├── forms.py        # Django forms
  ├── admin.py        # Admin configuration
  └── urls.py         # App URL routing

templates/            # HTML templates
  ├── base.html       # Base template
  ├── home.html       # Homepage
  ├── cart.html       # Shopping cart
  ├── checkout.html   # Checkout form
  └── order_success.html

db.sqlite3            # SQLite database
manage.py             # Django management script
```

## Installation & Setup

### Prerequisites

- Python 3.7+
- pip (Python package manager)

### Steps

1. **Clone the repository:**

   ```bash
   git clone https://github.com/<your-username>/Food-Order-Project.git
   cd "food order project"
   ```

2. **Create and activate virtual environment:**

   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate

   # macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies:**

   ```bash
   pip install django
   ```

4. **Run migrations:**

   ```bash
   python manage.py migrate
   ```

5. **Create superuser (admin):**

   ```bash
   python manage.py createsuperuser
   ```

   - Enter username, email, and password when prompted

6. **Start development server:**

   ```bash
   python manage.py runserver
   ```

7. **Access the application:**
   - Frontend: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
   - Admin Panel: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

## How to Use

### As a Customer

1. Navigate to the homepage
2. Browse available food items
3. Click "Add to Cart" on desired items
4. Click cart icon to view your shopping cart
5. Update quantities or remove items as needed
6. Click "Proceed to Checkout"
7. Fill in delivery details and place order
8. View order confirmation on success page

### As an Admin

1. Log in at `/admin/`
2. Add/edit food items with images, prices, and descriptions
3. View all customer orders
4. Track order status and details

## Technologies Used

- **Backend:** Django 3.x/4.x
- **Database:** SQLite
- **Frontend:** HTML, CSS
- **Package Manager:** pip

## Database Models

- **Food** - Food items (name, price, image, description)
- **Cart** - Shopping cart items (user, food, quantity)
- **Order** - Customer orders (user, items, delivery address, phone)

## Future Enhancements

- User authentication system
- Payment gateway integration
- Order tracking for customers
- Email notifications
- Star ratings and reviews
- Admin dashboard analytics

## License

MIT License - feel free to use this project for educational purposes.

## Author

**Developed by:** Your Name / Your Team
**Last Updated:** March 2026

---

**Questions or Issues?** Feel free to open an issue on GitHub.
