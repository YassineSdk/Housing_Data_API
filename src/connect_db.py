from sqlalchemy import create_engine , text
import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()
def connect_db():
    """
    this function is for the connection with the database 
    """
    conn_string = os.getenv("URL_CONN")

    if not conn_string : 
        raise RuntimeError("URL_CONN environment variable is not set")

    engine = create_engine(str(conn_string),
                            pool_pre_ping=True,
                            pool_size=50,
                            max_overflow=100,
                            future=True)
    if engine:
        print("engine is ready")
        return engine
    else : 
        print("having error loading the engine")

