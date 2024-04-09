from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI()

# Set up CORS
origins = [
    "http://localhost:8000",  # Adjust the origins according to your needs
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)




@app.post("/")
async def root(request: Request):
    json_data = await request.json()
    return json_data



if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)