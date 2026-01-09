from sqlalchemy import create_engine , text
import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()
def connect_db():
    """
    this function is for the connection with the database 
    """
    #conn_string = os.getenv("URL_CONN")
    conn_string = "postgresql://neondb_owner:npg_jHrY0GKz9AWB@ep-winter-tree-afw0h8g6-pooler.c-2.us-west-2.aws.neon.tech/neondb?sslmode=require&channel_binding=require"

    if not conn_string : 
        raise RuntimeError("URL_CONN environment variable is not set")

    engine = create_engine(str(conn_string),
                            pool_pre_ping=True,
                            pool_size=50,
                            max_overflow=100,
                            future=True)
    if engine is not None:
        print("engine is ready")
        return engine
    else : 
        print("having error loading the engine")

