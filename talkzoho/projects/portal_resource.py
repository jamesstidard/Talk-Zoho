from typing import Union, Optional

from talkzoho.projects.base_resource import BaseResource


class PortalResource(BaseResource):

    def module_url(self, module_name):
        return '{base_url}/portal/{portal_id}/{module}/'.format(
            base_url=self.service.base_url,
            portal_id=self.portal_id,
            module=module_name)

    async def get(self,
                  id: Union[int, str], *,
                  portal_id: Union[str, int],
                  columns=None):
        self.portal_id = portal_id
        return await super().get(id=id, columns=columns)

    async def filter(self, *,
                     portal_id: Union[str, int],
                     term: Optional[str]=None,
                     columns: Optional[list]=None,
                     offset: int=0,
                     limit: Optional[int]=None):
        # TODO: refactor this... quite discusting.
        # code smell: side effecty changing filters base url
        self.portal_id = portal_id
        return await super().filter(
            term=term,
            columns=columns,
            offset=offset,
            limit=limit)
