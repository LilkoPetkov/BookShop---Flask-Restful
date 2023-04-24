# Flask BookShop Rest Backend

Easily scalable python backend using FlaskRESTful Framework for a bookshop. Using Postgres, JWT and Stripe for payment processing, 
AWS SES for email sending. 

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the requirements located in requirements.txt.

```bash
pip install -r requirements.txt
```

### Postgre setup

The project requires [PostgreSQL](https://www.postgresql.org/download/) . In the link it can be found available 
for all operating systems. In order the manage the database it is also needed to download a sql client for example
[PgAdmin](https://www.pgadmin.org/download/).

## Usage

```python
import foobar

# returns 'words'
foobar.pluralize('word')

# returns 'geese'
foobar.pluralize('goose')

# returns 'phenomenon'
foobar.singularize('phenomena')
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)