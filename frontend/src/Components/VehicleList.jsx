import React from "react";

const VehicleList = ({ vehicles, refresh }) => {
  const onDelete = async (id) => {
    try {
      const options = {
        method: "DELETE",
      };
      const response = await fetch(
        `http://127.0.0.1:5000/delete_vehicle/${id}`,
        options
      );
      if (response.status === 200) {
        refresh();
      } else {
        console.error("Failde to delete");
      }
    } catch (error) {
      alert(error);
    }
  };
  return (
    <div>
      <h2>Vehicles History</h2>
      <table className="table">
        <thead>
          <tr>
            <th scope="col">Date</th>
            <th scope="col">Path to Image</th>
            <th scope="col">Total no of Vehicles</th>
            <th scope="col">Bicycle</th>
            <th scope="col">Car</th>
            <th scope="col">Motorcycle</th>
            <th scope="col">Bus</th>
            <th scope="col">Truck</th>
            <th scope="col">Action</th>
          </tr>
        </thead>
        <tbody>
          {vehicles.map((vehicle) => (
            <tr key={vehicle.id}>
              <td>{vehicle.date}</td>
              <td>{vehicle.filePath}</td>
              <td>{vehicle.vehicleTotal}</td>
              <td>{vehicle.bicycle}</td>
              <td>{vehicle.car}</td>
              <td>{vehicle.motorcycle}</td>
              <td>{vehicle.bus}</td>
              <td>{vehicle.truck}</td>
              <td>
                <button
                  type="button"
                  className="btn btn-danger"
                  onClick={() => onDelete(vehicle.id)}
                >
                  Delete
                </button>
              </td>
            </tr>
          ))}
          <tr></tr>
        </tbody>
      </table>
    </div>
  );
};

export default VehicleList;
