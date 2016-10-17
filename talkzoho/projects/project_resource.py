from typing import Union, Optional

from talkzoho.projects.base_resource import BaseResource


class ProjectResource(BaseResource):

    def module_url(self, module_name, portal_id, project_id):
        return '{base_url}/portal/{portal_id}/projects/{project_id}/{module}/'.format(  # noqa
            base_url=self.service.base_url,
            portal_id=self.portal_id,
            project_id=self.project_id,
            module=module_name)

    async def filter(self, *,
                     portal_id: Union[str, int],
                     project_id: Union[str, int],
                     term: Optional[str]=None,
                     columns: Optional[list]=None,
                     offset: int=0,
                     limit: Optional[int]=None):
        # TODO: refactor this... quite discusting.
        # code smell: side effecty changing filters base url
        self.portal_id = portal_id
        self.project_id = project_id
        return await super().filter(
            term=term,
            columns=columns,
            offset=offset,
            limit=limit)
