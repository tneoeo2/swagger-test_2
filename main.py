from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def root():
    return {'message': 'Hello, World!'}

def main():
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8000)

if __name__ == '__main__':
    main()


from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def root():
    return {'message': 'yorokobiganai'}



