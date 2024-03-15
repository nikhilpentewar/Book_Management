# Django Book Management Project

This Django project provides a platform for managing books with CRUD (Create, Read, Update, Delete) operations. It also includes a REST API for interacting with the book data.

## Features

- **CRUD Operations**: Perform Create, Read, Update, and Delete operations on books.
- **REST API**: Access book data through a RESTful API for integration with other applications.
- **User Authentication**: Secure access to the application with user authentication.
- **Responsive Design**: The frontend interface is designed to be responsive and accessible on different devices.
- **Search and Filter**: Easily search and filter books based on various criteria.

## Technologies Used

- **Django**: Web framework for building the application.
- **Python**: Programming language used for backend development.
- **HTML/CSS**: Frontend markup and styling.
- **Django REST Framework**: For building the RESTful API.
- **SQLite**: Database management system for storing book data.

## Installation

1. Clone the repository:
```bash
git clone https://github.com/nikhilpentewar/django-book-management.git
```
2. Navigate to the project directory:
```bash
cd django-book-management
```
3. Create a virtual environment (optional but recommended):
```bash
python -m venv env
```
4. Activate the virtual environment:

- On Windows:
```bash
env\Scripts\activate
```

- On macOS and Linux:
```bash
source env/bin/activate
```
5. Install dependencies:
```bash
pip install -r requirements.txt
```
6. Apply migrations:
```bash
python manage.py migrate
```
7. Run the development server:
```bash
python manage.py runserver
```
8. Access the application at `http://localhost:8000` in your web browser.

## Usage

- **CRUD Operations**: Navigate to the appropriate pages to perform CRUD operations on books.
- **REST API**: Access the API endpoints at `/api/books/`.
- **User Authentication**: Register for a new account or log in with existing credentials to access authenticated features.

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/my-feature`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature/my-feature`).
6. Create a new Pull Request.

## Acknowledgements

- This project was inspired by the need for a simple yet effective book management system.
- Special thanks to the Django and Django REST Framework communities for their excellent documentation and support.
