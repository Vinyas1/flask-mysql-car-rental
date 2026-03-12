# 🚗 Car Rental Booking System (Flask + MySQL)

A simple **Car Rental Web Application** built using **Flask, MySQL, HTML, CSS, and JavaScript**.
Users can register, log in, view available cars, and book a car online. Booking details are stored in a **MySQL database**, and confirmation can be sent via **Formspree email integration**.

---

## 📌 Features

* 🔐 User Registration and Login (secure password hashing)
* 🚗 Browse featured cars
* 📅 Car booking with booking date and return date
* 📧 Email confirmation using Formspree
* 💾 Booking data stored in MySQL

---

## 🛠 Tech Stack

**Backend**

* Python
* Flask
* MySQL
* MySQL Connector
* Hashlib (for password hashing)

**Frontend**

* HTML
* CSS
* JavaScript
* LocalStorage

**Other Tools**

* Formspree (email form submission)

---

## 📂 Project Structure

```
https://res.cloudinary.com/dokuv73yo/image/upload/v1773335605/Screenshot_2026-03-12_224229_tufxfa.png
```

---

## ⚙️ Installation

### 1️⃣ Clone the repository

```
git clone https://github.com/Vinyas1/flask-mysql-car-rental.git
cd car-rental-flask
```

---

### 2️⃣ Create Virtual Environment

```
python -m venv venv
```
```
venv\Scripts\activate
```
---

### 3️⃣ Install Dependencies

```
pip install flask mysql-connector-python
```

---

### 4️⃣ Setup MySQL Database

Access the DB code from the "DATABASE.sql" and run the code in MY-sql once

Set your My-sql Username and Password in the app.py 
```

---

### 6️⃣ Run the Application

```bash
python app.py
```

Open browser:

```
http://127.0.0.1:5000
```

---


## 📧 Email Integration

Booking confirmations are sent using **Formspree**.

Go to Formspree and signup and get your formspree-ID 
ex : "https://formspree.io/f/XXXXXXXX

 

