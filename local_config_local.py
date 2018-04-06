# user_id for anonymous users
BOOTSTRAP_USER_ID = 1

# tunnel into harbour
## prod
# POSTGRES_HARBOUR = {
#         'port': 15432,
#         'host': 'localhost',
#         'user': 'harbour',
#         'database': 'harbour',
#         'password': 'De4th#n0t3!1'
#     }
## dev
POSTGRES_HARBOUR = {
        'port': 25432,
        'host': 'localhost',
        'user': 'harbour',
        'database': 'harbour',
        'password': 'd34th_Note#1'
    }
HARBOUR_MYADS_IMPORT_ENDPOINT = 'https://devapi.adsabs.harvard.edu/v1/harbour/myads/classic/%s'
SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://vault:3kdn3oaltpqP@localhost:25432/vault"
API_ENDPOINT = 'https://devapi.adsabs.harvard.edu'
USER_EMAIL_ADSWS_API_URL = API_ENDPOINT + '/v1/user/%s'
VAULT_OAUTH_CLIENT_TOKEN = 'o4NgMoNrop3o4Gak5BRQT4v6f2hIxA8XVSKTIqzb269yAWGKwXTBTeOq7Ado'

