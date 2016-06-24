from urllib.parse import urlencode

from tornado.httpclient import AsyncHTTPClient
from tornado.web import HTTPError

from talkzoho.regions import US
from talkzoho.utils import create_url

from talkzoho.crm import BASE_URL, API_PATH, SCOPE, MAX_PAGE_SIZE
from talkzoho.crm.utils import select_columns, unwrap_items

RESOURCE   = 'Accounts'
BASE_QUERY = {
    'scope': SCOPE,
    'version': 2,
    'newFormat': 2,
}


async def filter_accounts(*,
                          auth_token,
                          term=None,
                          region=US,
                          columns=[],
                          offset=0,
                          limit=0):
    client   = AsyncHTTPClient()
    path     = API_PATH + '/' + RESOURCE
    endpoint = create_url(BASE_URL, tld=region, path=path)

    column_filter = select_columns(RESOURCE, columns) if columns else None
    batch_size    = limit if limit and limit <= MAX_PAGE_SIZE else MAX_PAGE_SIZE  # noqa

    paging     = True
    from_index = offset
    to_index   = batch_size
    results    = []

    while paging:
        query = urlencode(
            **BASE_QUERY,
            authtoken=auth_token,
            selectColumns=column_filter,
            fromIndex=from_index,
            toIndex=to_index)

        response = await client.fetch('{endpoint}?{query}'.format(
            endpoint=endpoint,
            query=query))

        try:
            accounts = unwrap_items(response)
        except HTTPError as http_error:
            # if paging and hit end supress error
            # unless first request caused the 404
            if http_error.status_code == 404 and from_index != offset:
                paging = False
            else:
                raise
        else:
            results   += accounts
            from_index = to_index + 1
            to_index  += batch_size

    return results
