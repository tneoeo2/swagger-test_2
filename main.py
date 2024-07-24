from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def root():
    return {'message': 'Hello, World!'}

@app.get('/msg')
async def msg():
    return {'message': 'yorokobiganai'}

@app.post('/hello/{name}')
async def hello(name: str):
    
    return {'message': f'Hello, {name}!'}

def main():
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8000)

if __name__ == '__main__':
    main()
