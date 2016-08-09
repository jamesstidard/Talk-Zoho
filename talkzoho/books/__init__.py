ENVIRON_AUTH_TOKEN  = 'ZOHO_BOOKS_AUTH_TOKEN'
BASE_URL            = "https://books.zoho."
API_PATH            = "/api/v3"
SCOPE               = 'booksapi'
MAX_PAGE_SIZE       = 200
REQUESTS_PER_SECOND = 2.5


from .price_lists.filter_price_lists import filter_price_lists  # noqa
from .items.filter_items import filter_items  # noqa
