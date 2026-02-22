# ✨ Candles - Premium Handmade Candles Website

A full-stack Python Flask web application for selling handmade, therapeutic candles in India. Features authentication, product catalog with 5 categories, shopping cart, checkout with COD/Online payment options, and user account management.

## Project Structure

```
Website/
├── app.py                      # Main Flask application
├── requirements.txt            # Python dependencies
├── README.md                   # Project documentation
├── app/
│   ├── templates/              # HTML templates
│   │   ├── base.html          # Base template with header/footer
│   │   ├── index.html         # Homepage
│   │   ├── signin.html        # Sign in page
│   │   ├── signup.html        # Sign up page
│   │   ├── forgot_password.html
│   │   ├── category.html      # Product listing pages
│   │   ├── product_detail.html
│   │   ├── cart.html
│   │   ├── checkout.html
│   │   ├── order_confirmation.html
│   │   ├── account.html       # User dashboard
│   │   ├── about.html
│   │   ├── sustainability.html
│   │   ├── faq.html
│   │   └── contact.html
│   ├── static/
│   │   ├── css/
│   │   │   └── style.css      # Main styling
│   │   ├── js/
│   │   │   └── script.js      # Client-side JavaScript
│   │   └── images/            # Placeholder for product images
│   └── data/
│       ├── users.json         # User data (auto-created)
│       ├── products.json      # Product catalog (auto-created)
│       └── orders.json        # Order history (auto-created)
```

## Features

### Authentication
- ✓ User registration with email, phone, postal code validation
- ✓ Secure login with password hashing
- ✓ Forgot password recovery
- ✓ Session management

### Product Management
- ✓ 5 Product Categories: Luxury, Scented, Relaxing, Gifting, Customized
- ✓ Product filtering by benefit and price range
- ✓ Product sorting options
- ✓ Detailed product pages with reviews

### Shopping Features
- ✓ Add to cart functionality
- ✓ Cart management (view, update, remove)
- ✓ Shipping cost calculator based on postal code
- ✓ Product recommendations

### Checkout & Payment
- ✓ COD (Cash on Delivery) - Primary option
- ✓ Online Payment option
- ✓ Order confirmation with order ID
- ✓ Order tracking history

### User Account
- ✓ My Account dashboard
- ✓ Order history with status
- ✓ Saved address management
- ✓ Account settings

### Additional Pages
- ✓ About Us - Brand story and mission
- ✓ Sustainability - Eco-friendly practices
- ✓ FAQ - Common questions answered
- ✓ Contact - Contact form and support info

## Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 2: Run the Application
```bash
python app.py
```

The application will start on `http://localhost:5000`

### Step 3: Access the Website
Open your browser and navigate to:
- **Homepage:** http://localhost:5000/
- **Sign Up:** http://localhost:5000/signup
- **Sign In:** http://localhost:5000/signin

## Demo Credentials (for testing)

Once you sign up, use your credentials to log in. The application uses JSON files to store data locally.

## Key Pages & Routes

| Page | Route | Description |
|------|-------|-------------|
| Homepage | `/` | Featured products and intro |
| Sign In | `/signin` | User login |
| Sign Up | `/signup` | New user registration |
| Forgot Password | `/forgot-password` | Password recovery |
| Luxury Candles | `/category/luxury` | Premium candle collection |
| Scented Candles | `/category/scented` | Fragrance-focused collection |
| Relaxing Candles | `/category/relaxing` | Therapeutic collection |
| Gifting Candles | `/category/gifting` | Gift sets |
| Customized Candles | `/category/customized` | Personalized orders |
| Product Detail | `/product/<id>` | Full product information |
| Cart | `/cart` | Shopping cart |
| Checkout | `/checkout` | Order confirmation |
| Account | `/account` | User dashboard |
| About | `/about` | Brand story |
| Sustainability | `/sustainability` | Eco-friendly practices |
| FAQ | `/faq` | Common questions |
| Contact | `/contact` | Contact form |

## Technology Stack

- **Backend:** Python Flask
- **Frontend:** HTML5, CSS3, Vanilla JavaScript
- **Database:** JSON files (Local storage)
- **Security:** Werkzeug password hashing

## Features Implemented

### Phase 1: Authentication ✓
- Complete signup flow with validation
- Secure login
- Password reset functionality
- Session management

### Phase 2: Core Site Structure ✓
- Homepage with header, banner, featured products
- Navigation menu with all categories
- Responsive footer with links

### Phase 3: Product Management ✓
- 5 Category pages with filtering
- Product details page
- Product recommendations
- Rating and reviews display

### Phase 4: E-Commerce ✓
- Shopping cart with add/remove/update
- Checkout with multiple payment options
- COD as primary payment method
- Order confirmation with tracking ID

### Phase 5: User Management ✓
- Account dashboard
- Order history
- Address management
- User settings

### Phase 6: Supporting Pages ✓
- About Us page
- Sustainability commitment
- Comprehensive FAQ
- Contact form

## Data Storage

Data is stored locally in JSON format:

- **users.json** - Stores user accounts with hashed passwords
- **products.json** - Product catalog with pricing and details
- **orders.json** - Order history with status tracking

*Note: For production, replace JSON with a proper database like PostgreSQL or MongoDB*

## Security Features

- Password hashing using Werkzeug
- Session-based authentication
- Form validation (email, phone format)
- CSRF protection ready
- Input sanitization

## Customization Guide

### Update Brand Name
Edit `app/templates/base.html` - Change logo text from "✨ Candles" to your brand name

### Add Products
Edit `app.py` - Modify the `init_products()` function to add more candles

### Change Colors
Edit `app/static/css/style.css` - Update color variables:
- Primary: `#8B7355` (warm brown)
- Secondary: `#7A9E7E` (soft green)
- Background: `#F5F1E8` (cream)

### Add Product Images
Place images in `app/static/images/` and update image URLs in templates

## Future Enhancements

- [ ] Real database integration (PostgreSQL)
- [ ] Email notifications
- [ ] Payment gateway integration
- [ ] Admin panel
- [ ] Subscription box feature
- [ ] Wishlist functionality
- [ ] Product reviews submission
- [ ] Analytics dashboard
- [ ] Search functionality
- [ ] Multiple language support

## Troubleshooting

### Port Already in Use
```bash
# Change port in app.py
if __name__ == '__main__':
    app.run(debug=True, port=5001)  # Change to 5001
```

### Import Errors
```bash
# Reinstall dependencies
pip install --upgrade -r requirements.txt
```

### Static Files Not Loading
Ensure `app/static/` directory exists with `css/` and `js/` subdirectories

## Performance Notes

- JSON file storage is suitable for <1000 products and <10000 orders
- For scaling, migrate to:
  - **Database:** PostgreSQL, MySQL, or MongoDB
  - **Cache:** Redis for session management
  - **CDN:** CloudFront or Cloudflare for static assets

## Support & Contact

- Email: hello@candlebliss.com
- Phone: +91 98765 43210
- Website: www.candlebliss.com

## License

This project is built for Candles. All rights reserved.

---

**Built with ❤️ using Python Flask | Handmade in India 🇮🇳**
