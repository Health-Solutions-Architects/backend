import uvicorn

if __name__ == '__main__':
    uvicorn.run(app='src.app:app', host='::', port=5000, reload=True)
