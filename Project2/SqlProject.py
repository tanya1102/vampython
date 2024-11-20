import mysql.connector
import random
from datetime import datetime, timedelta

# Connect to the MySQL database
def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="12345678",  
        database="railway_system"
    )

# Add dummy data for trains
def add_train():
    db = connect_db()
    cursor = db.cursor()

    train_names = ['Express 101', 'Fast Track', 'Super Express', 'Shatabdi', 'Vande Bharat']
    sources = ['Delhi', 'Mumbai', 'Chennai', 'Kolkata', 'Bangalore']
    destinations = ['Lucknow', 'Goa', 'Hyderabad', 'Jaipur', 'Pune']
    departure_time = (datetime.now() + timedelta(hours=random.randint(1, 6))).strftime('%H:%M:%S')

    train_name = random.choice(train_names)
    source = random.choice(sources)
    destination = random.choice(destinations)

    cursor.execute("""
        INSERT INTO trains (train_name, source, destination, departure_time)
        VALUES (%s, %s, %s, %s)
    """, (train_name, source, destination, departure_time))

    db.commit()
    print(f"Train '{train_name}' from {source} to {destination} added successfully.")
    db.close()

# Add dummy data for passengers
def add_passenger():
    db = connect_db()
    cursor = db.cursor()

    names = ['John Doe', 'Jane Smith', 'Robert Johnson', 'Emily Davis', 'Michael Brown']
    ages = random.randint(18, 60)
    genders = ['Male', 'Female']
    name = random.choice(names)
    gender = random.choice(genders)

    cursor.execute("""
        INSERT INTO passengers (name, age, gender)
        VALUES (%s, %s, %s)
    """, (name, ages, gender))

    db.commit()
    print(f"Passenger '{name}', Age {ages}, Gender {gender} added successfully.")
    db.close()

# Book a ticket for a passenger
def book_ticket():
    db = connect_db()
    cursor = db.cursor()

    passenger_id = random.randint(1, 5)  # Automatically selecting a passenger ID
    train_id = random.randint(1, 5)  # Automatically selecting a train ID

    booking_date = datetime.now().date()

    cursor.execute("""
        INSERT INTO bookings (passenger_id, train_id, booking_date)
        VALUES (%s, %s, %s)
    """, (passenger_id, train_id, booking_date))

    db.commit()
    print(f"Ticket booked for Passenger ID {passenger_id} on Train ID {train_id} for {booking_date}.")
    db.close()

# Display all bookings
def display_bookings():
    db = connect_db()
    cursor = db.cursor()

    cursor.execute("""
        SELECT b.booking_id, p.name, t.train_name, t.source, t.destination, b.booking_date
        FROM bookings b
        JOIN passengers p ON b.passenger_id = p.passenger_id
        JOIN trains t ON b.train_id = t.train_id
    """)

    bookings = cursor.fetchall()
    print("\nBooking ID | Passenger Name | Train Name | Source | Destination | Date")
    print("-" * 70)

    for booking in bookings:
        print(f"{booking[0]} | {booking[1]} | {booking[2]} | {booking[3]} | {booking[4]} | {booking[5]}")

    db.close()

# Main Menu for Railway Management System
def main():
    while True:
        print("\nRailway Management System")
        print("1. Add a new train")
        print("2. Add a new passenger")
        print("3. Book a ticket")
        print("4. Display all bookings")
        print("5. Exit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            add_train()
        elif choice == "2":
            add_passenger()
        elif choice == "3":
            book_ticket()
        elif choice == "4":
            display_bookings()
        elif choice == "5":
            print("Exiting the system...")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
