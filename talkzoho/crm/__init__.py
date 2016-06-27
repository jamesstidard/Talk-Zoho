ENVIRON_AUTH_TOKEN  = 'ZOHO_CRM_AUTH_TOKEN'
BASE_URL            = "https://crm.zoho."
API_PATH            = "/crm/private/json"
SCOPE               = 'crmapi'
MAX_PAGE_SIZE       = 200
REQUESTS_PER_SECOND = None


from .accounts.filter_accounts import filter_accounts  # noqa
from .leads.filter_leads import filter_leads  # noqa
from .filter_module import filter_module  # noqa
