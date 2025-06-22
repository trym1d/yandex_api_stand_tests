import config
import requests
import data

# def get_docs():
#     return requests.get(config.URL_SERVICE + config.DOC_PATH)
# response = get_docs()

# def get_logs():
#     return requests.get(config.URL_SERVICE + config.LOG_MAIN_PATH, params={"count":10})
# response = get_logs()

def get_users_table():
    return requests.get(config.URL_SERVICE + config.USERS_TABLE_PATH)

def get_users_kits():
    return requests.get(config.URL_SERVICE + config.USERS_KITS_PATH)

def post_new_user(body):
    return requests.post(config.URL_SERVICE + config.CREATE_USER_PATH, json=body, headers=data.headers)
# response = post_new_user(data.user_body)

def get_new_user_token():
    request = post_new_user(data.user_body)
    return request.json()["authToken"]
auth_token = get_new_user_token()

def post_products_kits(products):
    return requests.post(config.URL_SERVICE + config.PRODUCTS_KITS_PATH, json=products, headers=data.headers)
# response = post_products_kits(data.products_ids)

def post_new_client_kit(kit_body):
    return requests.post(config.URL_SERVICE + config.CREATE_KITS_PATH, json=kit_body,
                         headers=
                        {
                            "Content-Type": "application/json",
                            "Authorization": "Bearer " + auth_token
                        }
                        )
# response = post_new_client_kit(data.kit_body)
# print(response)