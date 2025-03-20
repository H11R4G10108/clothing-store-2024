Clothing Store Website

A fully functional e-commerce platform for a clothing store, allowing users to browse products, manage carts, and complete purchases.

🎯 Project Goal

Develop a responsive and feature-rich online clothing store with essential e-commerce functionalities.

🚀 Features

✅ Product List – Browse all available clothing items.

✅ Product Detail – View product images, price, and descriptions.

✅ Product Search – Search for products using keywords.

✅ Shopping Cart – Add, remove, and update cart items.

✅ Checkout Process – Securely place an order.

✅ Order History – View past purchases.

✅ Shipping Address Management – Save and update delivery addresses.

✅ Change Password – Update account credentials securely.

✅ Login & Logout – User authentication with JWT.

✅ Register – Create a new account.

🛠️ Tech Stack

Frontend
ReactJS -
React Router -
Tailwind CSS

Backend
Django REST Framework -
MySQL -
JWT Authentication

📌 API Endpoints

🔐 Authentication


POST	/api/token/	Get authentication token

POST	/api/token/refresh/	Refresh JWT token

POST	/api/register/	Register new user

POST	/api/change-password/	Change user password

🛍️ Product & Category


GET	/api/product/	Retrieve all products

GET	/api/categoryview/	Get product categories

📦 Address Management


GET	/api/address/	List all addresses

POST	/api/create-address/	Add a new address

PATCH	/api/mark_default_address/<int:pk>/	Set default address

GET	/api/user/<int:pk>/address	Retrieve user’s address

🛒 Order Management


GET	/api/order/	Retrieve all orders

GET	/api/user/<int:pk>/order	Get user's orders

GET	/api/order/<int:pk>/detail	Get order details

POST	/api/orderdetail/	Retrieve specific order info

DELETE	/api/cancel-order/<int:pk>/	Cancel an order

