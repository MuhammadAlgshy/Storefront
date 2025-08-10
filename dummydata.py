from store.models import *
from django.contrib.auth import get_user_model
from decimal import Decimal
from uuid import uuid4
import random
from datetime import date

User = get_user_model()

# --- Optional: FULL CLEAR ---
Review.objects.all().delete()
CartItem.objects.all().delete()
Cart.objects.all().delete()
OrderItem.objects.all().delete()
Order.objects.all().delete()
Address.objects.all().delete()
Customer.objects.all().delete()
Product.objects.all().delete()
Collection.objects.all().delete()
Promotion.objects.all().delete()
# Delete only our dummy users (not all)
User.objects.filter(username__in=["john", "jane", "alex"]).delete()

# --- Create Users ---
users = [
    User.objects.create_user(username="john", password="test123", first_name="John", last_name="Doe", email="john@example.com"),
    User.objects.create_user(username="jane", password="test123", first_name="Jane", last_name="Smith", email="jane@example.com"),
    User.objects.create_user(username="alex", password="test123", first_name="Alex", last_name="Brown", email="alex@example.com")
]

# --- Create Customers linked to Users ---
customers = []
memberships = [Customer.MEMBERSHIP_GOLD, Customer.MEMBERSHIP_SILVER, Customer.MEMBERSHIP_BRONZE]
birth_dates = ["1990-05-12", "1985-07-20", "1995-03-15"]

for user, membership, birth_date in zip(users, memberships, birth_dates):
    customer, created = Customer.objects.get_or_create(
        user=user,
        defaults={
            "phone": "123456789",
            "birth_date": birth_date,
            "membership": membership,
        }
    )
    customers.append(customer)

# --- Promotions ---
promos = [
    Promotion.objects.create(description="Summer Sale - 10% off", discount=10.0),
    Promotion.objects.create(description="Black Friday - 20% off", discount=20.0),
    Promotion.objects.create(description="Clearance - 50% off", discount=50.0)
]

# --- Collections ---
collections = [
    Collection.objects.create(title="Electronics"),
    Collection.objects.create(title="Home Appliances"),
    Collection.objects.create(title="Books")
]

# --- Products ---
product_data = [
    ("Wireless Mouse", "wireless-mouse", "Ergonomic wireless mouse with long battery life", "25.99", 50, collections[0], [promos[0]]),
    ("Gaming Keyboard", "gaming-keyboard", "Mechanical RGB gaming keyboard", "89.99", 30, collections[0], [promos[1]]),
    ("Bluetooth Headphones", "bluetooth-headphones", "Noise cancelling over-ear headphones", "120.00", 20, collections[0], [promos[2]]),

    ("Air Fryer", "air-fryer", "Oil-free air fryer for healthy cooking", "75.50", 40, collections[1], [promos[1]]),
    ("Robot Vacuum", "robot-vacuum", "Smart robot vacuum cleaner with scheduling", "250.00", 15, collections[1], [promos[0]]),
    ("Espresso Machine", "espresso-machine", "High-pressure coffee maker", "150.00", 10, collections[1], [promos[2]]),

    ("Python for Beginners", "python-for-beginners", "Learn Python programming from scratch", "19.99", 100, collections[2], [promos[0]]),
    ("Django Unleashed", "django-unleashed", "Comprehensive guide to Django framework", "39.99", 60, collections[2], [promos[1]]),
    ("Clean Code", "clean-code", "A Handbook of Agile Software Craftsmanship", "29.99", 80, collections[2], [promos[2]]),
]

products = []
for title, slug, desc, price, inv, col, promo_list in product_data:
    p = Product.objects.create(
        title=title,
        slug=slug,
        description=desc,
        unit_price=Decimal(price),
        inventory=inv,
        collection=col
    )
    p.promotions.add(*promo_list)
    products.append(p)

# Assign featured products
for col in collections:
    col.featured_product = random.choice(products)
    col.save()

# --- Orders & Order Items ---
for cust in customers:
    for _ in range(2):
        order = Order.objects.create(customer=cust, payment_status=random.choice([Order.PAYMENT_COMPLETED, Order.PAYMENT_PENDING]))
        for _ in range(2):
            prod = random.choice(products)
            OrderItem.objects.create(order=order, product=prod, quantity=random.randint(1, 5), unit_price=prod.unit_price)

# --- Addresses ---
Address.objects.create(street="123 Main St", city="Springfield", customer=customers[0])
Address.objects.create(street="456 Oak Ave", city="Rivertown", customer=customers[1])
Address.objects.create(street="789 Pine Rd", city="Lakeside", customer=customers[2])

# --- Carts & Cart Items ---
for cust in customers:
    cart = Cart.objects.create(id=uuid4())
    used_products = set()
    for _ in range(2):
        # avoid duplicate products per cart
        prod = random.choice(products)
        while prod.id in used_products:
            prod = random.choice(products)
        used_products.add(prod.id)
        CartItem.objects.create(cart=cart, product=prod, quantity=random.randint(1, 3))

# --- Reviews ---
for prod in products:
    for cust in customers:
        Review.objects.create(product=prod, name=f"{cust.user.first_name} {cust.user.last_name}", description=f"Loved the {prod.title}! Works as expected.", date=date.today())

print("Dummy data created successfully!")
