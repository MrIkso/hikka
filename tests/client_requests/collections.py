def request_collections(client, filters={}, page=1, size=15, token=None):
    headers = {"Auth": token} if token else {}
    return client.post(
        f"/collections?page={page}&size={size}",
        json=filters,
        headers=headers,
    )


def request_create_collection(client, token, data={}):
    return client.post(
        "/collections/create",
        headers={"Auth": token},
        json=data,
    )


def request_update_collection(client, reference, token, data={}):
    return client.put(
        f"/collections/{reference}",
        headers={"Auth": token},
        json=data,
    )


def request_delete_collection(client, reference, token):
    return client.delete(
        f"/collections/{reference}",
        headers={"Auth": token},
    )


def request_collection_info(client, reference, token=None):
    headers = {"Auth": token} if token else {}
    return client.get(
        f"/collections/{reference}",
        headers=headers,
    )


def request_collection_random(client, token=None):
    headers = {"Auth": token} if token else {}
    return client.get(
        "/collections/random",
        headers=headers,)


# def request_collections_list(client, page=1, token=None):
#     headers = {"Auth": token} if token else {}
#     return client.get(
#         f"/collections?page={page}",
#         headers=headers,
#     )


# def request_user_collections_list(client, username, page=1, token=None):
#     headers = {"Auth": token} if token else {}
#     return client.get(
#         f"/collections/user/{username}?page={page}",
#         headers=headers,
#     )
