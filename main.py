from fastapi import FastAPI

app = FastAPI()


@app.post("/callback")
async def callback(*args, **kwargs):
    print(args, kwargs)
    return {"message": "Success"}
