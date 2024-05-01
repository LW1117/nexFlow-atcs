from datetime import datetime
from flask import request, jsonify

from config import app, db
from detect import detect_vehicle
from models import Vehicle


@app.route("/vehicles", methods=["GET"])
def get_vehicles():
    vehicles = Vehicle.query.all()
    json_vehicles = list(map(lambda x: x.to_json(), vehicles))
    return jsonify({"vehicles": json_vehicles})


@app.route("/create_vehicle", methods=["POST"])
def create_vehicles():
    date = datetime.now()
    file_path = request.json.get("filePath")

    if not file_path:
        return {
            jsonify({"message": "You must enter a image url"}), 400
        }

    try:
        number_of_each_vehicle, total_number_of_vehicles = detect_vehicle(
            file_path)
    except:
        total_number_of_vehicles = 0
        number_of_each_vehicle = {
            'bicycle': 0, 'car': 0, 'motorcycle': 0, 'bus': 0, 'truck': 0}

    vehicle_total = total_number_of_vehicles
    bicycle = number_of_each_vehicle["bicycle"]
    car = number_of_each_vehicle["car"]
    motorcycle = number_of_each_vehicle["motorcycle"]
    bus = number_of_each_vehicle["bus"]
    truck = number_of_each_vehicle["truck"]

    new_vehicle = Vehicle(date=date, file_path=file_path, vehicle_total=vehicle_total,
                          bicycle=bicycle, car=car, motorcycle=motorcycle, bus=bus, truck=truck)
    try:
        db.session.add(new_vehicle)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({"message": str(e)}), 400

    return jsonify({"message": "Vehicle entry created"}), 201


@app.route("/delete_vehicle/<int:user_id>", methods=["DELETE"])
def delete_contact(user_id):
    vehicle = Vehicle.query.get(user_id)

    if not vehicle:
        return jsonify({"message": "Entry not found"}), 404

    db.session.delete(vehicle)
    db.session.commit()

    return jsonify({"message": "Entry deleted"}), 200


if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=True)
