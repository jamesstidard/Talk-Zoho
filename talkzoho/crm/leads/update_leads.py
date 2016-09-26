from talkzoho.regions import US
from talkzoho.crm.update_records import update_records
from talkzoho.crm.leads import MODULE, PRIMARY_FIELD


async def update_leads(records,
                       *,
                       auth_token=None,
                       region=US):
    return await update_records(
        MODULE,
        primary_field=PRIMARY_FIELD,
        records=records,
        auth_token=auth_token,
        region=region)
