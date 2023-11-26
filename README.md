
# Django Blog Tutorial

This Django project is a tutorial for building a Blog website with CRUD functionality using the Python Django framework. The tutorial has been published on the [Faradars website](https://faradars.org/courses/website-and-web-application-design-using-django-and-python-fvdjn101).

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Database Configuration](#database-configuration)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Faradars Tutorial Link](#faradars-tutorial-link)

## Introduction

This Django project serves as a step-by-step guide for creating a Blog website (and also any website) with CRUD functionality using the Django framework. The tutorial covers essential concepts in Django development, including python basic tutorial, models, views, templates, forms, authentication, jinja codes, http requests.

## Features

- CRUD (Create, Read, Update, Delete) functionality for blog posts
- Integration with PostgreSQL for database management
- Image uploading and handling using Pillow

## Requirements

Ensure you have the following dependencies installed:

- asgiref==3.6.0
- Django==4.1.7
- Pillow==9.4.0
- psycopg2==2.9.5
- psycopg2-binary==2.9.5
- sqlparse==0.4.3
- tzdata==2022.7

You can install them using the following command:

```bash
pip install -r requirements.txt
```

## Installation

To set up the Django Blog project locally, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/your-repository.git
   ```

2. Navigate to the project directory:

   ```bash
   cd your-repository
   ```

3. (Optional) Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

   If you choose not to use a virtual environment, skip this step.

4. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. Apply database migrations:

   ```bash
   python manage.py migrate
   ```

6. Create a superuser account:

   ```bash
   python manage.py createsuperuser
   ```

   Follow the prompts to set up the superuser account.

## Database Configuration

This project is configured to use PostgreSQL. Update the database settings in the `settings.py` file:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_database_name',
        'USER': 'your_database_user',
        'PASSWORD': 'your_database_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

Replace `your_database_name`, `your_database_user`, and `your_database_password` with your PostgreSQL database details.

**OPTIONAL**
If you prefer to use SQLite instead, follow these steps:

1. Open the `settings.py` file located in the `ryan_blog` project directory.

2. Comment out the existing `DATABASES` configuration for PostgreSQL:

   ```python
   # DATABASES = {
   #     'default': {
   #         'ENGINE': 'django.db.backends.postgresql',
   #         'NAME': 'your_database_name',
   #         'USER': 'your_database_user',
   #         'PASSWORD': 'your_database_password',
   #         'HOST': 'localhost',
   #         'PORT': '5432',
   #     }
   # }
   ```

3. Uncomment the SQLite configuration:

   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.sqlite3',
           'NAME': BASE_DIR / "db.sqlite3",
       }
   }
   ```

   This configuration uses the default SQLite database file (`db.sqlite3`) in the project directory. You can change the `NAME` parameter to specify a different location or name for the SQLite database file.

4. Save the `settings.py` file.

Now, the Django Blog project is configured to use SQLite. When you run the migration and create a superuser, the SQLite database file will be created in the project directory.

**Note:** If you are using version control (e.g., Git), make sure to add `db.sqlite3` to your `.gitignore` file to avoid committing the database file to the repository.


## Usage

After completing the installation and also configuring the database, you can run the development server:

```bash
python manage.py runserver
```

Visit `http://localhost:8000` in your web browser to access the Django Blog website. Log in with the superuser account you created to access the admin panel at `http://localhost:8000/admin` and start managing blog posts.

## Contributing

If you'd like to contribute to this project, please follow these guidelines:

1. Fork the repository
2. Create a new branch
3. Make your changes
4. Submit a pull request

### Code Style

- Follow the [PEP 8](https://www.python.org/dev/peps/pep-0008/) style guide for Python code.

### Testing

- Ensure that your changes do not break existing functionality.
- Write tests for new features or bug fixes.

### Pull Request Template

Consider using the following template when creating a pull request:

```
## Description

[Describe your changes here]

## Checklist

- [ ] I have tested my changes thoroughly.
- [ ] My code follows the PEP 8 style guide.
- [ ] I have updated the documentation.
- [ ] I have added/updated tests for my changes.
```

We appreciate your contributions! Happy coding!

## License

This Django Blog project is open-source and available under the [MIT License](LICENSE).

## Faradars Tutorial Link

Visit [Faradars Tutorial](https://faradars.org/courses/website-and-web-application-design-using-django-and-python-fvdjn101) for an in-depth guide on building a Blog website with CRUD functionality using Django.
