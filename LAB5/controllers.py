from flask import Flask
from flask import jsonify
from flask import request
from database import db # Додайте цей імпорт
from models import Driver, CarType, Car, User, Route, Order, DriverRating, AvailabilityCar, DriverCar, Feedback

from dao import (
    DriverDAO, CarTypeDAO, CarDAO, UserDAO, RouteDAO, OrderDAO,
    DriverRatingDAO, AvailabilityCarDAO, DriverCarDAO, FeedbackDAO
)

from schema import (
    DriverSchema, CarTypeSchema, CarSchema, UserSchema, RouteSchema, OrderSchema, DriverRatingSchema,
    AvailabilityCarSchema, DriverCarSchema, FeedbackSchema
)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Ivanna2223@localhost/Laba1'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


driver_schema = DriverSchema()
car_type_schema = CarTypeSchema()
car_schema = CarSchema()
user_schema = UserSchema()
route_schema = RouteSchema()
order_schema = OrderSchema()
driver_rating_schema = DriverRatingSchema()
availability_car_schema = AvailabilityCarSchema()
driver_car_schema = DriverCarSchema()
feedback_schema = FeedbackSchema()


@app.route('/drivers', methods=['GET'])
def get_all_drivers():
    drivers = DriverDAO.get_all_drivers()
    return jsonify(driver_schema.dump(drivers, many=True))


@app.route('/drivers/<int:driver_id>', methods=['GET'])
def get_driver_by_id(driver_id):
    driver = DriverDAO.get_driver_by_id(driver_id)
    if driver:
        return jsonify(driver_schema.dump(driver))
    return jsonify({'message': 'Driver not found'}), 404



@app.route('/drivers', methods=['POST'])
def create_driver():
    try:
        # Отримайте дані від клієнта у форматі JSON
        driver_data = request.get_json()

        # Створіть нового водія та додайте його до бази даних
        new_driver = DriverDAO.create_driver(driver_data)

        # Поверніть створеного водія у відповідь
        return jsonify(driver_schema.dump(new_driver)), 201
    except Exception as e:
        # Обробте помилку, якщо вона виникне
        return jsonify({'error': str(e)}), 400



def update_driver(driver_id):
    try:
        print(f'Received PUT request for driver ID: {driver_id}')
        driver_data = request.get_json()
        print(f'Received data: {driver_data}')

        db.init_app(app)

        updated_driver = DriverDAO.update_driver_by_id(driver_id, driver_data)

        if updated_driver:
            return jsonify(driver_schema.dump(updated_driver))
        return jsonify({'message': f'Driver with ID {driver_id} not found'}), 404
    except Exception as e:
        print(f'Error: {e}')
        return jsonify({'error': str(e)}), 400

@app.route('/drivers/<int:driver_id>', methods=['DELETE'])
def delete_driver(driver_id):
    success = DriverDAO.delete_driver_by_id(driver_id)
    if success:
        return jsonify({'message': f'Driver with ID {driver_id} deleted successfully'})
    return jsonify({'message': f'Driver with ID {driver_id} not found'}), 404



@app.route('/cars_type_types', methods=['GET'])
def get_all_car_types():
    car_types = CarTypeDAO.get_all_car_types()
    return jsonify(car_type_schema.dump(car_types, many=True))


@app.route('/cars', methods=['GET'])
def get_all_cars():
    cars = CarDAO.get_all_cars()
    return jsonify(car_schema.dump(cars, many=True))


@app.route('/users', methods=['GET'])
def get_all_users():
    users = UserDAO.get_all_users()
    return jsonify(user_schema.dump(users, many=True))


@app.route('/routes', methods=['GET'])
def get_all_routes():
    routes = RouteDAO.get_all_routes()
    return jsonify(route_schema.dump(routes, many=True))


@app.route('/orders', methods=['GET'])
def get_all_orders():
    orders = OrderDAO.get_all_orders()
    return jsonify(order_schema.dump(orders, many=True))


