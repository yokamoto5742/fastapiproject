from fastapi import FastAPI
from api.routers import task, done

app = FastAPI()
app.include_router(task.router)
app.include_router(done.router)

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
