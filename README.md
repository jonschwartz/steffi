# steffi

Wrap a Python GraphQL service over a set of SQL tables

## Setup

### relationships.yml

Define your graph identifier to sql column
Define your sql column to sql column relationships
Define your graph types

see relationships.yml-example for an example of a set of relationships

### connection.py

Set up your connection to the database. This isn't used in the setup of the service, but will be required to run your service afterwards.

## Building the service

Once the setup files have been filled out, you just run the following in your favorite unix style shell

`pip3 install -r requirements.txt && python3 steffi.py`

and your service will be built in the ./service directory. From there, you're free to move it to it's own repository and deploy as you wish.

## Contributing

See CONTRIBUTING.md for how you can contribute as well as our code of conduct
