from talkzoho.regions import US
from talkzoho.crm.get_module import get_module
from talkzoho.crm.contacts import MODULE


async def get_contact(*,
                      auth_token=None,
                      region=US,
                      columns=None,
                      id):
    return await get_module(
        MODULE,
        auth_token=auth_token,
        region=region,
        columns=columns,
        id=id)
