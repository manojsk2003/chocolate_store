import sqlite3

def connect_db():
    return sqlite3.connect("my_store.db")

def init_db():
    """Initializes the database with tables for flavors, ingredients, and customer feedback."""
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS SeasonalFlavors (
            id INTEGER PRIMARY KEY,
            name TEXT UNIQUE,
            description TEXT,
            is_available BOOLEAN
        )
    ''')

    # Table for tracking ingredient inventory
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Ingredients (
            id INTEGER PRIMARY KEY,
            name TEXT,
            quantity INTEGER
        )
    ''')

    # Table for customer suggestions and allergies
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS CustomerFeedback (
            id INTEGER PRIMARY KEY,
            customer_name TEXT,
            flavor_suggestion TEXT,
            allergy_info TEXT
        )
    ''')
    conn.commit()
    conn.close()


if __name__ == "__main__":
    print("Setting up the database...")
    init_db()
    print("Database initialized successfully!")
