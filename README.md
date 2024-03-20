
# E-commerce API

This is a simple Flask-based API for managing e-commerce products. It allows users to perform CRUD (Create, Read, Update, Delete) operations on products stored in a MySQL database.

## Features

- View all products
- View a specific product by ID
- Create a new product
- Update an existing product
- Delete a product by ID
- Swagger UI for API documentation

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/hemanthkhn/ecommerce-api.git
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Set up MySQL:
   
   - Make sure you have MySQL installed and running on your machine.
   - Create a database named `ecommerce_db`.
   - Update the MySQL configuration in `main.py` with your MySQL credentials.

4. Run the Flask app:

   ```bash
   python3 main.py
   ```

5. Access the API at `http://localhost:5000`.

## API Endpoints

- `GET /products`: Get all products
- `GET /products/<product_id>`: Get a specific product by ID
- `POST /products`: Create a new product
- `PUT /products/<product_id>`: Update an existing product by ID
- `DELETE /products/<product_id>`: Delete a product by ID

## Swagger UI

The API documentation is available using Swagger UI. Access it at `http://localhost:5000/swagger`.


