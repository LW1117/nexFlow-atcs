import { useState, useEffect } from "react";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";

import "./App.css";
import NavBar from "./Components/NavBar";
import VehicleList from "./Components/VehicleList";
import VehicleForm from "./Components/VehicleForm";

function App() {
  const [vehicles, setVehicles] = useState([]);

  useEffect(() => {
    fetchVehicles();
  }, []);

  const fetchVehicles = async () => {
    const response = await fetch("http://127.0.0.1:5000/vehicles");
    const data = await response.json();
    setVehicles(data.vehicles);
  };

  return (
    <div>
      <Router>
        <div>
          <NavBar />
          <div id="main-content">
            <Routes>
              <Route path="/" exact element={<h1 className="h1">Home</h1>} />
              <Route
                path="/list"
                element={
                  <VehicleList vehicles={vehicles} refresh={fetchVehicles} />
                }
              />
              <Route
                path="/detect"
                element={<VehicleForm refresh={fetchVehicles} />}
              />
            </Routes>
          </div>
        </div>
      </Router>
    </div>
  );
}

export default App;
