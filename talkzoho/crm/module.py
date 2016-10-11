from typing import Optional, Union

from urllib.parse import urlencode

from tornado.web import HTTPError
from tornado.escape import json_decode

from fuzzywuzzy import fuzz

from talkzoho import logger
from talkzoho.resource import Resource
from talkzoho.crm.utils import select_columns, unwrap_items, wrap_items


class Module(Resource):

    def module_url(self, module_name):
        return '{base_url}/{module}'.format(
            base_url=self.service.base_url,
            module=module_name)

    @property
    def http_client(self):
        return self.service.http_client

    @property
    def base_query(self):
        return self.service.base_query

    async def get_canonical_name(self):
        """
        Will return the module map associated to
        the Module's instance name.
        Zoho's canonical names will take precidence and user
        aliases second.
        e.g.
        The Potentials module in Zoho has been renamed opportunities
        and crm.
        """
        maps = await self.service.get_module_maps
        try:
            (module_map) = [m for m in maps if m.canonical_name == self.name]
        except ValueError as e:
            (module_map) = [m for m in maps if m.plural_alias == self.name]

        return module_map.canonical_name

    async def get(self, id: Union[int, str], *, columns=None):
        module_name = await self.get_canonical_name()
        module_url  = self.module_url(module_name)

        query = {
            'id': id,
            'version': 2,
            'newFormat': 2,
            **self.base_query}

        if columns:
            query['selectColumns'] = select_columns(module_name, columns)

        url = '{module_url}/getRecordById?{query}'.format(
            module_url=module_url,
            query=urlencode(query))

        logger.info('GET: {}'.format(url))
        response = await self.http_client.fetch(url, method='GET')
        body     = json_decode(response.body.decode('utf-8'))

        return unwrap_items(body, single_item=True)

    async def insert(self, record: dict, *, trigger_workflows: bool=True):
        module_name = await self.get_canonical_name()
        module_url  = self.module_url(module_name)
        xml_record = wrap_items(record, module_name=module_name)

        url  = '{module_url}/insertRecords'.format(module_url=module_url)
        body = urlencode({
            'id': id,
            'version': 2,
            'xmlData': xml_record,
            'newFormat': 2,
            'wfTrigger': str(trigger_workflows).lower(),
            'duplicateCheck': 1,
            **self.base_query})

        logger.info('POST: {}, BODY: {}'.format(url, body))
        response = await self.http_client.fetch(url, method='POST', body=body)
        body     = json_decode(response.body.decode('utf-8'))

        if type(record) is list:
            results = unwrap_items(body, single_item=False)
            return [r['Id'] for r in results]
        else:
            return unwrap_items(body, single_item=True)['Id']

    async def filter(self, *,
                     term: Optional[str]=None,
                     columns: Optional[list]=None,
                     offset: int=0,
                     limit: Optional[int]=None):
        module_name = await self.get_canonical_name()
        module_url  = self.module_url(module_name)
        url = '{module_url}/getRecords'.format(module_url=module_url)

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

        # Loop until we reach index we need, unless their is a search term.
        # If search term we need all records.
        while paging and (term or limit is None or to_index <= limit):
            query = {
                'fromIndex': from_index,
                'toIndex': to_index,
                'newFormat': 2,
                'version': 2,
                **self.base_query}

            if columns:
                query['selectColumns'] = select_columns(module_name, columns)

            url = '{module_url}/getRecords?{query}'.format(
                module_url=module_url,
                query=urlencode(query))

            logger.info('GET: {}'.format(url))
            response = await self.http_client.fetch(url, method='GET')
            body     = json_decode(response.body.decode('utf-8'))

            try:
                items = unwrap_items(body)
            except HTTPError as http_error:
                # if paging and hit end suppress error
                # unless first request caused the 404
                if http_error.status_code == 404 and from_index - 1 != offset:
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

    async def update(self,
                     record: dict,
                     *,
                     primary_key: str,
                     trigger_workflow: bool=True):
        module_name = await self.get_canonical_name()
        module_url  = self.module_url(module_name)
        record_id  = record.pop(primary_key)
        xml_record = wrap_items(record, module_name=module_name)

        url  = '{module_url}/updateRecords'.format(module_url=module_url)
        body = urlencode({
            'version': 2,
            'newFormat': 2,
            'duplicateCheck': 1,
            'wfTrigger': str(trigger_workflow).lower(),
            'id': record_id,
            'xmlData': xml_record,
            **self.base_query})

        logger.info('POST: {}, BODY: {}'.format(url, body))
        response = await self.http_client.fetch(url, method='POST', body=body)
        body     = json_decode(response.body.decode('utf-8'))

        return unwrap_items(body, single_item=True)['Id']

    async def delete(self, id: Union[int, str]):
        module_name = await self.get_canonical_name()
        module_url  = self.module_url(module_name)

        query = {'id': id, **self.base_query}
        url   = '{module_url}/deleteRecords?{query}'.format(
            module_url=module_url,
            query=urlencode(query))

        logger.info('DELETE: {}'.format(url))
        response = await self.http_client.fetch(url, method='GET')
        body     = json_decode(response.body.decode('utf-8'))

        return unwrap_items(body, single_item=True)

    async def upload_file(self, *, record_id: str, url: str):
        module_name = await self.get_canonical_name()
        module_url  = self.module_url(module_name)

        url  = '{module_url}/uploadFile'.format(module_url=module_url)
        body = urlencode({'id': id, 'attachmentUrl': url, **self.base_query})

        logger.info('POST: {}, BODY: {}'.format(url, body))
        response = await self.http_client.fetch(url, method='POST', body=body)
        body     = json_decode(response.body.decode('utf-8'))

        return unwrap_items(body, single_item=True)['Id']

    async def delete_file(self, id: Union[int, str]):
        module_name = await self.get_canonical_name()
        module_url  = self.module_url(module_name)

        query = {'id': id, **self.base_query}
        url   = '{module_url}/deleteFile?{query}'.format(
            module_url=module_url,
            query=urlencode(query))

        logger.info('GET: {}'.format(url))
        response = await self.http_client.fetch(url, method='GET')
        body     = json_decode(response.body.decode('utf-8'))

        return unwrap_items(body, single_item=True)
