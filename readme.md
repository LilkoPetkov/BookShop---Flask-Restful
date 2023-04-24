Flask BookShop Rest Backend
Easily scalable python backend using FlaskRESTful Framework for a bookshop. Using Postgres, JWT, Stripe for payment processing and AWS SES for email sending.

Table of contents
Installation
Setup
Technologies
Contibuting
License
Installation
Use the package manager pip to install the requirements located in requirements.txt.

pip install -r requirements.txt
Postgre setup
The project requires PostgreSQL . In the link it can be found available for all operating systems. In order to create and manage the database it is also needed to download a sql client for example PgAdmin.

Setup
Make sure to update the sample_env with the correct details for Postgre and additional services (AWS, Stripe, etc).
The AWS security details could be found in your AWS account -> Profile Dropdown -> Security credentials
Stripe API keys could be found in Stripe (Stripe account required).
The sample_env file should be renamed to: .env
After the environment variables are set, it is needed to run the database migrations.
bash export FLASK_APP=app.py
bash flask db init
bash flask db migrate -m "Add comment here"
bash flask db upgrade
Current endpoints:
/register
/login
/post-order
/books
/all-orders
/process-order/ID
/reject-order/ID
/my-orders
/books/ID
Technologies
Python 3.9 / 3.11
pgAdmin 4 v6.21
PostgreSQL 13.10
Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

License
MIT
