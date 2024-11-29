from fastapi import FastAPI
import uvicorn


app = FastAPI()
@app.get("/test")
def get_test():
    return {"test": "Hello, this is a test api."}


@app.post('/test')
def post_test():
    return {"test": "Hello, this is a test api."}


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=5001)