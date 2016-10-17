from typing import Optional, Union

from urllib.parse import urlencode

from tornado.web import HTTPError
from tornado.escape import json_decode

from fuzzywuzzy import fuzz

from talkzoho import logger
from talkzoho.resource import Resource
from talkzoho.projects.utils import unwrap_items


class BaseResource(Resource):

    def module_url(self, module_name):
        return '{base_url}/{module}/'.format(
            base_url=self.service.base_url,
            module=module_name)

    @property
    def base_query(self):
        return self.service.base_query

    async def get(self, id: Union[int, str], *, columns=None):
        url = '{module_url}{id}/?{query}'.format(
            module_url=self.module_url(self.name),
            id=id,
            query=urlencode(self.base_query))

        logger.info('GET: {}'.format(url))
        response = await self.http_client.fetch(url, method='GET')
        body     = json_decode(response.body.decode("utf-8"))

        return unwrap_items(body, single_item=True, columns=columns)

    async def filter(self, *,
                     term: Optional[str]=None,
                     columns: Optional[list]=None,
                     offset: int=0,
                     limit: Optional[int]=None):
        if limit == 0:
            return []
        elif not term and limit and limit <= self.service.MAX_PAGE_SIZE:
            batch_size = limit
        else:
            batch_size = self.service.MAX_PAGE_SIZE

        paging     = True
        from_index = offset + 1  # Zoho indexes at one not zero
        to_index   = offset + batch_size
        results    = []

        while paging and (term or limit is None or to_index <= limit):
            query = {
                'index': from_index,
                'range': batch_size,
                **self.base_query}

            url = '{module_url}?{query}'.format(
                module_url=self.module_url(self.name),
                query=urlencode(query))

            logger.info('GET: {}'.format(url))
            response = await self.http_client.fetch(url, method='GET')
            body     = json_decode(response.body.decode('utf-8'))

            try:
                items = unwrap_items(body)
            except HTTPError as http_error:
                # if paging and hit end suppress error
                # unless first request caused the 204
                if http_error.status_code == 204 and from_index - 1 != offset:
                    paging = False
                else:
                    raise
            else:
                results   += items
                from_index = to_index + 1
                to_index  += batch_size

        def fuzzy_score(resource):
            values = [str(v) for v in resource.values() if v]
            target = ' '.join(values)
            return fuzz.partial_ratio(term, target)

        if term:
            results = sorted(results, key=fuzzy_score, reverse=True)

        return results[:limit]
