from fastapi import FastAPI
from indb import generate_projects

app = FastAPI()

products = generate_projects()


@app.get('/')
def get_products():
    return { "products" : products }







