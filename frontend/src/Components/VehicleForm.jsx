import { useState } from "react";

const VehicleForm = ({ refresh }) => {
  const [filePath, setFilePath] = useState("");

  const onDetect = async (e) => {
    e.preventDefault();

    const data = {
      filePath,
    };
    const url = "http://127.0.0.1:5000/create_vehicle";
    const options = {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(data),
    };
    const response = await fetch(url, options);
    if (response.status !== 201 && response.status !== 200) {
      const message = await response.json();
      alert(data.message);
    }
    refresh();
  };

  return (
    <form onSubmit={onDetect}>
      <div className="form-floating mb-3">
        <input
          type="text"
          id="filePath"
          value={filePath}
          onChange={(e) => setFilePath(e.target.value)}
          className="form-control"
          placeholder="name@example.com"
        />
        <label htmlFor="filePath">File Path</label>
      </div>
      <button type="submit" className="btn btn-primary">
        Detect
      </button>
    </form>
  );
};

export default VehicleForm;
