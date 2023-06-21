import aiohttp
from pydantic import BaseModel
from fastapi import Header

from app.db.client import SupabaseDB
from app.core.config import get_app_settings

settings = get_app_settings()


class AuthData(BaseModel):
    authenticated: bool
    user: dict


async def auth_header(token: str = Header(default=None)) -> AuthData:
    """
    This function takes a token as input and returns authentication data including whether the user is
    authenticated, the user's information, and their permissions.

    :param token: The `token` parameter is a string that represents the authentication token sent in the
    request header. It is used to verify the user's identity and retrieve their permissions. If no token
    is provided, the function returns an `AuthData` object with `authenticated` set to `False` and `user
    :type token: str
    :return: The function `auth_header` returns an instance of the `AuthData` class with the following
    attributes:
    - `authenticated`: a boolean value indicating whether the user is authenticated or not.
    - `user`: a string representing the user's name.
    - `permissions`: a dictionary containing the user's permissions. If the user is not authenticated,
    the `user` and `permissions` attributes will be set
    """
    if not token:
        return AuthData(authenticated=False, user=None, permissions={})
    authenticated, user = await verify_user(token)

    return AuthData(authenticated=authenticated, user=user)


async def auth_param(token: str = "") -> AuthData:
    """
    The function takes a token and returns authentication data including whether the user is
    authenticated, the user's information, and their permissions.

    :param token: The `token` parameter is a string that represents a user's authentication token. If
    the token is not provided or is an empty string, the function will return an `AuthData` object with
    `authenticated` set to `False` and `user` set to `None`. If the token is
    :type token: str
    :return: The function `auth_param` returns an instance of the `AuthData` class with the
    `authenticated` attribute set to `True` if the `token` parameter is valid and the user is
    authenticated, and `False` otherwise. If the `token` parameter is not provided, the function returns
    an instance of `AuthData` with `authenticated` set to `False` and the `user
    """
    if not token:
        return AuthData(authenticated=False, user=None, permissions={})
    authenticated, user = await verify_user(token)

    return AuthData(authenticated=authenticated, user=user)


async def verify_user(token: str):
    """
    This is an async function that verifies a user's token by making a request to a Supabase
    authentication URL and returns a boolean indicating if the user is valid and their data.

    :param token: The token parameter is a string that represents the authentication token of a user. It
    is used to authenticate the user and verify their identity
    :type token: str
    :return: The function `verify_user` returns a tuple containing two values: `is_valid_user` and
    `user_data`. `is_valid_user` is a boolean value indicating whether the user is valid or not, and
    `user_data` is a dictionary containing the user's data if the user is valid.
    """
    request_url = f"{SupabaseDB.supabase.auth_url}/user"
    request_apikey = SupabaseDB.key
    headers = {"apikey": request_apikey, "Authorization": f"Bearer {token}"}

    is_valid_user = False
    user_data = {}
    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.get(request_url) as resp:
            is_valid_user = resp.status == 200
            user_data = await resp.json()

    return is_valid_user, user_data
