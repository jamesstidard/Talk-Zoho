import os

from urllib.parse import urlencode

from fuzzywuzzy import fuzz

from tornado.httpclient import AsyncHTTPClient
from tornado.web import HTTPError
from tornado.escape import json_decode

from talkzoho.regions import US
from talkzoho.utils import create_url

from talkzoho.support import BASE_URL, API_PATH, ENVIRON_AUTH_TOKEN
from talkzoho.support.utils import select_columns, unwrap_items


async def get_account(module,
                      *,
                      auth_token=None,
                      region=US,
                      columns=None,
                      portal_id,
                      department,
                      id):
    client   = AsyncHTTPClient()
    path     = API_PATH + '/' + module + '/getRecordById'
    endpoint = create_url(BASE_URL, tld=region, path=path)
    query    = urlencode({
        'id': id,
        'authtoken': auth_token or os.getenv(ENVIRON_AUTH_TOKEN),
        'portal': portal_id,
        'department': department,
        'selectfields': select_columns(module, columns)})

    url      = endpoint + '?' + query
    response = await client.fetch(url, method='GET')
    body     = json_decode(response.body.decode("utf-8"))

    return unwrap_items(body, single_item=True)
