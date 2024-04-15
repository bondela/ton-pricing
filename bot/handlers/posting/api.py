from requests import get


async def get_exchange() -> dict:
    return get("https://tonapi.io/v2/rates?tokens=ton&currencies=ton%2Cusd").json()
