from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
import json
from datetime import datetime
import os

# Get the directory where this file is located
basedir = os.path.abspath(os.path.dirname(__file__))

# Create Flask app with template and static folders
app = Flask(__name__, 
            template_folder=os.path.join(basedir, 'app', 'templates'),
            static_folder=os.path.join(basedir, 'app', 'static'))
app.secret_key = 'candle_website_secret_key_2026'

# Data files path
DATA_DIR = os.path.join(basedir, 'app', 'data')
USERS_FILE = os.path.join(DATA_DIR, 'users.json')
PRODUCTS_FILE = os.path.join(DATA_DIR, 'products.json')
ORDERS_FILE = os.path.join(DATA_DIR, 'orders.json')

# Ensure data directory exists
os.makedirs(DATA_DIR, exist_ok=True)

# Helper functions to read/write JSON files
def load_json(filepath):
    if os.path.exists(filepath):
        with open(filepath, 'r') as f:
            return json.load(f)
    return {}

def save_json(filepath, data):
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=2)

def load_users():
    return load_json(USERS_FILE)

def save_users(users):
    save_json(USERS_FILE, users)

def load_products():
    return load_json(PRODUCTS_FILE)

def load_orders():
    return load_json(ORDERS_FILE)

def save_orders(orders):
    save_json(ORDERS_FILE, orders)

# Initialize products if not exist
def init_products():
    products = load_products()
    if not products:
        products = {
            "luxury": [
                {"id": 1, "name": "Golden Hour", "price": 799, "scent": "Rose + Sandalwood", "benefit": "Luxury Relaxation", "burnTime": "50 hours", "image": "candle1.jpg", "rating": 4.8, "reviews": 45, "inStock": True},
                {"id": 2, "name": "Pearl Essence", "price": 899, "scent": "Jasmine + Musk", "benefit": "Evening Elegance", "burnTime": "55 hours", "image": "candle2.jpg", "rating": 4.7, "reviews": 38, "inStock": True},
            ],
            "scented": [
                {"id": 3, "name": "Forest Fresh", "price": 499, "scent": "Cedarwood + Pine", "benefit": "Energizing", "burnTime": "40 hours", "image": "candle3.jpg", "rating": 4.5, "reviews": 62, "inStock": True},
                {"id": 4, "name": "Vanilla Bliss", "price": 449, "scent": "Vanilla + Amber", "benefit": "Warm Comfort", "burnTime": "45 hours", "image": "candle4.jpg", "rating": 4.6, "reviews": 89, "inStock": True},
            ],
            "relaxing": [
                {"id": 5, "name": "Lavender Dreams", "price": 599, "scent": "Lavender + Chamomile", "benefit": "Deep Sleep", "burnTime": "50 hours", "image": "candle5.jpg", "rating": 4.9, "reviews": 124, "inStock": True},
                {"id": 6, "name": "Zen Mind", "price": 549, "scent": "Eucalyptus + Mint", "benefit": "Mental Clarity", "burnTime": "48 hours", "image": "candle6.jpg", "rating": 4.7, "reviews": 71, "inStock": True},
            ],
            "gifting": [
                {"id": 7, "name": "Celebration Set", "price": 1299, "scent": "Mixed 3-pack", "benefit": "Perfect Gift", "burnTime": "120 hours total", "image": "candle7.jpg", "rating": 4.8, "reviews": 53, "inStock": True},
                {"id": 8, "name": "Love Express", "price": 899, "scent": "Rose + Vanilla", "benefit": "Romance", "burnTime": "50 hours", "image": "candle8.jpg", "rating": 4.6, "reviews": 47, "inStock": True},
            ],
            "customized": [
                {"id": 9, "name": "Custom Creation", "price": 699, "scent": "Your Choice", "benefit": "Personalized", "burnTime": "45 hours", "image": "candle9.jpg", "rating": 4.7, "reviews": 28, "inStock": True},
                {"id": 10, "name": "Name Engraved", "price": 749, "scent": "Premium Blend", "benefit": "Bespoke Gift", "burnTime": "50 hours", "image": "candle10.jpg", "rating": 4.9, "reviews": 35, "inStock": True},
            ]
        }
        save_json(PRODUCTS_FILE, products)
    return products

# Routes
@app.route('/')
def home():
    products = init_products()
    featured = []
    for category in products.values():
        featured.extend(category[:2])
    featured = featured[:4]  # Get first 4 for homepage
    return render_template('index.html', featured_products=featured)

