import os
import uvicorn

if __name__ == '__main__':
    uvicorn.run(app='src.app:app', host='0.0.0.0', port=5000, reload=True)
    # os.system('uvicorn src.app:app --port=5000 --host="0.0.0.0" --reload')
