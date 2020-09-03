# Calypso CSV Challenge

Docker and docker-compose are needed to lauch app locally. Execute `docker-compose build & docker-compose up` to start the app. Next navigate to http://localhost:5000 to view.

To run in dev/test mode you'll need to:
- setup to locally. The app is already configured to use a postgres container. Execute `docker-compose -f docker-compose-test.yaml up -d` to start the container. You can use any postgres instnace, but you'll need to update the database connection string stored in SQLALCHEMY_DATABASE_URI in config.py. 
- install dependencies. e.g. `pip install -r requirements.txt` (strongly recommend using a virtualenv)
- run initial database migrations. e.g. `flask db upgrade`
- set environment variable FLASK_ENV to development. e.g. `export FLASK_ENV=development`

To run behave tests you'll need to:
- have Chrome installed.
- download the correct version of chromedriver from https://chromedriver.chromium.org/. Update CHROMEDRIVER_PATH constant in features/environment.py with the location of chromedriver executable.
- Now run `behave` from project directory to see test results.


### To Dos
-	~~Upload a CSV file~~
-	~~List uploaded CSV files~~
-	~~Download the previously uploaded CSV file~~
-	~~Display the CSV content showing at least all column headers and content~~
-	~~Provide statistics on the number of people with the same year in the “date” field.~~
-   ~~The CSV file may contain empty string in the ‘state’ column. In this case, fill in with the text “BLANK” instead~~
-   Clean up UI
-   ~~Docker setup~~
-   ECS setup
-   ~~Deployment instructions~~