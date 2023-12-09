from models import Driver, CarType, Car, User, Route, Order, DriverRating, AvailabilityCar, DriverCar, Feedback
from dao import DriverDAO, CarTypeDAO, CarDAO, UserDAO, RouteDAO, OrderDAO, DriverRatingDAO, AvailabilityCarDAO, DriverCarDAO, FeedbackDAO


class DriverService:
    @staticmethod
    def create_driver(driver_data):
        return DriverDAO.create_driver(driver_data)

    @staticmethod
    def get_all_drivers():
        return DriverDAO.get_all_drivers()

    @staticmethod
    def get_driver_by_id(driver_id):
        return DriverDAO.get_driver_by_id(driver_id)

    @staticmethod
    def update_driver_by_id(driver_id, driver_data):
        return DriverDAO.update_driver_by_id(driver_id, driver_data)


class CarTypeService:
    @staticmethod
    def create_car_type(car_type_data):
        return CarTypeDAO.create_car_type(car_type_data)

    @staticmethod
    def get_all_car_types():
        return CarTypeDAO.get_all_car_types()

    @staticmethod
    def get_car_type_by_id(car_type_id):
        return CarTypeDAO.get_car_type_by_id(car_type_id)

    @staticmethod
    def update_car_type_by_id(car_type_id, car_type_data):
        return CarTypeDAO.update_car_type_by_id(car_type_id, car_type_data)


class CarService:
    @staticmethod
    def create_car(car_data):
        return CarDAO.create_car(car_data)

    @staticmethod
    def get_all_cars():
        return CarDAO.get_all_cars()

    @staticmethod
    def get_car_by_id(car_id):
        return CarDAO.get_car_by_id(car_id)

    @staticmethod
    def update_car_by_id(car_id, car_data):
        return CarDAO.update_car_by_id(car_id, car_data)


class UserService:
    @staticmethod
    def create_user(user_data):
        return UserDAO.create_user(user_data)

    @staticmethod
    def get_all_users():
        return UserDAO.get_all_users()

    @staticmethod
    def get_user_by_id(user_id):
        return UserDAO.get_user_by_id(user_id)

    @staticmethod
    def update_user_by_id(user_id, user_data):
        return UserDAO.update_user_by_id(user_id, user_data)


class RouteService:
    @staticmethod
    def create_route(route_data):
        return RouteDAO.create_route(route_data)

    @staticmethod
    def get_all_routes():
        return RouteDAO.get_all_routes()

    @staticmethod
    def get_route_by_id(route_id):
        return RouteDAO.get_route_by_id(route_id)

    @staticmethod
    def update_route_by_id(route_id, route_data):
        return RouteDAO.update_route_by_id(route_id, route_data)


class OrderService:
    @staticmethod
    def create_order(order_data):
        return OrderDAO.create_order(order_data)

    @staticmethod
    def get_all_orders():
        return OrderDAO.get_all_orders()

    @staticmethod
    def get_order_by_id(order_id):
        return OrderDAO.get_order_by_id(order_id)

    @staticmethod
    def update_order_by_id(order_id, order_data):
        return OrderDAO.update_order_by_id(order_id, order_data)


class DriverRatingService:
    @staticmethod
    def create_driver_rating(driver_rating_data):
        return DriverRatingDAO.create_driver_rating(driver_rating_data)

    @staticmethod
    def get_all_driver_ratings():
        return DriverRatingDAO.get_all_driver_ratings()

    @staticmethod
    def get_driver_rating_by_id(driver_rating_id):
        return DriverRatingDAO.get_driver_rating_by_id(driver_rating_id)

    @staticmethod
    def update_driver_rating_by_id(driver_rating_id, driver_rating_data):
        return DriverRatingDAO.update_driver_rating_by_id(driver_rating_id, driver_rating_data)


class AvailabilityCarService:
    @staticmethod
    def create_availability_car(availability_car_data):
        return AvailabilityCarDAO.create_availability_car(availability_car_data)

    @staticmethod
    def get_all_availability_cars():
        return AvailabilityCarDAO.get_all_availability_cars()

    @staticmethod
    def get_availability_car_by_id(availability_car_id):
        return AvailabilityCarDAO.get_availability_car_by_id(availability_car_id)

    @staticmethod
    def update_availability_car_by_id(availability_car_id, availability_car_data):
        return AvailabilityCarDAO.update_availability_car_by_id(availability_car_id, availability_car_data)


class DriverCarService:
    @staticmethod
    def create_driver_car(driver_car_data):
        return DriverCarDAO.create_driver_car(driver_car_data)

    @staticmethod
    def get_all_driver_cars():
        return DriverCarDAO.get_all_driver_cars()

    @staticmethod
    def get_driver_has_car_by_id(driver_car_id):
        return DriverCarDAO.get_driver_has_car_by_id(driver_car_id)

    @staticmethod
    def update_driver_car_by_id(driver_car_id, driver_car_data):
        return DriverCarDAO.update_driver_car_by_id(driver_car_id, driver_car_data)


class FeedbackService:
    @staticmethod
    def create_feedback(feedback_data):
        return FeedbackDAO.create_feedback(feedback_data)

    @staticmethod
    def get_all_feedbacks():
        return FeedbackDAO.get_all_feedbacks()

    @staticmethod
    def get_feedbacks_by_id(feedbacks_id):
        return FeedbackDAO.get_feedbacks_by_id(feedbacks_id)

    @staticmethod
    def update_feedback_by_id(feedbacks_id, feedback_data):
        return FeedbackDAO.update_feedback_by_id(feedbacks_id, feedback_data)

