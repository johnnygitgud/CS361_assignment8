import requests

BASE_URL = "http://127.0.0.1:5000"

# Function to test the edit_recipe endpoint
def test_edit_recipe():
    data = {
        "id": 1,
        "name": "Spaghetti Bolognese",
        "ingredients": ["spaghetti", "meat sauce"]
    }
    response = requests.post(f"{BASE_URL}/edit_recipe", json=data)
    print("Edit Response:", response.json())

# Function to test the delete_recipe endpoint
def test_delete_recipe():
    data = {"id": 2}
    response = requests.post(f"{BASE_URL}/delete_recipe", json=data)
    print("Delete Response:", response.json())

# Run the test functions
if __name__ == "__main__":
    test_edit_recipe()
    test_delete_recipe()