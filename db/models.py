from sqlalchemy import Column, Integer, String, Date, Text

from app import db


class Car(db.Model):
    __tablename__ = 'car'
    id = Column(Integer, primary_key=True)
    category_id = Column(Integer)
    brand = Column(String)
    model = Column(String)
    mileage = Column(String)
    color = Column(String)
    production_year = Column(Integer)


class Category(db.Model):
    __tablename__ = 'category'
    id = Column(Integer, primary_key=True)
    name = Column(String)


class Customer(db.Model):
    __tablename__ = 'customer'
    customer_id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    birth_date = Column(Date)
    driver_license_number = Column(String)


class Address(db.Model):
    def __init__(self, id, street, city, state, zipcode, country):
        self.id = id
        self.street = street
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.country = country

    __tablename__ = 'address'
    id = Column(Integer, primary_key=True)
    street = Column(String(45))
    city = Column(String(45))
    state = Column(String(45))
    zipcode = Column(Integer)
    country = Column(String(20))


class Location(db.Model):
    __tablename__ = 'location'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    address = Column(Integer)


class Insurance(db.Model):
    __tablename__ = 'insurance'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(Text)
    policy = Column(Integer)


class RentalInsurance(db.Model):
    __tablename__ = 'rental_insurance'
    id = Column(Integer, primary_key=True)
    rental_id = Column(Integer)
    insurance_id = Column(Integer)


class Rental(db.Model):
    __tablename__ = 'rental'
    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer)
    car_id = Column(Integer)
    pickup_location = Column(Integer)
    dropoff_location = Column(Integer)
    start_date = Column(Date)
    end_date = Column(Date)
    remarks = Column(Text)
