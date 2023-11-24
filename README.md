
# Django REST Framework Todo App

## Overview
This project is a Todo application built using Django REST Framework (DRF). It allows users to manage their tasks efficiently and effectively. Users can create, read, update, and delete tasks, providing a simple yet powerful tool for task management.

## Features

- **CRUD Operations**: Create, Read, Update, and Delete tasks.
- **Search and Filter**: Enhanced features to search and filter tasks.


## Technologies Used
- Django and Django REST Framework
- SQLite (Default Django Database)


## Getting Started

### Prerequisites
- Python 3.10.11
- pip

### Setting Up a Virtual Environment


### Installation
1. Clone the repository:
   ```
   git clone https://github.com/your-username/todo-app-drf.git
   ```
2. Navigate to the project directory:
   ```
   cd todo-app-drf
   ```
3. Install virtualenv if you haven't installed it yet:
   ```
   pip install virtualenv
   ```
4. Create a virtual environment in the project directory:
   ```
   virtualenv venv
   ```
5. Activate the virtual environment:
   - On Windows:
     ```
     .\venv\Scripts\activate
     ```
   - On macOS and Linux:
     ```
     source venv/bin/activate
     ```
7. Install required packages:
   ```
   pip install -r requirements.txt
   ```
8. Migrate the database:
   ```
   python manage.py migrate
   ```
9. Run the server:
   ```
   python manage.py runserver
   ```

## Usage
After running the server, navigate to `http://localhost:8000` in your browser to use the application.

## API Endpoints
Describe your API endpoints here, for example:
- `GET /api/`: List all tasks.
- `POST /api/create`: Create a new task.
- `PUT /api/:id/`: Update a specific task.
- `DELETE /api/delete/:id`: Delete a specific task.

## Contact
For any queries, feel free to reach out at [Twitter] (https://twitter.com/MungaiMbuthi).
