Inventory Management System

The **Inventory Management System** is a Django-based web application that helps manage inventory items. It provides an API for creating, retrieving, updating, and deleting items.

Features
- Add, update, and delete inventory items.
- Retrieve details of inventory items.
- Authentication using Token-based authentication.
- RESTful API endpoints for managing inventory.

Requirements

- Python 3.12.6
- Django 5.1.1
- Django REST Framework
- PostgreSQL
- psycopg2
- django rest framework-simple jwt
- redis

Setup Instructions
1. Clone the Repository

git clone https://github.com/yourusername/inventory_management.git
cd inventory_management

2. Create a Virtual Environment:

python -m venv myenv
On Windows: myenv\Scripts\activate

3. Install Dependencies:

pip install -r requirements.txt

4. Configure PostgreSQL Database:
Create a PostgreSQL database, e.g., inventory_db.
In the settings.py file, configure your database settings:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'inventory_db',
        'USER': 'your_postgres_user',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

5. Apply Migrations:
python manage.py migrate

6. Create a Superuser (for admin access):

python manage.py createsuperuser

7. Run the Development Server:

python manage.py runserver

The application will be accessible at http://127.0.0.1:8000/.
API Endpoints
The application uses Django REST Framework to expose RESTful API endpoints. Below are the key endpoints available:
POST /api/items/ - Create a new item
GET /api/items/<id>/ - Retrieve a specific item by ID
PUT /api/items/<id>/ - Update an item by ID
DELETE /api/items/<id>/ - Delete an item by ID
Authentication:
Token-based authentication is used for the API. You must include a valid token in the Authorization header of the request.
Example:

curl -X GET http://127.0.0.1:8000/api/items/ -H "Authorization: Token your_token_here"

Running Tests
The project includes a suite of tests for testing the API endpoints.
To run the tests:

python manage.py test

Common Issues
1. 401 Unauthorized Error
If you encounter 401 Unauthorized when accessing API endpoints, make sure you include the authentication token in the request headers.
2. Database Connection Error
If you're having trouble connecting to the PostgreSQL database, ensure your settings.py file has the correct database credentials and the PostgreSQL service is running.
Technologies Used
Django: A Python web framework used for rapid development and clean design.
Django REST Framework: A powerful toolkit for building Web APIs.
PostgreSQL: An open-source relational database used for managing data.
License
This project is licensed under the MIT License. See the LICENSE file for details.
Contact
For any inquiries, feel free to contact:
Name: raj
Email: pandula3896@gmail.com
GitHub: https:https://github.com/katamraj123/




This `README.md` provides all essential information about the project setup, configuration, API usage, and troubleshooting, making it easy for developers to understand and use the project.



