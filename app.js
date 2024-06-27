import React, { useEffect, useState } from 'react';

function App() {
  const [foodTrucks, setFoodTrucks] = useState([]);

  useEffect(() => {
    fetch('/api/foodtrucks')
      .then(response => response.json())
      .then(data => setFoodTrucks(data));
  }, []);

  return (
    <div>
      <h1>Food Trucks in San Francisco</h1>
      <ul>
        {foodTrucks.map(truck => (
          <li key={truck.id}>{truck.name}</li>
        ))}
      </ul>
    </div>
  );
}

export default App;
