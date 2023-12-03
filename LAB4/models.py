from database import db


class Driver(db.Model):
    __tablename__ = 'Drivers'
    id = db.Column(db.Integer, primary_key=True)
    surname = db.Column(db.String(45), nullable=False)
    name = db.Column(db.String(45), nullable=False)
    phone = db.Column(db.String(13), nullable=False)


class CarType(db.Model):
    __tablename__ = 'CarTypes'
    id = db.Column(db.Integer, primary_key=True)
    type_name = db.Column(db.String(45), nullable=False)
    description = db.Column(db.String(110))


class Car(db.Model):
    __tablename__ = 'Cars'
    id = db.Column(db.Integer, primary_key=True)
    model = db.Column(db.String(45), nullable=False)
    license_plate = db.Column(db.String(45), nullable=False)
    CarTypes_id = db.Column(db.Integer, db.ForeignKey('CarTypes.id'), nullable=False)
    car_type = db.relationship('CarType', backref=db.backref('cars', lazy=True))


class User(db.Model):
    __tablename__ = 'Users'
    id = db.Column(db.Integer, primary_key=True)
    surname = db.Column(db.String(45), nullable=False)
    name = db.Column(db.String(45), nullable=False)
    phone = db.Column(db.String(13), nullable=False)


class Route(db.Model):
    __tablename__ = 'Routes'
    id = db.Column(db.Integer, primary_key=True)
    start_location = db.Column(db.String(45), nullable=False)
    end_location = db.Column(db.String(45), nullable=False)
    distance = db.Column(db.String(45))


class Order(db.Model):
    __tablename__ = 'Orders'
    id = db.Column(db.Integer, primary_key=True)
    pickup_time = db.Column(db.String(45), nullable=False)
    status = db.Column(db.String(45), nullable=False)
    Users_id = db.Column(db.Integer, db.ForeignKey('Users.id'), nullable=False)
    Routes_id = db.Column(db.Integer, db.ForeignKey('Routes.id'), nullable=False)
    Cars_id = db.Column(db.Integer, db.ForeignKey('Cars.id'), nullable=False)
    Cars_CarTypes_id = db.Column(db.Integer, db.ForeignKey('CarTypes.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('orders', lazy=True))
    route = db.relationship('Route', backref=db.backref('orders', lazy=True))
    car = db.relationship('Car', backref=db.backref('orders', lazy=True))
    car_type = db.relationship('CarType', backref=db.backref('orders', lazy=True))


class DriverRating(db.Model):
    __tablename__ = 'Driver_Ratings'
    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.DECIMAL(2), nullable=False)
    comment = db.Column(db.String(200))
    Drivers_id = db.Column(db.Integer, db.ForeignKey('Drivers.id'), nullable=False)
    driver = db.relationship('Driver', backref=db.backref('ratings', lazy=True))


class AvailabilityCar(db.Model):
    __tablename__ = 'Availability_Cars'
    id = db.Column(db.Integer, primary_key=True)
    start_time = db.Column(db.DECIMAL(2))
    end_time = db.Column(db.String(2))
    available = db.Column(db.String(30), nullable=False)


class DriverCar(db.Model):
    __tablename__ = 'Drivers_has_Cars'
    Drivers_id = db.Column(db.Integer, db.ForeignKey('Drivers.id'), primary_key=True, nullable=False)
    Cars_id = db.Column(db.Integer, db.ForeignKey('Cars.id'), primary_key=True, nullable=False)
    driver = db.relationship('Driver', backref=db.backref('driver_cars', lazy=True))
    car = db.relationship('Car', backref=db.backref('driver_cars', lazy=True))


class Feedback(db.Model):
    __tablename__ = 'Feedback'
    id = db.Column(db.Integer, primary_key=True)
    comments = db.Column(db.String(100), nullable=False)
    Drivers_id = db.Column(db.Integer, db.ForeignKey('Drivers.id'), nullable=False)
    Users_id = db.Column(db.Integer, db.ForeignKey('Users.id'), nullable=False)
    driver = db.relationship('Driver', backref=db.backref('feedbacks', lazy=True))
    user = db.relationship('User', backref=db.backref('feedbacks', lazy=True))