@app.route('/driver_ratings', methods=['GET'])
def get_all_driver_ratings():
    driver_ratings = DriverRatingDAO.get_all_driver_ratings()
    return jsonify(driver_rating_schema.dump(driver_ratings, many=True))


@app.route('/availability_cars', methods=['GET'])
def get_all_availability_cars():
    availability_cars = AvailabilityCarDAO.get_all_availability_cars()
    return jsonify(availability_car_schema.dump(availability_cars, many=True))


@app.route('/driver_has_cars', methods=['GET'])
def get_all_driver_cars():
    driver_cars = DriverCarDAO.get_all_driver_cars()
    return jsonify(driver_car_schema.dump(driver_cars, many=True))


@app.route('/feedbacks', methods=['GET'])
def get_all_feedbacks():
    feedbacks = FeedbackDAO.get_all_feedbacks()
    return jsonify(feedback_schema.dump(feedbacks, many=True))


# Новий маршрут для отримання інформації про автомобілі разом із типами
@app.route('/cars_with_types', methods=['GET'])
def get_cars_with_types():
    cars_with_types = db.session.query(Car, CarType).join(CarType).all()
    result = [
        {
            'car_id': car.id,
            'model': car.model,
            'license_plate': car.license_plate,
            'car_type': {
                'id': car_type.id,
                'type_name': car_type.type_name,
                'description': car_type.description
            }
        }
        for car, car_type in cars_with_types
    ]
    return jsonify(result)


# Новий маршрут для отримання інформації про замовлення разом із даними про користувачів, маршрути та автомобілі
@app.route('/orders_with_details', methods=['GET'])
def get_orders_with_details():
    orders_with_details = db.session.query(Order, User, Route, Car).join(User).join(Route).join(Car).all()
    result = [
        {
            'order_id': order.id,
            'pickup_time': order.pickup_time,
            'status': order.status,
            'user': {
                'id': user.id,
                'surname': user.surname,
                'name': user.name,
                'phone': user.phone
            },
            'route': {
                'id': route.id,
                'start_location': route.start_location,
                'end_location': route.end_location,
                'distance': route.distance
            },
            'car': {
                'id': car.id,
                'model': car.model,
                'license_plate': car.license_plate
            }
        }
        for order, user, route, car in orders_with_details
    ]
    return jsonify(result)


# ... інші імпорти ...

@app.route('/cars_type_types/<int:car_type_id>', methods=['GET'])
def get_car_type_by_id(car_type_id):
    car_type = CarTypeDAO.get_car_type_by_id(car_type_id)
    if car_type:
        return jsonify(car_type_schema.dump(car_type))
    return jsonify({'message': 'Car type not found'}), 404


@app.route('/cars/<int:car_id>', methods=['GET'])
def get_car_by_id(car_id):
    car = CarDAO.get_car_by_id(car_id)
    if car:
        return jsonify(car_schema.dump(car))
    return jsonify({'message': 'Car not found'}), 404


@app.route('/users/<int:user_id>', methods=['GET'])
def get_user_by_id(user_id):
    user = UserDAO.get_user_by_id(user_id)
    if user:
        return jsonify(user_schema.dump(user))
    return jsonify({'message': 'User not found'}), 404


@app.route('/routes/<int:route_id>', methods=['GET'])
def get_route_by_id(route_id):
    route = RouteDAO.get_route_by_id(route_id)
    if route:
        return jsonify(route_schema.dump(route))
    return jsonify({'message': 'Route not found'}), 404


@app.route('/orders/<int:order_id>', methods=['GET'])
def get_order_by_id(order_id):
    order = OrderDAO.get_order_by_id(order_id)
    if order:
        return jsonify(order_schema.dump(order))
    return jsonify({'message': 'Order not found'}), 404


@app.route('/driver_ratings/<int:driver_rating_id>', methods=['GET'])
def get_driver_rating_by_id(driver_rating_id):
    driver_rating = DriverRatingDAO.get_driver_rating_by_id(driver_rating_id)
    if driver_rating:
        return jsonify(driver_rating_schema.dump(driver_rating))
    return jsonify({'message': 'Driver rating not found'}), 404


