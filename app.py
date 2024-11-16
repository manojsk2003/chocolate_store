from flask import Flask, request, jsonify
from storage import connect_db, init_db

def create_app():
    """Create and configure the Flask application."""
    app = Flask(__name__)

    # Initialize the database (you could move this to a separate route if you like)
    init_db()

    # Route to manage seasonal flavors
    @app.route('/flavors', methods=['GET', 'POST'])
    def handle_flavors():
        """Get all seasonal flavors or add a new one."""
        conn = connect_db()
        cursor = conn.cursor()

        if request.method == 'POST':
            data = request.json
            try:
                cursor.execute(
                    "INSERT INTO SeasonalFlavors (name, description, is_available) VALUES (?, ?, ?)",
                    (data['name'], data['description'], data['is_available'])
                )
                conn.commit()
                return jsonify({'message': f"Flavor '{data['name']}' added!"}), 201
            except Exception as e:
                return jsonify({'error': str(e)}), 400

        cursor.execute("SELECT * FROM SeasonalFlavors")
        flavors = cursor.fetchall()
        conn.close()
        return jsonify(flavors), 200

    # Route to manage ingredients
    @app.route('/ingredients', methods=['GET', 'POST'])
    def manage_ingredients():
        conn = connect_db()
        cursor = conn.cursor()
        if request.method == 'POST':
            data = request.json
            cursor.execute("INSERT INTO Ingredients (name, quantity) VALUES (?, ?)", 
                           (data['name'], data['quantity']))
            conn.commit()
            return jsonify({'message': 'Ingredient added successfully!'}), 201

        cursor.execute("SELECT * FROM Ingredients")
        ingredients = cursor.fetchall()
        conn.close()
        return jsonify(ingredients)

    # Add a route for customer feedback
    @app.route('/feedback', methods=['POST'])
    def customer_feedback():
        data = request.json
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO CustomerFeedback (customer_name, flavor_suggestion, allergy_info) VALUES (?, ?, ?)",
            (data['customer_name'], data['flavor_suggestion'], data['allergy_info'])
        )
        conn.commit()
        conn.close()
        return jsonify({'message': 'Feedback submitted!'}), 201

    return app

# Running the Flask application
if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=5000, debug=True)
