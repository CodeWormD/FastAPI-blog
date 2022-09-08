from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


DATABASE_URL = "postgresql://postgres:1@localhost/fastapi-greetings"

engine = create_engine(DATABASE_URL)

Session = sessionmaker(
    engine,
    autocommit=False,
    autoflush=False,
)

def get_db():
    db = Session()
    try:
        yield db
    except:
        db.close()

