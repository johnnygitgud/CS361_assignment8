# CS361_assignment8

📌 Recipe Editing & Deletion Microservice
Overview

This microservice allows clients to edit and delete recipes via HTTP requests. It operates as a RESTful service, listening for requests and responding with confirmation messages or errors.
Communication Contract
1️⃣ How to Request Data

To interact with the microservice, send an HTTP POST request to the appropriate endpoint with JSON-formatted data.
🔹 Editing a Recipe

    Endpoint: /edit_recipe
    Method: POST
    Request Body (JSON):

{
  "id": 1,
  "name": "Spaghetti Bolognese",
  "ingredients": ["spaghetti", "meat sauce"]
}

Example Python Call:

    import requests

    data = {
        "id": 1,
        "name": "Spaghetti Bolognese",
        "ingredients": ["spaghetti", "meat sauce"]
    }

    response = requests.post("http://127.0.0.1:5000/edit_recipe", json=data)
    print(response.json())

🔹 Deleting a Recipe

    Endpoint: /delete_recipe
    Method: POST
    Request Body (JSON):

{
  "id": 2
}

Example Python Call:

    import requests

    data = {"id": 2}
    response = requests.post("http://127.0.0.1:5000/delete_recipe", json=data)
    print(response.json())

2️⃣ How to Receive Data

Responses will be returned as JSON objects.
✅ Successful Edit Response:

{
  "message": "Recipe updated",
  "recipe": {
    "name": "Spaghetti Bolognese",
    "ingredients": ["spaghetti", "meat sauce"]
  }
}

✅ Successful Delete Response:

{
  "message": "Recipe deleted"
}

❌ Error Response (Invalid ID):

{
  "error": "Recipe not found"
}
