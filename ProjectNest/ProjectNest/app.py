from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient

app = Flask(__name__)

# Define the MongoDB connection
client = MongoClient('mongodb://localhost:27017')
db = client.mydb

# Create a collection named 'mycollection'
collection = db.mycollection

@app.route('/')
def mainpage():
    return render_template('mainpage.html')

@app.route('/home')
def homepage():
    return render_template('home.html')

@app.route('/specialoffers')
def specialoffers():
    return render_template('specialoffers.html')

@app.route('/reservation', methods=['GET', 'POST'])
def reservation():
    if request.method == 'POST':
        # Get the form data
        name = request.form.get('name')
        address = request.form.get('address')
        email = request.form.get('email')
        restaurant = request.form.get('restaurant')
        area = request.form.get('area')
        phone_number = request.form.get('phone_number')
        comment = request.form.get('comment')

        # Create a dictionary to represent the reservation data
        reservation_data = {
            'name': name,
            'address': address,
            'email': email,
            'restaurant': restaurant,
            'area': area,
            'phone_number': phone_number,
            'comment': comment
        }

        # Insert the reservation data into the MongoDB collection
        collection.insert_one(reservation_data)

        # Redirect to a success page or another page as needed
        return redirect(url_for('reservation_success'))

    return render_template('reservation.html')

@app.route('/menu')
def menu():
    return render_template('menu.html')

@app.route('/Contact')
def contact():
    return render_template('contact.html')

@app.route('/reservation_success')
def reservation_success():
    return render_template('Mainpage.html')

if __name__ == '__main__':
    app.run(debug=True)
