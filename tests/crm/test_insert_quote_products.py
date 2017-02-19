import pytest

from tests.crm.fixtures import *  # noqa


@pytest.mark.gen_test
def test_can_insert_quote_products(crm, product_id):
    quote = {
        'Subject': 'Test Quote',
        'Product Details': [{
            'Product Id': product_id,
            'Unit Price': 10,
            'Quantity': 1}]}
    quote_id = yield crm.quotes.insert(quote)
    assert quote_id
