# OBJORPROG-QUIZ2
Clone the project:

git clone https://github.com/yourusername/your-repo.git
cd your-repo


Create and activate a virtual environment:

python -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`


Install dependencies:

pip install -r requirements.txt


Run migrations:

python manage.py makemigrations
python manage.py migrate


Create a superuser (optional):

python manage.py createsuperuser


Run the development server:

python manage.py runserver
