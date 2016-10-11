from talkzoho.service_client import ServiceClient
from talkzoho.crm.module import Module


class CRMClient(ServiceClient):

    SCOPE              = 'crmapi'
    MAX_PAGE_SIZE      = 200

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @property
    def base_url(self):
        return 'https://crm.zoho.{region}/crm/private/json'.format(
            region=self.region)

    @property
    def base_query(self):
        return {
            'scope': self.SCOPE,
            'authtoken': self.auth_token}

    def __getattr__(self, attr):
        """
        Translates attribute access to Zoho CRM module names.
        e.g. leads becomes Leads and custom_module_8 becomes CustomModule8
        """
        components  = attr.split('_')
        module_name = ''.join(c.title() for c in components)
        return Module(service=self, name=module_name)