@app.route('/availability_cars/<int:availability_car_id>', methods=['GET'])
def get_availability_car_by_id(availability_car_id):
    availability_car = AvailabilityCarDAO.get_availability_car_by_id(availability_car_id)
    if availability_car:
        return jsonify(availability_car_schema.dump(availability_car))
    return jsonify({'message': 'Availability car not found'}), 404


@app.route('/driver_has_cars/<int:driver_has_car_id>', methods=['GET'])
def get_driver_has_car_by_id(driver_has_car_id):
    driver_has_car = DriverCarDAO.get_driver_has_car_by_id(driver_has_car_id)
    if driver_has_car:
        return jsonify(driver_car_schema.dump(driver_has_car))
    return jsonify({'message': 'Driver has car not found'}), 404


@app.route('/feedbacks/<int:feedbacks_id>', methods=['GET'])
def get_feedbacks_by_id(feedbacks_id):
    feedback = FeedbackDAO.get_feedbacks_by_id(feedbacks_id)
    if feedback:
        return jsonify(feedback_schema.dump(feedback))
    return jsonify({'message': 'Feedbacks not found'}), 404


@app.route('/cars_type_types', methods=['POST'])
def create_car_type():
    try:
        car_type_data = request.get_json()
        new_car_type = CarTypeDAO.create_car_type(car_type_data)
        return jsonify(car_type_schema.dump(new_car_type)), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400


@app.route('/cars', methods=['POST'])
def create_car():
    try:
        car_data = request.get_json()
        new_car = CarDAO.create_car(car_data)
        return jsonify(car_schema.dump(new_car)), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400


@app.route('/users', methods=['POST'])
def create_user():
    try:
        user_data = request.get_json()
        new_user = UserDAO.create_user(user_data)
        return jsonify(user_schema.dump(new_user)), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400


@app.route('/routes', methods=['POST'])
def create_route():
    try:
        route_data = request.get_json()
        new_route = RouteDAO.create_route(route_data)
        return jsonify(route_schema.dump(new_route)), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400


@app.route('/orders', methods=['POST'])
def create_order():
    try:
        order_data = request.get_json()
        new_order = OrderDAO.create_order(order_data)
        return jsonify(order_schema.dump(new_order)), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400


@app.route('/driver_ratings', methods=['POST'])
def create_driver_rating():
    try:
        driver_rating_data = request.get_json()
        new_driver_rating = DriverRatingDAO.create_driver_rating(driver_rating_data)
        return jsonify(driver_rating_schema.dump(new_driver_rating)), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400


@app.route('/availability_cars', methods=['POST'])
def create_availability_car():
    try:
        availability_car_data = request.get_json()
        new_availability_car = AvailabilityCarDAO.create_availability_car(availability_car_data)
        return jsonify(availability_car_schema.dump(new_availability_car)), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400


@app.route('/driver_has_cars', methods=['POST'])
def create_driver_car():
    try:
        driver_car_data = request.get_json()
        new_driver_car = DriverCarDAO.create_driver_car(driver_car_data)
        return jsonify(driver_car_schema.dump(new_driver_car)), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400


@app.route('/feedbacks', methods=['POST'])
def create_feedback():
    try:
        feedback_data = request.get_json()
        new_feedback = FeedbackDAO.create_feedback(feedback_data)
        return jsonify(feedback_schema.dump(new_feedback)), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400


def update_car_type(car_type_id):
    try:
        print(f'Received PUT request for car_type ID: {car_type_id}')
        car_type_data = request.get_json()
        print(f'Received data: {car_type_data}')

        db.init_app(app)

        updated_car_type = CarTypeDAO.update_car_type_by_id(car_type_id, car_type_data)

        if updated_car_type:
            return jsonify(car_type_schema.dump(updated_car_type))
        return jsonify({'message': f'Car_type with ID {car_type_id} not found'}), 404
    except Exception as e:
        print(f'Error: {e}')
        return jsonify({'error': str(e)}), 400


