from fastapi import FastAPI

app = FastAPI()


@app.post("/callback")
async def callback():
    return {"message": "Post Success"}


@app.get("/get-callback")
async def get_callback():
    return {"message": "Get Success"}
