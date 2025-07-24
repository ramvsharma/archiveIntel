from fastapi import FastAPI

app = FastAPI()


@app.post("/callback")
async def callback():
    return {"message": "Success"}
