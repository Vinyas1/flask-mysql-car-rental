from flask import Flask, render_template, request, redirect, url_for, session, flash
import mysql.connector
import hashlib

app = Flask(__name__)
app.secret_key = '07a57389f43b5279aeb6aa30abc68b38'

# MySQL Connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",   #DATABASE USERNMAE (MYSQL)
    password="password",  #DATABASE PASSWORD (MYSQL)
    database="flask_auth"
)
cursor = conn.cursor(dictionary=True)

@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        hashed_pw = hashlib.sha256(password.encode()).hexdigest()

        cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
        existing_user = cursor.fetchone()

        if existing_user:
            flash('Email already exists. Try logging in.', 'warning')
            return redirect(url_for('register'))

        cursor.execute("INSERT INTO users (username, email, password) VALUES (%s, %s, %s)",
                       (username, email, hashed_pw))
        conn.commit()
        flash('Registered successfully! Please log in.', 'success')
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password_input = request.form['password']
        hashed_input = hashlib.sha256(password_input.encode()).hexdigest()

        cursor.execute("SELECT * FROM users WHERE email = %s AND password = %s",
                       (email, hashed_input))
        user = cursor.fetchone()

        if user:
            session['loggedin'] = True
            session['username'] = user['username']
            return redirect(url_for('dashboard'))
        else:
            flash('Incorrect email or password.', 'danger')
    return render_template('login.html')


@app.route('/book')
def book():
    car_id = request.args.get('car_id')
    return render_template('book.html', car_id=car_id)

@app.route('/bookf')
def bookf():
    car_id = request.args.get('car_id')
    return render_template('bookf.html', car_id=car_id)




@app.route('/dashboard')
def dashboard():
    if 'loggedin' in session:
        return render_template('dashboard.html', username=session['username'])
    return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))



@app.route('/submit_booking', methods=['POST'])
def submit_booking():
    carid = request.form['carid']
    carname = request.form['carname']
    name = request.form['name']
    age = request.form['age']
    booking_date = request.form['booking_date']
    return_date = request.form['return_date']
    amount = request.form['amount']
    email = request.form['email']
    text=request.form['text']

    # Check if user has already booked any car
    cursor.execute("SELECT * FROM bookings WHERE name = %s", (name,))
    existing_booking = cursor.fetchone()

    if existing_booking:
        flash("You have already booked a car!")
        return redirect('/')
    
    
    cursor.execute("SELECT * FROM bookings WHERE carid = %s AND booking_date = %s", (carid, booking_date))
    existing_booking = cursor.fetchone()
    
    if existing_booking:
        flash("This car is already booked on the selected date!")
        return redirect('/')


    
    cursor.execute("""
        INSERT INTO bookings (carid, carname, name, age, booking_date, return_date, amount, email,text)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s,%s)
    """, (carid, carname, name, age, booking_date, return_date, amount, email,text))
    conn.commit()

    flash("Booking successful!")
    return redirect('/')



if __name__ == '__main__':
    app.run(debug=True)
