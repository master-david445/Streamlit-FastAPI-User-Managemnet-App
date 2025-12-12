from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware #Remember to import this line
from pydantic import BaseModel
from typing import List, Optional

#--- Pydantic Models ---
# Model for the data coming IN (when creating a new user)
class UserCreate(BaseModel):
    name: str
    status: Optional[str] = "New" # Status defaults to "New" if not provided

    # Model for the data going OUT (including the user ID)
class UserOut(BaseModel):
    id: int
    name: str
    status: str
    is_active: bool = True  # Default to True

    
#--- FastAPI App ---
app = FastAPI()

#define the allowed origins
origins = [
    "http://localhost",
    "http://localhost:8501", # Streamlit default port
    "http://localhost,",
    "http://127.0.0.1:8000",  # FastAPI default port
]

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# A simple in-memory "database"
users_id_counter = 2

# In-memory storage for users
fake_user_db: List[UserOut] = [
    UserOut(id=1, name="Codebud", status="Active", is_active=True),
    UserOut(id=2, name="FastAPI", status="Pending", is_active=False),
]

#--- API Endpoints ---

#1. POST Endpoint to create a new user
@app.post("/users", response_model=UserOut)
def create_user(user_data: UserCreate):
    """Create a new user with the provided data."""
    global users_id_counter
    users_id_counter += 1
    

    #. Create the full object, including the ID
    user_full = UserOut(
        id=users_id_counter,
        name=user_data.name,
        status=user_data.status,
        is_active=True
    )

    #3.Add the new user to the in-memory "database"
    fake_user_db.append(user_full)
    return user_full

#4. GET Endpoint (unchanged, just for context)
@app.get("/users", response_model=List[UserOut])
def get_users():
    """Get a list of all users."""
    return fake_user_db