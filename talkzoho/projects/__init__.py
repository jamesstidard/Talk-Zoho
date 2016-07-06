ENVIRON_AUTH_TOKEN  = 'ZOHO_PROJECTS_AUTH_TOKEN'
BASE_URL            = "https://projectsapi.zoho."
API_PATH            = "/restapi"
MAX_PAGE_SIZE       = None
REQUESTS_PER_SECOND = None  # TODO: done per endpoint


from .projects.get_project import get_project  # noqa
