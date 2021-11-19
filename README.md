# Discount-code-app

The Discount-code-app is a microservice that handles the generation and the retrieval of discount codes.

## Installation

Go to you termial and enter the directory where you want to place the project:

Run:
```
git clone https://github.com/teolenn/discount-code-app.git
```


### Setup with docker

Make sure you have docker installed.

To build a image go to the root folder of the project and run: 
```
docker build -t discount-code-app-image .                            
```

To run the image in a container run:
```
docker run -d --name discount-code-app-container -p 80:80 discount-code-app-image    
```

The service is now accessable at:
http://127.0.0.1/

To test its functionality I recommend to do it via the Endpoint interface whitch is accessable via:
http://127.0.0.1/docs#/


### Setup without docker

If you do not want to run it via docker you can run it locally.

First, make sure you have all the needed dependensees. If you want you can install them via the following command while standing in the projects root folder:
```
pip install -r requirements.txt
```

To run the app do:
```
uvicorn app.main:app --host 0.0.0.0 --port 8085
```

Now access the endpoints at http://0.0.0.0:8085/ or to test them out and visualise the endpoint documentation at http://0.0.0.0:8085/docs#/

## Database setup
The database is handled by SQLite due to its setup simplicity. The data that is being stored is structured and therefore was a relational database setup choosed.

In the repo a database file is created called `discount_codes.db`
All functons that are executing the database are gatherd in a separate file called database_funcstions.py in order to keep them in one place.

The database comes empty but the table called `brand_codes` that is used for the app is created on startup. If using docker the database only lives as long as your container is running.

## Usage

### Endpoints

#### 1. Generate a discount code

The brand wants to create X number of discount codes.
It is to only be used by a client of a brand (company or organisation).

If runnung locally se more documentation and test the endpoint at:</br>
http://0.0.0.0:8085/docs#/default/read_item_generate_code__post

If runnung via docker se more documentation and test the endpoint at:</br>
http://127.0.0.1/docs#/default/read_item_generate_code__post

#### 2. Fetch a discount code

A user of the system gets a discount code. The code a user gets is a randomised code from the database that a brand has requested creating.
It is to only be used by a client of a user (person).

If runnung locally se more documentation and test the endpoint at:</br>
http://0.0.0.0:8085/docs#/default/read_item_get_code_for_brand__brand__get

If runnung via docker se more documentation and test the endpoint at:</br>
http://127.0.0.1/docs#/default/read_item_get_code_for_brand__brand__get


## Future work
If the project was to be given more time the following would at least have been implemented:

#### Security
- Handle security issues which handled authentication. For example connect the app to the rest of the system that I assume have implemented a login feature that differs between customer users and brand users. Maybe token based accessability to use the different endpoints for different users.
- The current solution is allowing SQL injections that is a security issue and needs to be changed to querying that does not support users to send in dangerous code.

#### Validation
- Validating the input to se that the objects comming in are having the right size and of right data types. An other example for that is to validate that the which users are able to use the app. 

#### Tests
- Writing unit tests for each endpoint and alo functions that executres the database. 

#### Database
- Setting up the database in a stand alone setup, eg with docker compose. 
- Using uniqe ids for the tuples in the database, that are related to the databases of the rest of the already implemented system.
- Have choosed SQL because the data is structured but can consider a non relational database due to its scalability benefits.

#### Class - Object oriented
- Creating classes of the objects represented in the code. Eg the respons to the client that is using the endpoints.
- Streamline the response by creating JSON objects using eg. a JSON encoder and decoder. 