@app.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        users = load_users()
        if email in users and check_password_hash(users[email]['password'], password):
            session['user_email'] = email
            session['user_name'] = users[email]['name']
            return redirect(url_for('home'))
        else:
            return render_template('signin.html', error="Invalid email or password")
    
    return render_template('signin.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        confirm_email = request.form.get('confirm_email')
        birthday = request.form.get('birthday')
        zipcode = request.form.get('zipcode')
        phone = request.form.get('phone')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')
        
        # Validation
        if email != confirm_email:
            return render_template('signup.html', error="Emails do not match")
        if password != confirm_password:
            return render_template('signup.html', error="Passwords do not match")
        if len(phone) != 10 or not phone.isdigit():
            return render_template('signup.html', error="Phone must be 10 digits")
        
        users = load_users()
        if email in users:
            return render_template('signup.html', error="Email already registered")
        
        # Save user
        users[email] = {
            'name': name,
            'email': email,
            'birthday': birthday,
            'zipcode': zipcode,
            'phone': phone,
            'password': generate_password_hash(password),
            'created_at': datetime.now().isoformat()
        }
        save_users(users)
        
        session['user_email'] = email
        session['user_name'] = name
        return redirect(url_for('home'))
    
    return render_template('signup.html')

@app.route('/forgot-password', methods=['GET', 'POST'])
def forgot_password():
    if request.method == 'POST':
        email = request.form.get('email')
        users = load_users()
        if email in users:
            return render_template('forgot_password.html', success=f"Reset link sent to {email}")
        else:
            return render_template('forgot_password.html', error="Email not found")
    return render_template('forgot_password.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('home'))

@app.route('/category/<category>')
def category(category):
    products = init_products()
    category_products = products.get(category, [])
    return render_template('category.html', category=category, products=category_products)

@app.route('/product/<int:product_id>')
def product_detail(product_id):
    products = init_products()
    product = None
    for category_products in products.values():
        for p in category_products:
            if p['id'] == product_id:
                product = p
                break
    if not product:
        return redirect(url_for('home'))
    return render_template('product_detail.html', product=product)

@app.route('/cart')
def cart():
    cart_items = session.get('cart', [])
    products = init_products()
    items_detail = []
    total = 0
    
    for item in cart_items:
        for category_products in products.values():
            for p in category_products:
                if p['id'] == item['id']:
                    item_total = p['price'] * item['qty']
                    items_detail.append({**p, 'qty': item['qty'], 'item_total': item_total})
                    total += item_total
                    break
    
    shipping = 0 if total == 0 else 99
    return render_template('cart.html', items=items_detail, total=total, shipping=shipping)

@app.route('/add-to-cart/<int:product_id>', methods=['POST'])
def add_to_cart(product_id):
    qty = request.form.get('qty', 1, type=int)
    cart = session.get('cart', [])
    
    # Check if product already in cart
    existing = next((item for item in cart if item['id'] == product_id), None)
    if existing:
        existing['qty'] += qty
    else:
        cart.append({'id': product_id, 'qty': qty})
    
    session['cart'] = cart
    return redirect(request.referrer or url_for('home'))

@app.route('/remove-from-cart/<int:product_id>')
def remove_from_cart(product_id):
    cart = session.get('cart', [])
    session['cart'] = [item for item in cart if item['id'] != product_id]
    return redirect(url_for('cart'))

@app.route('/checkout', methods=['GET', 'POST'])
def checkout():
    if not session.get('user_email'):
        return redirect(url_for('signin'))
    
    if request.method == 'POST':
        users = load_users()
        user = users.get(session['user_email'], {})
        payment_method = request.form.get('payment_method', 'cod')
        
        cart = session.get('cart', [])
        products = init_products()
        order_items = []
        total = 0
        
        for item in cart:
            for category_products in products.values():
                for p in category_products:
                    if p['id'] == item['id']:
                        item_total = p['price'] * item['qty']
                        order_items.append({'name': p['name'], 'qty': item['qty'], 'price': p['price']})
                        total += item_total
        
        shipping = 99
        tax = round(total * 0.05, 2)
        grand_total = total + shipping + tax
        
        # Save order
        orders = load_orders()
        order_id = f"ORD{datetime.now().strftime('%Y%m%d%H%M%S')}"
        orders[order_id] = {
            'user_email': session['user_email'],
            'items': order_items,
            'subtotal': total,
            'shipping': shipping,
            'tax': tax,
            'total': grand_total,
            'payment_method': payment_method,
            'status': 'Confirmed' if payment_method == 'cod' else 'Processing',
            'created_at': datetime.now().isoformat()
        }
        save_orders(orders)
        
        session['cart'] = []
        return render_template('order_confirmation.html', order_id=order_id, total=grand_total, payment_method=payment_method)
    
    users = load_users()
    user = users.get(session['user_email'], {})
    return render_template('checkout.html', user=user)

@app.route('/account')
def account():
    if not session.get('user_email'):
        return redirect(url_for('signin'))
    
    users = load_users()
    user = users.get(session['user_email'], {})
    orders = load_orders()
    user_orders = {k: v for k, v in orders.items() if v.get('user_email') == session['user_email']}
    
    return render_template('account.html', user=user, orders=user_orders)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/sustainability')
def sustainability():
    return render_template('sustainability.html')

@app.route('/faq')
def faq():
    return render_template('faq.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        # In real app, send email here
        return render_template('contact.html', success="Thank you! We'll get back to you soon.")
    return render_template('contact.html')

if __name__ == '__main__':
    init_products()
    app.run(debug=True, port=5000)