@app.route('/cars_type_types/<int:car_type_id>', methods=['DELETE'])
def delete_car_type(car_type_id):
    success = CarTypeDAO.delete_car_type_by_id(car_type_id)
    if success:
        return jsonify({'message': f'Car type with ID {car_type_id} deleted successfully'})
    return jsonify({'message': f'Car type with ID {car_type_id} not found'}), 404


def update_car(car_id):
    try:
        print(f'Received PUT request for car ID: {car_id}')
        car_data = request.get_json()
        print(f'Received data: {car_data}')

        db.init_app(app)

        updated_car = CarDAO.update_car_by_id(car_id, car_data)

        if updated_car:
            return jsonify(car_schema.dump(updated_car))
        return jsonify({'message': f'Car with ID {car_id} not found'}), 404
    except Exception as e:
        print(f'Error: {e}')
        return jsonify({'error': str(e)}), 400


@app.route('/cars/<int:car_id>', methods=['DELETE'])
def delete_car(car_id):
    success = CarDAO.delete_car_by_id(car_id)
    if success:
        return jsonify({'message': f'Car with ID {car_id} deleted successfully'})
    return jsonify({'message': f'Car with ID {car_id} not found'}), 404


def update_user(user_id):
    try:
        print(f'Received PUT request for user ID: {user_id}')
        user_data = request.get_json()
        print(f'Received data: {user_data}')

        db.init_app(app)

        updated_user = UserDAO.update_user_by_id(user_id, user_data)

        if updated_user:
            return jsonify(user_schema.dump(updated_user))
        return jsonify({'message': f'User with ID {user_id} not found'}), 404
    except Exception as e:
        print(f'Error: {e}')
        return jsonify({'error': str(e)}), 400


@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    success = UserDAO.delete_user_by_id(user_id)
    if success:
        return jsonify({'message': f'User with ID {user_id} deleted successfully'})
    return jsonify({'message': f'User with ID {user_id} not found'}), 404


def update_route(route_id):
    try:
        print(f'Received PUT request for route ID: {route_id}')
        route_data = request.get_json()
        print(f'Received data: {route_data}')

        db.init_app(app)

        updated_route = RouteDAO.update_route_by_id(route_id, route_data)

        if updated_route:
            return jsonify(route_schema.dump(updated_route))
        return jsonify({'message': f'Route with ID {route_id} not found'}), 404
    except Exception as e:
        print(f'Error: {e}')
        return jsonify({'error': str(e)}), 400


@app.route('/routes/<int:route_id>', methods=['DELETE'])
def delete_route(route_id):
    success = RouteDAO.delete_route_by_id(route_id)
    if success:
        return jsonify({'message': f'Route with ID {route_id} deleted successfully'})
    return jsonify({'message': f'Route with ID {route_id} not found'}), 404


def update_order(order_id):
    try:
        print(f'Received PUT request for order ID: {order_id}')
        order_data = request.get_json()
        print(f'Received data: {order_data}')

        db.init_app(app)

        updated_order = OrderDAO.update_order_by_id(order_id, order_data)

        if updated_order:
            return jsonify(order_schema.dump(updated_order))
        return jsonify({'message': f'Order with ID {order_id} not found'}), 404
    except Exception as e:
        print(f'Error: {e}')
        return jsonify({'error': str(e)}), 400


@app.route('/orders/<int:order_id>', methods=['DELETE'])
def delete_order(order_id):
    success = OrderDAO.delete_order_by_id(order_id)
    if success:
        return jsonify({'message': f'Order with ID {order_id} deleted successfully'})
    return jsonify({'message': f'Order with ID {order_id} not found'}), 404


