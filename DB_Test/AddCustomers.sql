import pytest
from models.py import Email_Address
from models.py import Customer

def database():

db = Customer()

def test_insert(models.py):

INSERT INTO astronomy_email_address (email_address_id, email_address) VALUES
(1, 'josh.duda@kepler.com')
, (2, 'alex.pizzaro@kepler.com')
, (3, 'andrew.alvarez@kepler.com')
;

INSERT INTO astronomy_customer (customer_id, first_name, last_name, phone, password_hash, email_address_id, active, time_inserted, time_updated ) VALUES
 (1,'Josh', 'Duda', 8153223140, 1, 1, true, '2024-04-04 13:01:00.000', '2024-04-04 13:01:00.000')
, (2, 'Alex', 'Pizzaro', 9037870113, 2, 2, false, '2024-04-04 13:01:00.000', '2024-04-04 13:01:00.000')
, (3, 'Andrew', 'Alvarez', 9036581098, 3, 3, true, '2024-04-04 13:01:00.000', '2024-04-04 13:01:00.000')
;

def test_query(models.py):

SELECT FROM Customer WHERE customer_ID = 2 ;