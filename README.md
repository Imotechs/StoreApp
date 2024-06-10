# Store_app Inventory and Supplier Management API

## Setup

This project implements an API for managing inventory items and suppliers for an online store.


1. **Clone the repository:**

    ```bash
    git clone https://github.com/Imotechs/StoreApp.git
    cd Store_app
    ```

2. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

3. **Run migrations:**

    ```bash
    python manage.py migrate
    ```

4. **Start the development server:**

    ```bash
    python manage.py runserver
    ```

5. **Open your web browser and visit [http://localhost:8000/api/](http://localhost:8000/api/) to view the browsable API.**

## Usage

- Use the browsable API interface to perform CRUD operations on inventory items and suppliers.
- Use tools like curl, Postman, or your preferred HTTP client to interact with the API programmatically.

## API Endpoints
- `GET /api/suppliers/`: Retrieve a list of all suppliers.
- `/api/suppliers/<str:slug>/`: CREATE,DELETE and UPPDATE a supplier.

- `GET /api/items/`: Retrieve a list of all inventory items.
- `/api/items/<str:slug>/`: CREATE,DELETE and UPPDATE an inventory item.



## Additional Notes

- You may need to adjust database settings in `settings.py` to match your environment (e.g., PostgreSQL, MySQL).
- Remember to create a superuser account using `python manage.py createsuperuser` to access the Django admin interface for managing data.
