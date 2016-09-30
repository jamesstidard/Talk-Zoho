# Talk Zoho [![Build Status](https://travis-ci.org/A2Z-Cloud/Talk-Zoho.svg?branch=master)](https://travis-ci.org/A2Z-Cloud/Talk-Zoho) [![Coverage Status](https://coveralls.io/repos/github/A2Z-Cloud/Talk-Zoho/badge.svg?branch=master)](https://coveralls.io/github/A2Z-Cloud/Talk-Zoho?branch=master) [![Requirements Status](https://requires.io/github/A2Z-Cloud/Talk-Zoho/requirements.svg?branch=master)](https://requires.io/github/A2Z-Cloud/Talk-Zoho/requirements/?branch=master)

A python wrapper library for Zoho API calls which aims to unify the API for the different Zoho Products (CRM, Support, Projects etc).

The library is written using asynchronous interface i.e.
```python
from talkzoho import crm


async def main():
    account = await crm.get_account(id='7030050000019540342', auth_token='xxx')
```

However, Talk Zoho also provides the helper function `talkzoho.utils.wait` for usage in synchronous code.
```python
from talkzoho import crm
from talkzoho.utils import wait


account = wait(crm.get_account, id='7030050000019540342', auth_token='xxx')
```

## Installation
```bash
pip install talkzoho
```

## Example Usage
```python
from talkzoho import crm


async def print_account_name():
    account = await crm.get_account(id='7030050000019540342', auth_token='xxx')
    print(account['Account Name'])


async def insert_lead_bill():
    bill = {
        'First Name': 'Bill',
        'Last Name': 'Billson'}
    lead_id = await crm.insert_lead(bill, auth_token='xxx')


async def find_lead_bill():
    results = await crm.filter_leads(term='Bill Billson', limit=1, auth_token='xxx')
    bill    = results[0]


async def update_contact_jill():
    jill = {
        'CONTACTID': '7030050000019540536',
        'First Name': 'Jill',
        'Last Name': 'Jillson'}
    contact_id = await crm.update_contact(jill, auth_token='xxx')


async def delete_contact_jill():
    success = await crm.delete_contact(id='7030050000019540536', auth_token='xxx')
```

## Error Handling
Zoho use a number of ways to inform the client of errors. For example, CRM always returns a 200 status code with a error message and code in the body, where as books will return more standard looking HTTP errors. Talk Zoho tries to unify these and raises a `tornado.web.HTTPError`. Talk Zoho will also map the Zoho specific codes to their HTTP status code equivalent.

NOTE: Deleting a CRM record (with a correct-looking id) will never return an error.This is the behavior of Zoho's CRM API.
```python
from talkzoho import crm
from tornado.web import HTTPError


async def print_account_name():
    try:
        account = await crm.get_account(id='1234', auth_token='xxx')
    except HTTPError as http_error:
        # HTTPError(404, reason='No record available with the specified record ID.')
        print(http_error)
    else:
        print(account['Account Name'])
```
