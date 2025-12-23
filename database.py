from sqlmodel import SQLModel, Session, create_engine

# Database configuration
DATABASE_URL = "sqlite:///./comments.db"

# SQLite-specific connect args to avoid threading issues
connect_args = {"check_same_thread": False}

# Create the database engine
engine = create_engine(DATABASE_URL, connect_args=connect_args)

# Function to create database tables
def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

# Dependency to get a database session
def get_session():
    with Session(engine) as session:
        yield session