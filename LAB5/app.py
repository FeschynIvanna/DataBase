# from flask import Flask, jsonify
# from database import init_db
# from flask import request
#
# from models import Driver, CarType, Car, User, Route, Order, DriverRating, AvailabilityCar, DriverCar, Feedback
#
# from controllers import (
#     get_all_drivers, get_driver_by_id, create_driver, delete_driver,
#     get_all_car_types, get_all_cars, get_all_users,
#     get_all_routes, get_all_orders, get_all_driver_ratings,
#     get_all_availability_cars, get_all_driver_cars, get_all_feedbacks, get_cars_with_types, get_orders_with_details,
#     get_feedbacks_by_id, get_driver_has_car_by_id, get_car_by_id, get_car_type_by_id, get_user_by_id, get_route_by_id,
#     get_order_by_id, get_driver_rating_by_id, get_availability_car_by_id, create_car_type, create_car, create_user,
#     create_route, create_order, create_driver_rating, create_availability_car, create_driver_car, create_feedback,
#     update_driver)
#
# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Ivanna2223@localhost/Laba1'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config['SECRET_KEY'] = 'cairocoders-ednalan'
# app.config['SQLALCHEMY_ECHO'] = True
#
# init_db(app)
from flask import Flask, jsonify
from database import db, init_db
from flask import request
from controllers import (
    get_all_drivers, get_driver_by_id, create_driver, delete_driver,
    get_all_car_types, get_all_cars, get_all_users,
    get_all_routes, get_all_orders, get_all_driver_ratings,
    get_all_availability_cars, get_all_driver_cars, get_all_feedbacks, get_cars_with_types, get_orders_with_details,
    get_feedbacks_by_id, get_driver_has_car_by_id, get_car_by_id, get_car_type_by_id, get_user_by_id, get_route_by_id,
    get_order_by_id, get_driver_rating_by_id, get_availability_car_by_id, create_car_type, create_car, create_user,
    create_route, create_order, create_driver_rating, create_availability_car, create_driver_car, create_feedback,
    update_driver, update_car_type, delete_car_type, update_car, delete_car, update_user, delete_user, update_route,
    delete_route, update_order, delete_order, update_driver_rating, delete_driver_rating, update_availability_car,
    delete_availability_car, update_driver_car, delete_driver_car, update_feedback, delete_feedback)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Ivanna2223@localhost/Laba1'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'cairocoders-ednalan'
app.config['SQLALCHEMY_ECHO'] = True


init_db(app)


@app.route('/')
def index():
    return jsonify({'message': 'Welcome to your Flask app!'})


@app.route('/drivers', methods=['GET', 'POST'])
def drivers():
    if request.method == 'GET':
        return get_all_drivers()
    elif request.method == 'POST':
        return create_driver()


@app.route('/drivers/<int:driver_id>', methods=['PUT', 'DELETE'])
def driver_(driver_id):
    if request.method == 'PUT':
        return update_driver(driver_id)
    elif request.method == 'DELETE':
        return delete_driver(driver_id)


# @app.route('/drivers/<int:driver_id>', methods=['DELETE'])
# def delete_driver_route(driver_id):
#     return delete_driver(driver_id)


@app.route('/drivers/<int:driver_id>', methods=['GET'])
def driver(driver_id):
    return get_driver_by_id(driver_id)


@app.route('/cars_type', methods=['GET', 'POST'])
def car_types():
    if request.method == 'GET':
        return get_all_car_types()
    elif request.method == 'POST':
        return create_car_type()


@app.route('/cars_type/<int:car_type_id>', methods=['PUT', 'DELETE'])
def car_type_(car_type_id):
    if request.method == 'PUT':
        return update_car_type(car_type_id)
    elif request.method == 'DELETE':
        return delete_car_type(car_type_id)


@app.route('/cars', methods=['GET', 'POST'])
def cars():
    if request.method == 'GET':
        return get_all_cars()
    elif request.method == 'POST':
        return create_car()


@app.route('/cars/<int:car_id>', methods=['PUT', 'DELETE'])
def car_(car_id):
    if request.method == 'PUT':
        return update_car(car_id)
    elif request.method == 'DELETE':
        return delete_car(car_id)


@app.route('/users', methods=['GET', 'POST'])
def users():
    if request.method == 'GET':
        return get_all_users()
    elif request.method == 'POST':
        return create_user()


@app.route('/users/<int:user_id>', methods=['PUT', 'DELETE'])
def user_(user_id):
    if request.method == 'PUT':
        return update_user(user_id)
    elif request.method == 'DELETE':
        return delete_user(user_id)


@app.route('/routes', methods=['GET', 'POST'])
def routes():
    if request.method == 'GET':
        return get_all_routes()
    elif request.method == 'POST':
        return create_route()


@app.route('/routes/<int:route_id>', methods=['PUT', 'DELETE'])
def route_(route_id):
    if request.method == 'PUT':
        return update_route(route_id)
    elif request.method == 'DELETE':
        return delete_route(route_id)


