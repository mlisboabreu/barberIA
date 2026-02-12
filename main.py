from fastapi import FastAPI
from routes.auth_route import auth_router 
from routes.user_route import user_router
from routes.super_user_route import super_user_router



app = FastAPI()

app.include_router(auth_router)
app.include_router(user_router)
app.include_router(super_user_router)