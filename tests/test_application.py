import requests

def test_flavors():
    response = requests.get('http://localhost:5000/flavors')
    assert response.status_code == 200

def test_add_flavor():
    response = requests.post(
        'http://localhost:5000/flavors',
        json={'name': 'Pumpkin Spice', 'description': 'Autumn favorite', 'available': True}
    )
    assert response.status_code == 201

def test_suggestions():
    response = requests.post(
        'http://localhost:5000/suggestions',
        json={'customer_name': 'John Doe', 'flavor_suggestion': 'Matcha', 'allergy_concern': 'None'}
    )
    assert response.status_code == 201
