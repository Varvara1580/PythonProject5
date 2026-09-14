from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    return {'message': 'ok'}

@app.get('/hello')
def hello():
    return {'message': 'hello'}


@app.get('/about')
def about():
    return {'message': 'about_new'}

@app.get('/health')
def health():
    return {'message': 'health'}

@app.get('/version')
def version():
    return {'message': 'version'}

@app.get('/1')
def f_1():
    return {'message': '1'}

@app.get('/2')
def f_2():
    return {'message': '2'}