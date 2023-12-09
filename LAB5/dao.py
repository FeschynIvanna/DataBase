# dao.py
from database import db
from models import Driver, CarType, Car, User, Route, Order, DriverRating, AvailabilityCar, DriverCar, Feedback


class DriverDAO:
    @staticmethod
    def get_all_drivers():
        return Driver.query.all()

    @staticmethod
    def get_driver_by_id(driver_id):
        return Driver.query.get(driver_id)

    @staticmethod
    def create_driver(driver_data):
        new_driver = Driver(**driver_data)
        db.session.add(new_driver)
        db.session.commit()
        return new_driver

    @staticmethod
    def update_driver_by_id(driver_id, driver_data):
        driver = Driver.query.get(driver_id)
        if driver:
            driver.name = driver_data.get('name', driver.name)
            driver.surname = driver_data.get('surname', driver.surname)
            driver.phone = driver_data.get('phone', driver.phone)

            db.session.commit()
            return driver
        return None

    @staticmethod
    def delete_driver_by_id(driver_id):
        driver = Driver.query.get(driver_id)
        if driver:
            db.session.delete(driver)
            db.session.commit()
            return True
        return False


class CarTypeDAO:
    @staticmethod
    def get_all_car_types():
        return CarType.query.all()

    @staticmethod
    def get_car_type_by_id(car_type_id):
        return CarType.query.get(car_type_id)

    @staticmethod
    def create_car_type(car_type_data):
        new_car_type = CarType(**car_type_data)
        db.session.add(new_car_type)
        db.session.commit()
        return new_car_type

    @staticmethod
    def update_car_type_by_id(car_type_id, car_type_data):
        car_type = CarType.query.get(car_type_id)
        if car_type:
            car_type.description = car_type_data.get('description', car_type.description)
            car_type.type_name = car_type_data.get('type_name', car_type.type_name)

            db.session.commit()
            return car_type
        return None

    @staticmethod
    def delete_car_type_by_id(car_type_id):
        car_type = CarType.query.get(car_type_id)
        if car_type:
            db.session.delete(car_type)
            db.session.commit()
            return True
        return False


class CarDAO:
    @staticmethod
    def get_all_cars():
        return Car.query.all()

    @staticmethod
    def get_car_by_id(car_id):
        return Car.query.get(car_id)

    @staticmethod
    def create_car(car_data):
        new_car = Car(**car_data)
        db.session.add(new_car)
        db.session.commit()
        return new_car

    @staticmethod
    def update_car_by_id(car_id, car_data):
        car = Car.query.get(car_id)
        if car:
            car.CarTypes_id = car_data.get('CarTypes_id', car.CarTypes_id)
            car.license_plate = car_data.get('license_plate', car.license_plate)
            car.model = car_data.get('model', car.model)

            db.session.commit()
            return car
        return None

    @staticmethod
    def delete_car_by_id(car_id):
        car = Car.query.get(car_id)
        if car:
            db.session.delete(car)
            db.session.commit()
            return True
        return False


class UserDAO:
    @staticmethod
    def get_all_users():
        return User.query.all()

    @staticmethod
    def get_user_by_id(user_id):
        return User.query.get(user_id)

    @staticmethod
    def create_user(user_data):
        new_user = User(**user_data)
        db.session.add(new_user)
        db.session.commit()
        return new_user

    @staticmethod
    def update_user_by_id(user_id, user_data):
        user = User.query.get(user_id)
        if user:
            user.surname = user_data.get('surname', user.surname)
            user.name = user_data.get('name', user.name)
            user.phone = user_data.get('phone', user.phone)

            db.session.commit()
            return user
        return None

    @staticmethod
    def delete_user_by_id(user_id):
        user = User.query.get(user_id)
        if user:
            db.session.delete(user)
            db.session.commit()
            return True
        return False


class RouteDAO:
    @staticmethod
    def get_all_routes():
        return Route.query.all()

    @staticmethod
    def get_route_by_id(route_id):
        return Route.query.get(route_id)

    @staticmethod
    def create_route(route_data):
        new_route = Route(**route_data)
        db.session.add(new_route)
        db.session.commit()
        return new_route

    @staticmethod
    def update_route_by_id(route_id, route_data):
        route = Route.query.get(route_id)
        if route:
            route.distance = route_data.get('distance', route.distance)
            route.end_location = route_data.get('end_location', route.end_location)
            route.start_location = route_data.get('start_location', route.start_location)

            db.session.commit()
            return route
        return None

    @staticmethod
    def delete_route_by_id(route_id):
        route = Route.query.get(route_id)
        if route:
            db.session.delete(route)
            db.session.commit()
            return True
        return False


