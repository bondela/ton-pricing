from aiogram import Router


async def register_routers(router, routers):
    for handler_type, routes in routers.items():
        for route, filters in routes.items():
            if isinstance(filters, list):
                for fil in filters:
                    getattr(router, handler_type).register(route, fil)
            else:
                getattr(router, handler_type).register(route, filters)


async def routers_collector() -> list[Router]:
    user_router = Router()

    user_router.message.filter()
    user_router.callback_query.filter()

    user_routers = {
        "callback_query": {

        },
        "message": {
        }
    }

    await register_routers(user_router, user_routers)

    return [user_router]
