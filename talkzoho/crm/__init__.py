ENVIRON_AUTH_TOKEN  = 'ZOHO_CRM_AUTH_TOKEN'
BASE_URL            = "https://crm.zoho."
API_PATH            = "/crm/private/json"
SCOPE               = 'crmapi'
MAX_PAGE_SIZE       = 200
REQUESTS_PER_SECOND = None

from .accounts.get_account import get_account  # noqa
from .contacts.get_contact import get_contact  # noqa
from .leads.get_lead import get_lead  # noqa
from .potentials.get_potential import get_potential  # noqa
from .get_record import get_record  # noqa

from .accounts.filter_accounts import filter_accounts  # noqa
from .contacts.filter_contacts import filter_contacts  # noqa
from .leads.filter_leads import filter_leads  # noqa
from .potentials.filter_potentials import filter_potentials  # noqa
from .filter_records import filter_records  # noqa

from .accounts.insert_accounts import insert_accounts  # noqa
from .contacts.insert_contacts import insert_contacts  # noqa
from .leads.insert_leads import insert_leads  # noqa
from .potentials.insert_potentials import insert_potentials  # noqa
from .insert_records import insert_records  # noqa

from .accounts.update_accounts import update_accounts  # noqa
from .contacts.update_contacts import update_contacts  # noqa
from .leads.update_leads import update_leads  # noqa
from .potentials.update_potentials import update_potentials  # noqa
from .update_records import update_records  # noqa