class OrderDAO:
    @staticmethod
    def get_all_orders():
        return Order.query.all()

    @staticmethod
    def get_order_by_id(order_id):
        return Order.query.get(order_id)

    @staticmethod
    def create_order(order_data):
        new_order = Order(**order_data)
        db.session.add(new_order)
        db.session.commit()
        return new_order

    @staticmethod
    def update_order_by_id(order_id, order_data):
        order = Order.query.get(order_id)
        if order:
            order.pickup_time = order_data.get('pickup_time', order.pickup_time)
            order.status = order_data.get('status', order.status)

            db.session.commit()
            return order
        return None

    @staticmethod
    def delete_order_by_id(order_id):
        order = Order.query.get(order_id)
        if order:
            db.session.delete(order)
            db.session.commit()
            return True
        return False


class DriverRatingDAO:
    @staticmethod
    def get_all_driver_ratings():
        return DriverRating.query.all()

    @staticmethod
    def get_driver_rating_by_id(driver_rating_id):
        return DriverRating.query.get(driver_rating_id)

    @staticmethod
    def create_driver_rating(driver_rating_data):
        new_driver_rating = DriverRating(**driver_rating_data)
        db.session.add(new_driver_rating)
        db.session.commit()
        return new_driver_rating

    @staticmethod
    def update_driver_rating_by_id(driver_rating_id, driver_rating_data):
        driver_rating = DriverRating.query.get(driver_rating_id)
        if driver_rating:
            driver_rating.Drivers_id = driver_rating_data.get('Drivers_id', driver_rating.Drivers_id)
            driver_rating.comment = driver_rating_data.get('comment', driver_rating.comment)
            driver_rating.rating = driver_rating_data.get('rating', driver_rating.rating)

            db.session.commit()
            return driver_rating
        return None

    @staticmethod
    def delete_driver_rating_by_id(driver_rating_id):
        driver_rating = DriverRating.query.get(driver_rating_id)
        if driver_rating:
            db.session.delete(driver_rating)
            db.session.commit()
            return True
        return False


class AvailabilityCarDAO:
    @staticmethod
    def get_all_availability_cars():
        return AvailabilityCar.query.all()

    @staticmethod
    def get_availability_car_by_id(availability_car_id):
        return AvailabilityCar.query.get(availability_car_id)

    @staticmethod
    def create_availability_car(availability_car_data):
        new_availability_car = AvailabilityCar(**availability_car_data)
        db.session.add(new_availability_car)
        db.session.commit()
        return new_availability_car

    @staticmethod
    def update_availability_car_by_id(availability_car_id, availability_car_data):
        availability_car = AvailabilityCar.query.get(availability_car_id)
        if availability_car:
            availability_car.available = availability_car_data.get('available', availability_car.available)
            availability_car.end_time = availability_car_data.get('end_time', availability_car.end_time)
            availability_car.start_time = availability_car_data.get('start_time', availability_car.start_time)

            db.session.commit()
            return availability_car
        return None

    @staticmethod
    def delete_availability_car_by_id(availability_car_id):
        availability_car = AvailabilityCar.query.get(availability_car_id)
        if availability_car:
            db.session.delete(availability_car)
            db.session.commit()
            return True
        return False


class DriverCarDAO:
    @staticmethod
    def get_all_driver_cars():
        return DriverCar.query.all()

    @staticmethod
    def get_driver_has_car_by_id(driver_has_car_id):
        return DriverCar.query.get(driver_has_car_id)

    @staticmethod
    def create_driver_car(driver_car_data):
        new_driver_car = AvailabilityCar(**driver_car_data)
        db.session.add(new_driver_car)
        db.session.commit()
        return new_driver_car

    @staticmethod
    def update_driver_car_by_id(driver_car_id, driver_car_data):
        driver_car = DriverCar.query.get(driver_car_id)
        if driver_car:
            driver_car.Drivers_id = driver_car_data.get('Drivers_id', driver_car.Drivers_id)
            driver_car.Cars_id = driver_car_data.get('Cars_id', driver_car.Cars_id)

            db.session.commit()
            return driver_car
        return None

    @staticmethod
    def delete_driver_car_by_id(driver_car_id):
        driver_car = DriverCar.query.get(driver_car_id)
        if driver_car:
            db.session.delete(driver_car)
            db.session.commit()
            return True
        return False


class FeedbackDAO:
    @staticmethod
    def get_all_feedbacks():
        return Feedback.query.all()

    @staticmethod
    def get_feedbacks_by_id(feedbacks_id):
        return Feedback.query.get(feedbacks_id)

    @staticmethod
    def create_feedback(feedback_data):
        new_feedback = Feedback(**feedback_data)
        db.session.add(new_feedback)
        db.session.commit()
        return new_feedback

    @staticmethod
    def update_feedback_by_id(feedbacks_id, feedback_data):
        feedback = Feedback.query.get(feedbacks_id)
        if feedback:
            feedback.name = feedback_data.get('name', feedback.name)
            feedback.surname = feedback_data.get('surname', feedback.surname)
            feedback.phone = feedback_data.get('phone', feedback.phone)

            db.session.commit()
            return feedback
        return None

    @staticmethod
    def delete_feedback_by_id(feedbacks_id):
        feedback = Feedback.query.get(feedbacks_id)
        if feedback:
            db.session.delete(feedback)
            db.session.commit()
            return True
        return False

