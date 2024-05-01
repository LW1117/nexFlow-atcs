from ultralytics import YOLO

model = YOLO('yolov8n.pt')
# source = 'media/1.jpeg'

classes = [1, 2, 3, 5, 7]

vehicle_labels = {1: 'bicycle',
                  2: 'car',
                  3: 'motorcycle',
                  5: 'bus',
                  7: 'truck'}


def detect_vehicle(source=''):
    results = model(source, classes=classes)  # list of Results objects

    number_of_each_vehicle = {'bicycle': 0, 'car': 0,
                              'motorcycle': 0, 'bus': 0, 'truck': 0}
    total_number_of_vehicles = 0

    number_of_each_vehicle, total_number_of_vehicles = vehicle_count(
        results, number_of_each_vehicle, total_number_of_vehicles)

    return number_of_each_vehicle, total_number_of_vehicles


def vehicle_count(results, number_of_each_vehicle, total_number_of_vehicles):

    for r in results:
        for vehicle in r.boxes.cls:
            total_number_of_vehicles += 1
            vehicle_type = vehicle_labels[int(vehicle)]
            if vehicle_type:
                number_of_each_vehicle[vehicle_type] += 1

    return number_of_each_vehicle, total_number_of_vehicles


# number_of_each_vehicle, total_number_of_vehicles = detect_vehicle()

# print(number_of_each_vehicle)

if __name__ == "__main__":
    detect_vehicle()
    vehicle_count()
