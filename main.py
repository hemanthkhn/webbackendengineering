from flask import Flask, jsonify, render_template, request, redirect
from flask_mysqldb import MySQL
from flask_swagger_ui import get_swaggerui_blueprint
from swagger_spec import get_swagger_spec

app = Flask(__name__)

# MySQL Configuration
app.config['MYSQL_HOST']  = 'localhost' 
app.config['MYSQL_USER'] = ''   
app.config['MYSQL_PASSWORD'] = ''  
app.config['MYSQL_DB'] = 'ecommerce_db' 

mysql = MySQL(app)

@app.route('/', methods=['GET'])
def homepage():
    return '''
    <h1>Welcome to the E-commerce API!</h1>
    <form action="/products">
        <input type="submit" value="View Products">
    </form>
    '''

# Error handling decorator
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error 404': 'Not found'}), 404

@app.errorhandler(400)
def bad_request(error):
    return jsonify({'error 400': 'Bad request'}), 400


# To get all products
@app.route('/products', methods=['GET'])
def get_products():
    try:
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM products")
        products = cur.fetchall()
        cur.close()

        if not products:
            return render_template('products.html', message="No products available")
        
        return render_template('products.html', products=products)
    except Exception as e:
        print("Error fetching products:", e)
        return jsonify({'error 500': str(e)}), 500


# To get a specific product by ID
@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    try:
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM products WHERE id = %s", (product_id,))
        product = cur.fetchone()
        cur.close()
        if product:
            return jsonify(product)
        else:
            return jsonify({'error 404': 'Product not found'}), 404
    except Exception as e:
        return jsonify({'error 500': str(e)}), 500

# To create a product
@app.route('/products', methods=['POST'])
def create_product():
    try:
        data = request.json
        name = data.get('name')
        price = data.get('price')
        description = data.get('description')

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO products (name, price, description) VALUES (%s, %s, %s)", (name, price, description))
        mysql.connection.commit()
        cur.close()
        return jsonify({'message 201': 'Product created successfully'}), 201
    except Exception as e:
        return jsonify({'error 500': str(e)}), 500

# To update a product by ID
@app.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    try:
        data = request.json
        name = data.get('name')
        price = data.get('price')
        description = data.get('description')

        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM products WHERE id = %s", (product_id,))
        product = cur.fetchone()
        if product:
            # Product exists, update it
            cur.execute("UPDATE products SET name = %s, price = %s, description = %s WHERE id = %s", (name, price, description, product_id))
            mysql.connection.commit()
            cur.close()
            return jsonify({'message 200': f'Product with ID {product_id} updated successfully'}), 200
        else:
            # Product does not exist
            return jsonify({'error 404': 'Product not found'}), 404
    except Exception as e:
        return jsonify({'error 500': str(e)}), 500


@app.route('/add_product', methods=['POST'])
def add_product():
    try:
        product_id = request.form.get('productId') 
        name = request.form.get('productName')
        price = request.form.get('productPrice')
        description = request.form.get('productDescription')

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO products (id, name, price, description) VALUES (%s, %s, %s, %s)", (product_id, name, price, description))
        mysql.connection.commit()
        cur.close()
        return redirect('/products')
    except Exception as e:
        return jsonify({'error 500': str(e)}), 500

# To delete a product by ID
@app.route('/delete_product/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    try:
        print("Deleting product with ID:", product_id)
        cur = mysql.connection.cursor()
        # Checking if the product exists
        cur.execute("SELECT * FROM products WHERE id = %s", (product_id,))
        product = cur.fetchone()
        if product:
            # Product exists, delete it
            cur.execute("DELETE FROM products WHERE id = %s", (product_id,))
            mysql.connection.commit()
            cur.close()
            print("Product deleted successfully.") 
            return redirect('/products')
        else:
            # Product does not exist
            print("Product not found.")
            return jsonify({'error 404': 'Product not found'}), 404
    except Exception as e:
        print("Error:", e) 
        return jsonify({'error 500': str(e)}), 500


# Define the Swagger blueprint
SWAGGER_URL = '/swagger'
API_URL = '/swagger.json'

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "E-commerce API"
    }
)

# Register the Swagger blueprint
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

# Define the Swagger specifications
@app.route('/swagger.json')
def swagger_spec():
    spec = get_swagger_spec()
    return jsonify(spec)

if __name__ == '__main__':
    app.run(debug=True)
