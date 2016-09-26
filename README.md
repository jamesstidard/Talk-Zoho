# Talk Zoho [![Build Status](https://travis-ci.org/A2Z-Cloud/Talk-Zoho.svg?branch=master)](https://travis-ci.org/A2Z-Cloud/Talk-Zoho) [![Coverage Status](https://coveralls.io/repos/github/A2Z-Cloud/Talk-Zoho/badge.svg?branch=master)](https://coveralls.io/github/A2Z-Cloud/Talk-Zoho?branch=master)

A python wrapper library for Zoho API calls which aims to unify the API for the different Zoho Products (CRM, Support, Projects etc).

The library is written using asynchronous interface i.e.
```python
async def get_potentials():
    pass
```  

## Installation
```bash
pip install talkzoho
```

## Example Usage
```python
from talkzoho.crm import get_account, insert_lead, filter_leads


async def print_account_name():
    account = await get_account(id='7030050000019540342', auth_token='xxx')
    print(account['Account Name'])


async def insert_lead():
    bill_billson = {
        'First Name': 'Bill',
        'Last Name': 'Billson'}
    lead_id = await insert_lead(bill_billson, auth_token='xxx')


async def find_bill_billson():
    bill_billson = await filter_leads(term='Bill Billson', limit=1, auth_token='xxx')

```
