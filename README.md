# Django CRUD with Ajax and jQuery
This project is a simple Django web application that demonstrates CRUD (Create, Read, Update, Delete) operations using Django, Ajax, and jQuery. It provides a user-friendly interface for managing data by leveraging the power of asynchronous requests and dynamic updates.
<!-- Add table of contents -->
## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

<!-- Add features list -->
## Features
- Users can add new records
- Users can view existing records retrieved from the database without page refresh
- Users can edit and update specific records in the database using Ajax requests
- Users can remove unwanted records from the database with Ajax requests

<!-- Add installation instructions -->
## Installation

To get started with Django Ajax CRUD App, you need to have Python and pip installed on your system. Then, follow these steps:

1. Clone this repository:
```python
git clone https://github.com/msdqhabib/Django-Ajax-CRUD-Operations
```
2. Navigate to the project directory:
```python
cd Django-Ajax-CRUD-Operations
```
3. Install the required packages:
```python
pip install -r requirements.txt
```
4. Apply the database migrations:
```python
python manage.py makemigrations
python manage.py migrate
```
5. Run the development server:
```python
python manage.py runserver
```

The application will now be available at `http://localhost:8000`.


## Contributing

If you would like to contribute to the Django Ajax CRUD App, you can follow these steps:

1. Fork this repository.
2. Create a new branch for your feature or bug fix.
3. Write your code and add tests if possible.
4. Submit a pull request.

## License

The Django Ajax CRUD App is licensed under the MIT License. See [LICENSE](LICENSE) for more information.
