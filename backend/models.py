from config import db


class Vehicle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, unique=True, nullable=True, )
    # img_name = db.Column(db.String, unique=True, nullable=True)
    file_path = db.Column(db.String, unique=False, nullable=True)
    vehicle_total = db.Column(db.Integer, unique=False, nullable=True)
    bicycle = db.Column(db.Integer, unique=False, nullable=True)
    car = db.Column(db.Integer, unique=False, nullable=True)
    motorcycle = db.Column(db.Integer, unique=False, nullable=True)
    bus = db.Column(db.Integer, unique=False, nullable=True)
    truck = db.Column(db.Integer, unique=False, nullable=True)

    def to_json(self):
        return {
            "id": self.id,
            "date": self.date,
            # "imgName": self.img_name,
            "filePath": self.file_path,
            "vehicleTotal": self.vehicle_total,
            "bicycle": self.bicycle,
            "car": self.car,
            "motorcycle": self.motorcycle,
            "bus": self.bus,
            "truck": self.truck
        }
