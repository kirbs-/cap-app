import os
basedir = os.path.abspath(os.path.dirname(__file__))

if os.environ.get('FLASK_ENV', 'development') in ['development', 'test']:
    # dev db - localhost flask app; localhost sqlite db
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'database', 'app.db')

    # test db - localhost flask app; db running in container
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://airflow:airflow@localhost:5432/postgres'
else:
    # prod db - flask app and db running in containers
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://airflow:airflow@db:5432/postgres'

OTP_SECRET = 'Wdj5ccVm4pGbDy'
DEBUG = True


UPLOAD_FOLDER = '/Users/ckirby/git/calypso/app/static'
ALLOWED_EXTENSIONS = {'txt', 'csv'}
