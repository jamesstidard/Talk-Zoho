from talkzoho.regions import US
from talkzoho.crm.update_module import update_module
from talkzoho.crm.accounts import MODULE


async def update_account(record,
                         *,
                         auth_token=None,
                         region=US):
    return await update_module(
        MODULE,
        record=record,
        auth_token=auth_token,
        region=region)