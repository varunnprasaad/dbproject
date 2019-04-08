from sqlalchemy import Column, Integer, String, Date, Text

from app import db


class Base(db.Model):
    __abstract__ = True

    def __repr__(self):
        items = ['%s=%r' % (col.name, getattr(self, col.name))
                 for col in self.__table__.columns]
        return "<%s.%s[object at %x] {%s}>" % (self.__class__.__module__,
                                               self.__class__.__name__,
                                               id(self), ','.join(items))

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class Car(Base):
    # def __init__(self, id, category_id, brand, model, mileage, color, production_year):
    #     self.id = id
    #     self.category_id = category_id
    #     self.brand = brand
    #     self.model = model
    #     self.mileage = mileage
    #     self.color = color
    #     self.production_year = production_year

    __tablename__ = 'car'
    id = Column(Integer, primary_key=True)
    category_id = Column(Integer)
    brand = Column(String)
    model = Column(String)
    mileage = Column(String)
    color = Column(String)
    production_year = Column(Integer)


class Category(Base):

    __tablename__ = 'category'
    id = Column(Integer, primary_key=True)
    name = Column(String)


class Customer(Base):
    # def __init__(self, customer_id, first_name):
    #     self.customer_id = customer_id
    #     self.first_name = first_name

    __tablename__ = 'customer'
    customer_id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    birth_date = Column(Date)
    driver_license_number = Column(String)


class Address(Base):
    # def __init__(self, id, street, city, state, zipcode, country):
    #     self.id = id
    #     self.street = street
    #     self.city = city
    #     self.state = state
    #     self.zipcode = zipcode
    #     self.country = country

    __tablename__ = 'address'
    id = Column(Integer, primary_key=True)
    street = Column(String(45))
    city = Column(String(45))
    state = Column(String(45))
    zipcode = Column(Integer)
    country = Column(String(20))


class Location(Base):
    # def __init__(self, id, name, address):
    #     self.id = id
    #     self.name = name
    #     self.address = address
    __tablename__ = 'location'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    address = Column(Integer)


class Insurance(Base):
    # def __init__(self, name, description, policy):
    #     self.id = id
    #     self.name = name
    #     self.description = description
    #     self.policy = policy

    __tablename__ = 'insurance'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(Text)
    policy = Column(Integer)


class RentalInsurance(Base):
    # def __init__(self, rental_id, insurance_id):
    #     self.id = id
    #     self.rental_id = rental_id
    #     self.insurance_id = insurance_id

    __tablename__ = 'rental_insurance'
    id = Column(Integer, primary_key=True)
    rental_id = Column(Integer)
    insurance_id = Column(Integer)


class Rental(Base):
    # def __init__(self, customer_id, car_id, pickup_location, dropoff_location, start_date, end_date, remarks):
    #     self.id = id
    #     self.customer_id = customer_id
    #     self.car_id = car_id
    #     self.pickup_location = pickup_location
    #     self.dropoff_location = dropoff_location
    #     self.start_date = start_date
    #     self.end_date = end_date
    #     self.remarks = remarks

    __tablename__ = 'rental'
    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer)
    car_id = Column(Integer)
    pickup_location = Column(Integer)
    dropoff_location = Column(Integer)
    start_date = Column(Date)
    end_date = Column(Date)
    remarks = Column(Text)