@app.route('/orders', methods=['GET', 'POST'])
def orders():
    if request.method == 'GET':
        return get_all_orders()
    elif request.method == 'POST':
        return create_order()


@app.route('/orders/<int:order_id>', methods=['PUT', 'DELETE'])
def order_(order_id):
    if request.method == 'PUT':
        return update_order(order_id)
    elif request.method == 'DELETE':
        return delete_order(order_id)


@app.route('/driver-ratings', methods=['GET', 'POST'])
def driver_ratings():
    if request.method == 'GET':
        return get_all_driver_ratings()
    elif request.method == 'POST':
        return create_driver_rating()


@app.route('/driver-ratings/<int:driver_rating_id>', methods=['PUT', 'DELETE'])
def driver_rating_(driver_rating_id):
    if request.method == 'PUT':
        return update_driver_rating(driver_rating_id)
    elif request.method == 'DELETE':
        return delete_driver_rating(driver_rating_id)


@app.route('/availability-cars', methods=['GET', 'POST'])
def availability_cars():
    if request.method == 'GET':
        return get_all_availability_cars()
    elif request.method == 'POST':
        return create_availability_car()


@app.route('/availability-cars/<int:availability_car_id>', methods=['PUT', 'DELETE'])
def availability_car_(availability_car_id):
    if request.method == 'PUT':
        return update_availability_car(availability_car_id)
    elif request.method == 'DELETE':
        return delete_availability_car(availability_car_id)


@app.route('/driver_has_cars', methods=['GET', 'POST'])
def driver_cars():
    if request.method == 'GET':
        return get_all_driver_cars()
    elif request.method == 'POST':
        return create_driver_car()


@app.route('/driver_has_cars/<int:driver_car_id>', methods=['PUT', 'DELETE'])
def driver_car_(driver_car_id):
    if request.method == 'PUT':
        return update_driver_car(driver_car_id)
    elif request.method == 'DELETE':
        return delete_driver_car(driver_car_id)


@app.route('/feedbacks', methods=['GET', 'POST'])
def feedbacks():
    if request.method == 'GET':
        return get_all_feedbacks()
    elif request.method == 'POST':
        return create_feedback()


@app.route('/feedbacks/<int:feedback_id>', methods=['PUT', 'DELETE'])
def feedback_(feedback_id):
    if request.method == 'PUT':
        return update_feedback(feedback_id)
    elif request.method == 'DELETE':
        return delete_feedback(feedback_id)


@app.route('/cars_with_types', methods=['GET'])
def cars_with_types():
    return get_cars_with_types()


@app.route('/orders_with_details', methods=['GET'])
def orders_with_details():
    return get_orders_with_details()


@app.route('/cars_type/<int:car_type_id>', methods=['GET'])
def car_type(car_type_id):
    return get_car_type_by_id(car_type_id)


@app.route('/cars/<int:car_id>', methods=['GET'])
def car(car_id):
    return get_car_by_id(car_id)


@app.route('/users/<int:user_id>', methods=['GET'])
def user(user_id):
    return get_user_by_id(user_id)


@app.route('/routes/<int:route_id>', methods=['GET'])
def route(route_id):
    return get_route_by_id(route_id)


@app.route('/orders/<int:order_id>', methods=['GET'])
def order(order_id):
    return get_order_by_id(order_id)


@app.route('/driver-ratings/<int:driver_rating_id>', methods=['GET'])
def driver_rating(driver_rating_id):
    return get_driver_rating_by_id(driver_rating_id)


@app.route('/availability-cars/<int:availability_car_id>', methods=['GET'])
def availability_car(availability_car_id):
    return get_availability_car_by_id(availability_car_id)


@app.route('/driver_has_cars/<int:driver_car_id>', methods=['GET'])
def driver_has_car(driver_has_car_id):
    return get_driver_has_car_by_id(driver_has_car_id)


@app.route('/feedbacks/<int:feedbacks_id>', methods=['GET'])
def feedback(feedbacks_id):
    return get_feedbacks_by_id(feedbacks_id)


class CarDetails(db.Model):
    __tablename__ = 'CarDetails'

    id = db.Column(db.Integer, primary_key=True)
    detail_name = db.Column(db.String(50), nullable=False)
    detail_description = db.Column(db.String(255))
    Cars_id = db.Column(db.Integer, nullable=False)

# Ручка для отримання даних з таблиці CarDetails
@app.route('/car_details', methods=['GET'])
def get_car_details():
    car_details = CarDetails.query.all()
    car_details_list = []

    for detail in car_details:
        detail_data = {
            'id': detail.id,
            'detail_name': detail.detail_name,
            'detail_description': detail.detail_description,
            'Cars_id': detail.Cars_id
        }
        car_details_list.append(detail_data)

    return jsonify({'car_details': car_details_list})


if __name__ == '__main__':
    app.run(debug=True)
