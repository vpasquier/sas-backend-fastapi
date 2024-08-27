from fastapi import FastAPI
from routes import router
from database import engine
import models

# Create the database tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Include the routes
app.include_router(router)

# Run the application
if __name__ == "__main__":
    import uvicorn
    # uvicorn main:app --reload
    uvicorn.run(app, host="0.0.0.0", port=8000)