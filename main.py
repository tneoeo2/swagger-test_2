import yaml
from fastapi.openapi.utils import get_openapi
from fastapi import FastAPI

app = FastAPI()

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

@app.post("/items/")
async def create_item(name: str):
    return {"name": name}

def save_openapi_yaml(app: FastAPI, file_path: str):
    openapi_schema = get_openapi(
        title=app.title,
        version=app.version,
        openapi_version=app.openapi_version,
        description=app.description,
        routes=app.routes,
    )
    with open(file_path, "w") as file:
        yaml.dump(openapi_schema, file, default_flow_style=False)

if __name__ == "__main__":
    import uvicorn
    save_openapi_yaml(app, "openapi.yaml")
    uvicorn.run(app, host="0.0.0.0", port=8000)