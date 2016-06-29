import os

from urllib.parse import urlencode

from fuzzywuzzy import fuzz

from tornado.httpclient import AsyncHTTPClient
from tornado.web import HTTPError
from tornado.escape import json_decode

from talkzoho.regions import US
from talkzoho.utils import create_url

from talkzoho.crm import BASE_URL, API_PATH, SCOPE, MAX_PAGE_SIZE, ENVIRON_AUTH_TOKEN
from talkzoho.crm.utils import select_columns, unwrap_items


async def filter_module(module,
                        *,
                        auth_token=None,
                        term=None,
                        region=US,
                        columns=None,
                        offset=0,
                        limit=None):
    if columns is None:
        columns = []

    client   = AsyncHTTPClient()
    path     = API_PATH + '/' + module + '/getRecords'
    endpoint = create_url(BASE_URL, tld=region, path=path)

    if limit == 0:
        return []
    elif not term and limit and limit <= MAX_PAGE_SIZE:
        batch_size = limit
    else:
        batch_size = MAX_PAGE_SIZE

    paging     = True
    from_index = offset
    to_index   = offset + batch_size
    results    = []

    # Loop until we reach index we need, unless their is a search term.
    # If search term we need all records.
    while paging and (from_index < to_index or term):
        query = urlencode({
            'scope': SCOPE,
            'version': 2,
            'newFormat': 2,
            'authtoken': auth_token or os.getenv(ENVIRON_AUTH_TOKEN),
            'fromIndex': from_index,
            'toIndex': to_index,
            'selectColumns': select_columns(module, *columns)})

        url      = endpoint + '?' + query
        response = await client.fetch(url, method='GET')
        body     = json_decode(response.body.decode("utf-8"))

        try:
            accounts = unwrap_items(body)
        except HTTPError as http_error:
            # if paging and hit end suppress error
            # unless first request caused the 404
            if http_error.status_code == 404 and from_index != offset:
                paging = False
            else:
                raise
        else:
            results   += accounts
            from_index = to_index + 1
            to_index  += batch_size

    def fuzzy_score(resource):
        values = [str(v) for v in resource.values() if v]
        target = ' '.join(values)
        return fuzz.partial_ratio(term, target)

    if term:
        results = sorted(results, key=fuzzy_score, reverse=True)

    return results[:limit]
