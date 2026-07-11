import { useEffect, useState } from "react";
import API_BASE_URL from "./services/api";

function App() {
  const [message, setMessage] = useState("");

  useEffect(() => {
    fetch(`${API_BASE_URL}/api/hello`)
      .then((response) => response.json())
      .then((data) => {
        setMessage(data.message);
      });
  }, []);

  return (
    <div className="flex min-h-screen items-center justify-center bg-gray-100">
      <h1 className="text-4xl font-bold text-blue-600">
        {message}
      </h1>
    </div>
  );
}

export default App;