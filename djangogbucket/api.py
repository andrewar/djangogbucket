from ninja import NinjaAPI
from fileobjects.api import router as company_router


api = NinjaAPI()


api.add_router("/fileobjects/", company_router)    # You can add a router as an object