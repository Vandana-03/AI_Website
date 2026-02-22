/* ==================== UTILITY JAVASCRIPT ==================== */

document.addEventListener('DOMContentLoaded', function() {
    // Initialize cart count on page load
    updateCartCount();
});

// Update cart count in header
function updateCartCount() {
    const cart = JSON.parse(localStorage.getItem('cart') || '[]');
    const count = cart.reduce((total, item) => total + item.qty, 0);
    
    const cartIcon = document.querySelector('.header-icons .icon:last-child');
    if (cartIcon) {
        if (count > 0) {
            cartIcon.innerHTML = `🛒 Cart (${count})`;
        } else {
            cartIcon.innerHTML = '🛒 Cart';
        }
    }
}

// Toggle password visibility
function togglePassword(inputId = 'password') {
    const input = document.getElementById(inputId);
    const btn = document.querySelector('.show-pwd');
    if (input.type === 'password') {
        input.type = 'text';
        if (btn) btn.textContent = 'HIDE';
    } else {
        input.type = 'password';
        if (btn) btn.textContent = 'SHOW';
    }
}

// Form validation
function validateForm() {
    const form = event.target;
    
    // Check email match for signup
    const email = form.querySelector('input[name="email"]');
    const confirmEmail = form.querySelector('input[name="confirm_email"]');
    
    if (email && confirmEmail && email.value !== confirmEmail.value) {
        alert('Emails do not match!');
        return false;
    }
    
    // Check password match
    const password = form.querySelector('input[name="password"]');
    const confirmPassword = form.querySelector('input[name="confirm_password"]');
    
    if (password && confirmPassword && password.value !== confirmPassword.value) {
        alert('Passwords do not match!');
        return false;
    }
    
    // Check phone format
    const phone = form.querySelector('input[name="phone"]');
    if (phone && phone.value && (phone.value.length !== 10 || isNaN(phone.value))) {
        alert('Phone must be 10 digits!');
        return false;
    }
    
    return true;
}

// Filter products by benefit
function filterByBenefit(benefit) {
    const cards = document.querySelectorAll('.product-card');
    cards.forEach(card => {
        const badge = card.querySelector('.benefit-badge');
        if (badge && badge.textContent.includes(benefit)) {
            card.style.display = 'block';
        } else if (benefit) {
            card.style.display = 'none';
        }
    });
}

// Sort products
function sortProducts(sortType) {
    const grid = document.querySelector('.products-grid');
    const cards = Array.from(document.querySelectorAll('.product-card'));
    
    switch(sortType) {
        case 'price-low':
            cards.sort((a, b) => {
                const priceA = parseInt(a.querySelector('.price').textContent);
                const priceB = parseInt(b.querySelector('.price').textContent);
                return priceA - priceB;
            });
            break;
        case 'price-high':
            cards.sort((a, b) => {
                const priceA = parseInt(a.querySelector('.price').textContent);
                const priceB = parseInt(b.querySelector('.price').textContent);
                return priceB - priceA;
            });
            break;
        case 'rating':
            cards.sort((a, b) => {
                const ratingA = parseFloat(a.querySelector('.rating').textContent);
                const ratingB = parseFloat(b.querySelector('.rating').textContent);
                return ratingB - ratingA;
            });
            break;
    }
    
    // Re-append sorted cards
    cards.forEach(card => grid.appendChild(card));
}

// Calculate shipping cost based on postal code
function calculateShipping(zipcode) {
    // Basic example - in real app, use actual postal codes
    if (zipcode) {
        return 99; // Fixed shipping for demo
    }
    return 0;
}

// Format price in Indian Rupees
function formatPrice(amount) {
    return '₹' + amount.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
}

// Add smooth scroll behavior
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({ behavior: 'smooth' });
        }
    });
});

// Handle quantity updates
function updateQuantity(productId, change) {
    const quantityInput = document.getElementById(`qty-${productId}`);
    if (quantityInput) {
        let newValue = parseInt(quantityInput.value) + change;
        if (newValue >= 1) {
            quantityInput.value = newValue;
        }
    }
}

// Validate email format
function validateEmail(email) {
    const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return re.test(email);
}

// Show success message
function showSuccess(message) {
    const alert = document.createElement('div');
    alert.className = 'alert alert-success';
    alert.textContent = message;
    alert.style.position = 'fixed';
    alert.style.top = '100px';
    alert.style.right = '20px';
    alert.style.zIndex = '1000';
    document.body.appendChild(alert);
    
    setTimeout(() => alert.remove(), 3000);
}

// Show error message
function showError(message) {
    const alert = document.createElement('div');
    alert.className = 'alert alert-error';
    alert.textContent = message;
    alert.style.position = 'fixed';
    alert.style.top = '100px';
    alert.style.right = '20px';
    alert.style.zIndex = '1000';
    document.body.appendChild(alert);
    
    setTimeout(() => alert.remove(), 3000);
}

// Initialize tooltips
function initTooltips() {
    const tooltips = document.querySelectorAll('[data-tooltip]');
    tooltips.forEach(elem => {
        elem.addEventListener('hover', function() {
            const tooltip = document.createElement('div');
            tooltip.className = 'tooltip';
            tooltip.textContent = this.dataset.tooltip;
            this.appendChild(tooltip);
        });
    });
}

// Check form inputs in real-time
function setupFormValidation(form) {
    const inputs = form.querySelectorAll('input, textarea');
    inputs.forEach(input => {
        input.addEventListener('blur', function() {
            validateInput(this);
        });
    });
}

function validateInput(input) {
    const type = input.type;
    const value = input.value.trim();
    
    if (!value && input.required) {
        input.style.borderColor = '#f44336';
        return false;
    }
    
    if (type === 'email' && value && !validateEmail(value)) {
        input.style.borderColor = '#f44336';
        return false;
    }
    
    input.style.borderColor = '#ddd';
    return true;
}

// Fade in animation for page load
window.addEventListener('load', function() {
    document.body.style.opacity = '1';
});

console.log('Candles website loaded successfully! ✨');
