from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    return {'message': 'ok'}

@app.get('/hello')
def hello():
    return {'message': 'hello'}