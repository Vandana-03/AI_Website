# Candlelight - Premium Handmade Candles Website

A modern, responsive website for an online candle making business with user authentication, beautiful UI, and animated background effects.

## Features

✨ **Beautiful Design**
- Modern and elegant UI with premium color scheme
- Smooth animations and transitions
- Animated gradient backgrounds
- Responsive design for all devices

🔐 **User Authentication**
- User registration with validation
- Secure login system
- Local storage for user data
- Session management

📱 **Pages**
- **Login Page**: Email and password authentication
- **Registration Page**: New user account creation
- **Landing Page**: Personalized welcome, product showcase, about section

🛍️ **E-commerce Features**
- Product showcase with cards
- Add to cart functionality
- Product pricing display
- Smooth scrolling navigation

## Getting Started

### Installation

1. Clone or download this project to your computer
2. No installation required - it's a pure HTML/CSS/JavaScript project

### Running the Website

**Option 1: Double-click index.html**
- Simply double-click the `index.html` file to open it in your default browser

**Option 2: Use a Local Server (Recommended)**
- Open terminal/command prompt in the project folder
- Run: `python -m http.server 8000` (Python 3)
- Or: `python -m SimpleHTTPServer 8000` (Python 2)
- Visit: `http://localhost:8000`

**Option 3: Use VS Code Live Server**
- Install "Live Server" extension in VS Code
- Right-click on `index.html`
- Select "Open with Live Server"

## Test Credentials

Use these credentials to test the login:
- **Email**: `demo@example.com`
- **Password**: `Demo123`

## Creating a New Account

1. Click "Register here" on the login page
2. Fill in your details:
   - Full Name (minimum 2 characters)
   - Email (valid format required)
   - Password (minimum 6 characters, must include uppercase, lowercase, and number)
   - Confirm Password
3. Check "I agree to the Terms and Conditions"
4. Click "Create Account"

You'll automatically be logged in after registration.

## Password Requirements

- Minimum 6 characters
- At least 1 uppercase letter
- At least 1 lowercase letter
- At least 1 number

Example: `Password123`

## Features Breakdown

### Authentication System
- Email validation
- Password strength validation
- Duplicate email prevention
- Session persistence using localStorage
- Auto-logout option

### Background Effects
- Animated gradients with floating animations
- Shimmer effects
- Responsive to different screen sizes
- Smooth color transitions

### Landing Page Features
- Personalized welcome message
- Navigation bar with logout
- Product showcase (4 sample products)
- Add to cart functionality
- About section
- Smooth scrolling
- Sticky navigation

## File Structure

```
Website/
├── index.html          # Main HTML file with all pages
├── styles.css          # All styling and animations
├── script.js           # JavaScript functionality
└── README.md           # This file
```

## Customization

### Adding Products
Edit the products section in `index.html` to add more candle products.

### Changing Colors
Modify the color variables in `styles.css`:
```css
:root {
    --primary-color: #d4a574;      /* Gold/brown */
    --secondary-color: #8b6f47;    /* Dark brown */
    --dark-color: #2c2416;         /* Very dark brown */
    --light-color: #f5f1e8;        /* Cream */
    --accent-color: #e8c4a0;       /* Light tan */
}
```

### Changing Animations
All animations are defined in `styles.css`. Look for `@keyframes` sections to modify animation behavior.

## Browser Compatibility

- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)
- Mobile browsers

## Data Storage

User data is stored in the browser's localStorage. This means:
- Users created in one session persist across browser sessions
- Data is stored locally on the device
- Clearing browser data will delete user accounts
- This is suitable for demo purposes; for production, use a backend database

## Future Enhancements

- Backend database integration
- Payment gateway integration
- Email verification
- Password reset functionality
- Product reviews and ratings
- User profile management
- Shopping cart system
- Order history
- Admin panel

## Security Note

This is a frontend demo with client-side validation only. For production:
- Implement server-side authentication
- Use HTTPS
- Hash passwords
- Implement proper session management
- Use a secure backend database

## Support

For issues or feature requests, please modify the code as needed for your specific requirements.

---

**Created**: 2026
**Version**: 1.0.0
**License**: Open Source
