import os


# environmnet specific config. 
if os.environ.get('FLASK_ENV', 'development') in ['development', 'test']:
    # dev db - localhost flask app; localhost sqlite db
    # basedir = os.path.abspath(os.path.dirname(__file__))
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'database', 'app.db')

    # test db - localhost flask app; db running in container
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://airflow:airflow@localhost:5432/postgres'

    # hard code uploads to app/static folder for now.
    UPLOAD_FOLDER = '/Users/ckirby/git/calypso/app/static'

else:
    # prod db - flask app and db running in containers
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://airflow:airflow@db:5432/postgres'

    # upload to dedicated folder in prod
    UPLOAD_FOLDER = '/uploads'


# common environment config
ALLOWED_EXTENSIONS = {'txt', 'csv'}
