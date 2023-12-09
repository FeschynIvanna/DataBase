from marshmallow import Schema, fields


class DriverSchema(Schema):
    id = fields.Int()
    surname = fields.Str(required=True)
    name = fields.Str(required=True)
    phone = fields.Str(required=True)


class CarTypeSchema(Schema):
    id = fields.Int()
    type_name = fields.Str(required=True)
    description = fields.Str()


class CarSchema(Schema):
    id = fields.Int()
    model = fields.Str(required=True)
    license_plate = fields.Str(required=True)
    CarTypes_id = fields.Int(required=True)


class UserSchema(Schema):
    id = fields.Int()
    surname = fields.Str(required=True)
    name = fields.Str(required=True)
    phone = fields.Str(required=True)


class RouteSchema(Schema):
    id = fields.Int()
    start_location = fields.Str(required=True)
    end_location = fields.Str(required=True)
    distance = fields.Str()


class OrderSchema(Schema):
    id = fields.Int()
    pickup_time = fields.Str(required=True)
    status = fields.Str(required=True)
    Users_id = fields.Int(required=True)
    Routes_id = fields.Int(required=True)
    Cars_id = fields.Int(required=True)
    Cars_CarTypes_id = fields.Int(required=True)

class DriverRatingSchema(Schema):
    id = fields.Int()
    rating = fields.Decimal(required=True)
    comment = fields.Str()
    Drivers_id = fields.Int(required=True)

class AvailabilityCarSchema(Schema):
    id = fields.Int()
    start_time = fields.Decimal()
    end_time = fields.Str()
    available = fields.Str(required=True)

class DriverCarSchema(Schema):
    Drivers_id = fields.Int(required=True)
    Cars_id = fields.Int(required=True)

class FeedbackSchema(Schema):
    id = fields.Int()
    comments = fields.Str(required=True)
    Drivers_id = fields.Int(required=True)
    Users_id = fields.Int(required=True)