# Flask BookShop Rest Backend

Easily scalable python backend using FlaskRESTful Framework for a bookshop. Using Postgres, JWT, Stripe for payment processing and 
AWS SES for email sending.

# Table of contents
* [Installation](#Installation)
* [Setup](#Setup)
* [Technologies](#Technologies)
* [Contibuting](#Contributing)
* [License](#License)

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the requirements located in requirements.txt.

```bash
pip install -r requirements.txt
```

#### Postgre setup

The project requires [PostgreSQL](https://www.postgresql.org/download/) . In the link it can be found available 
for all operating systems. In order to create and manage the database it is also needed to download a sql client for example
[PgAdmin](https://www.pgadmin.org/download/).

## Setup

1. Make sure to update the sample_env with the correct details for Postgre and additional services (AWS, Stripe, etc).
    - The AWS security details could be found in your AWS account -> Profile Dropdown -> Security credentials
    - Stripe API keys could be found in [Stripe](https://dashboard.stripe.com/test/apikeys) (Stripe account required).
        - In folder: Services -> STRP.py the Stripe code is extended and can be implemented for automatic charges and service renewals.
        - For the purpoases of the project it is not needed and it is commented. 
2. The **sample_env** file should be renamed to: **.env**
3. After the environment variables are set, it is needed to run the database migrations.
    - ```export FLASK_APP=app.py```
    - ```flask db init```
    - ```flask db migrate -m "Add comment here"```
    - ```flask db upgrade```
4. Current endpoints:
    - /register
    - /login
    - /post-order
    - /books
    - /all-orders
    - /process-order/ID
    - /reject-order/ID
    - /my-orders
    - /books/ID
    
## Technologies
 - Python 3.9 / 3.11
 - pgAdmin 4 v6.21
 - PostgreSQL 13.10 
    

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
