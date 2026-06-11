# 🍕 Food Delivery App

A Full-Stack Food Delivery Web Application built using **FastAPI**, **HTML**, **CSS**, and **JavaScript**. The application allows users to browse food items, manage a shopping cart, and place food orders through a user-friendly interface.

---

## 📌 Project Overview

This project simulates a real-world food ordering platform where customers can:

* Browse available menu items
* Search and filter food items
* Sort menu items by price or category
* Add items to a shopping cart
* View cart total
* Place orders
* Manage menu items through REST APIs

The backend is developed using FastAPI, while the frontend is built using HTML, CSS, and JavaScript.

---

## 🚀 Features

### Menu Management

* View all menu items
* View a specific menu item
* Add new menu items
* Update menu item details
* Delete menu items

### Search & Filtering

* Search menu items by keyword
* Filter menu items by category
* Filter by price range
* Filter by availability

### Sorting & Pagination

* Sort items by:

  * Price
  * Name
  * Category
* Ascending and descending order
* Pagination support

### Cart Management

* Add items to cart
* Remove items from cart
* View cart details
* Calculate total bill

### Order Management

* Place food orders
* Checkout cart
* View all orders
* Generate order summary

### API Documentation

* Interactive Swagger UI documentation
* Automatic request/response validation

---

## 🛠️ Technology Stack

### Backend

* Python
* FastAPI
* Pydantic
* Uvicorn

### Frontend

* HTML5
* CSS3
* JavaScript (Fetch API)

### Tools

* VS Code
* Git
* GitHub

---

## 📂 Project Structure

```text
FoodDeliveryApp/
│
├── main.py
├── index.html
├── style.css
├── script.js
├── README.md
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/food-delivery-app.git

cd food-delivery-app
```

### 2️⃣ Install Dependencies

```bash
pip install fastapi uvicorn pydantic
```

### 3️⃣ Run Backend Server

```bash
uvicorn main:app --reload
```

Backend URL:

```text
http://127.0.0.1:8000
```

### 4️⃣ Open Swagger Documentation

```text
http://127.0.0.1:8000/docs
```

### 5️⃣ Run Frontend

Open a new terminal:

```bash
python -m http.server 5500
```

Frontend URL:

```text
http://localhost:5500
```

---

## 📡 API Endpoints

### Home

| Method | Endpoint | Description |
| ------ | -------- | ----------- |
| GET    | /        | Home Page   |

---

### Menu APIs

| Method | Endpoint        | Description         |
| ------ | --------------- | ------------------- |
| GET    | /menu           | Get all menu items  |
| GET    | /menu/{item_id} | Get menu item by ID |
| POST   | /menu           | Add new menu item   |
| PUT    | /menu/{item_id} | Update menu item    |
| DELETE | /menu/{item_id} | Delete menu item    |

---

### Search & Filter APIs

| Method | Endpoint     | Description                           |
| ------ | ------------ | ------------------------------------- |
| GET    | /menu/search | Search menu items                     |
| GET    | /menu/filter | Filter menu items                     |
| GET    | /menu/sort   | Sort menu items                       |
| GET    | /menu/page   | Paginate menu items                   |
| GET    | /menu/browse | Combined search, sort, and pagination |

---

### Order APIs

| Method | Endpoint | Description    |
| ------ | -------- | -------------- |
| POST   | /orders  | Place an order |
| GET    | /orders  | Get all orders |

---

### Cart APIs

| Method | Endpoint        | Description           |
| ------ | --------------- | --------------------- |
| POST   | /cart/add       | Add item to cart      |
| GET    | /cart           | View cart             |
| DELETE | /cart/{item_id} | Remove item from cart |
| POST   | /cart/checkout  | Checkout cart         |

---

## 📋 Sample Workflow

1. User opens the application.
2. Menu items are loaded from the FastAPI backend.
3. User adds food items to the cart.
4. Cart total is calculated automatically.
5. User enters delivery information.
6. User clicks "Place Order".
7. Order is stored in the backend.
8. Order details can be viewed using the Orders API.

---

## 🎯 Learning Outcomes

Through this project, I gained practical experience in:

* FastAPI development
* REST API design
* CRUD operations
* Frontend-backend integration
* JSON request and response handling
* API testing using Swagger UI
* CORS configuration
* Client-server architecture
* JavaScript Fetch API
* Error handling and validation

---

## 🔮 Future Enhancements

* Database integration using PostgreSQL or MySQL
* User Authentication and Authorization
* Admin Dashboard
* Payment Gateway Integration
* Order Tracking System
* Email Notifications
* Cloud Deployment
* React Frontend Implementation
* Docker Containerization

---

## 👩‍💻 Author

**Hasini Oruganti**

Aspiring Software Developer | AI & Full Stack Enthusiast

---

## 📄 License

This project is developed for educational, learning, and portfolio purposes.
