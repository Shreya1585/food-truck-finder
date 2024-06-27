**1. Set Up Git for Source Control**
Clone the repository to your local machine and navigate to the project directory
git clone https://github.com/YOUR_USERNAME/food-truck-finder.git
cd food-truck-finder

**2. Design the Web API**
Create a new directory for the API:
mkdir api
cd api

**3. Initialize a new Python project**

python3 -m venv venv
source venv/bin/activate
pip install flask pandas

**4. Create the API script (api.py)**

from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)

@app.route('/foodtrucks', methods=['GET'])
def get_foodtrucks():
    df = pd.read_csv('path/to/your/csv')
    foodtrucks = df.to_dict(orient='records')
    return jsonify(foodtrucks)

if __name__ == '__main__':
    app.run(debug=True)
    
**5. Create the Web Frontend**
**Create a new directory for the frontend:**

mkdir ../frontend
cd ../frontend
**Initialize a new React project (using create-react-app):**

npx create-react-app food-truck-frontend
cd food-truck-frontend
**Modify the App.js to fetch and display food trucks:**

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
**6. Develop the Command Line Interface (CLI)**
Create a new directory for the CLI:

mkdir ../cli
cd ../cli
Initialize a new Python script (cli.py):

import pandas as pd
import click

@click.command()
@click.option('--city', default='San Francisco', help='City to search for taco trucks')
def get_taco_trucks(city):
    df = pd.read_csv('path/to/your/csv')
    taco_trucks = df[df['fooditems'].str.contains('taco', case=False, na=False)]
    for index, row in taco_trucks.iterrows():
        print(row['applicant'])

if __name__ == '__main__':
    get_taco_trucks()
**7. Set Up Docker for Containerization**
**Create a Dockerfile for the API:**

FROM python:3.8-slim

WORKDIR /app

COPY ./api /app

RUN pip install -r requirements.txt

CMD ["python", "api.py"]
**Create a Dockerfile for the frontend:**

FROM node:14

WORKDIR /app

COPY ./frontend /app

RUN npm install

CMD ["npm", "start"]
**Create a docker-compose.yml file to manage the containers:**

version: '3'

services:
  api:
    build: ./api
    ports:
      - "5000:5000"
  frontend:
    build: ./frontend
    ports:
      - "3000:3000"
    depends_on:
      - api

# Food Truck Finder

This project helps you find food trucks in San Francisco. It includes:

- A web API that returns a list of food trucks.
- A web frontend that visualizes nearby food trucks.
- A CLI to get the names of all taco trucks in the city.
- A Docker setup for containerizing the application.

**** Prerequisites****

- Docker
- Node.js
- Python 3.8


**8. Set Up Terraform for Infrastructure Management**

1. Create a new directory for Terraform configuration:
  
   mkdir terraform
   cd terraform
Create a main.tf file to define your infrastructure:


provider "aws" {
  region = "us-west-1"
}

resource "aws_instance" "web" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "m5.xlarge"

  tags = {
    Name = "FoodTruckFinder"
  }
}
Initialize Terraform and apply the configuration:


terraform init
terraform apply

Final Steps
Commit your changes and push to GitHub:

git add .
git commit -m "Initial commit"
git push origin main
You now have a complete project with a web API, frontend, CLI, Docker setup, and Terraform configuration.