def update_driver_rating(driver_rating_id):
    try:
        print(f'Received PUT request for driver rating ID: {driver_rating_id}')
        driver_rating_data = request.get_json()
        print(f'Received data: {driver_rating_data}')

        db.init_app(app)

        updated_driver_rating = DriverRatingDAO.update_driver_rating_by_id(driver_rating_id, driver_rating_data)

        if updated_driver_rating:
            return jsonify(driver_rating_schema.dump(updated_driver_rating))
        return jsonify({'message': f'Driver rating with ID {driver_rating_id} not found'}), 404
    except Exception as e:
        print(f'Error: {e}')
        return jsonify({'error': str(e)}), 400


@app.route('/driver_ratings/<int:driver_rating_id>', methods=['DELETE'])
def delete_driver_rating(driver_rating_id):
    success = DriverRatingDAO.delete_driver_rating_by_id(driver_rating_id)
    if success:
        return jsonify({'message': f'Driver rating with ID {driver_rating_id} deleted successfully'})
    return jsonify({'message': f'Driver rating with ID {driver_rating_id} not found'}), 404


def update_availability_car(availability_car_id):
    try:
        print(f'Received PUT request for availability car ID: {availability_car_id}')
        availability_car_data = request.get_json()
        print(f'Received data: {availability_car_data}')

        db.init_app(app)

        updated_availability_car = AvailabilityCarDAO.update_availability_car_by_id(availability_car_id, availability_car_data)

        if updated_availability_car:
            return jsonify(availability_car_schema.dump(updated_availability_car))
        return jsonify({'message': f'Availability car with ID {availability_car_id} not found'}), 404
    except Exception as e:
        print(f'Error: {e}')
        return jsonify({'error': str(e)}), 400


@app.route('/availability_cars/<int:availability_car_id>', methods=['DELETE'])
def delete_availability_car(availability_car_id):
    success = AvailabilityCarDAO.delete_availability_car_by_id(availability_car_id)
    if success:
        return jsonify({'message': f'Availability car with ID {availability_car_id} deleted successfully'})
    return jsonify({'message': f'Availability car with ID {availability_car_id} not found'}), 404


def update_driver_car(driver_car_id):
    try:
        print(f'Received PUT request for driver car ID: {driver_car_id}')
        driver_car_data = request.get_json()
        print(f'Received data: {driver_car_data}')

        db.init_app(app)

        updated_driver_car = DriverCarDAO.update_driver_car_by_id(driver_car_id, driver_car_data)

        if updated_driver_car:
            return jsonify(driver_car_schema.dump(updated_driver_car))
        return jsonify({'message': f'Driver car with ID {driver_car_id} not found'}), 404
    except Exception as e:
        print(f'Error: {e}')
        return jsonify({'error': str(e)}), 400


@app.route('/driver_has_cars/<int:driver_car_id>', methods=['DELETE'])
def delete_driver_car(driver_car_id):
    success = DriverCarDAO.delete_driver_car_by_id(driver_car_id)
    if success:
        return jsonify({'message': f'Driver car with ID {driver_car_id} deleted successfully'})
    return jsonify({'message': f'Driver car with ID {driver_car_id} not found'}), 404


def update_feedback(feedbacks_id):
    try:
        print(f'Received PUT request for feedback ID: {feedbacks_id}')
        feedback_data = request.get_json()
        print(f'Received data: {feedback_data}')

        db.init_app(app)

        updated_feedback = FeedbackDAO.update_feedback_by_id(feedbacks_id, feedback_data)

        if updated_feedback:
            return jsonify(feedback_schema.dump(updated_feedback))
        return jsonify({'message': f'Feedback with ID {feedbacks_id} not found'}), 404
    except Exception as e:
        print(f'Error: {e}')
        return jsonify({'error': str(e)}), 400


@app.route('/feedbacks/<int:feedbacks_id>', methods=['DELETE'])
def delete_feedback(feedbacks_id):
    success = FeedbackDAO.delete_feedback_by_id(feedbacks_id)
    if success:
        return jsonify({'message': f'Feedback with ID {feedbacks_id} deleted successfully'})
    return jsonify({'message': f'Feedback with ID {feedbacks_id} not found'}), 404
