from sqlalchemy import create_engine , text
import pandas as pd
from dotenv import load_dotenv
import os


def connect_db():
    """
    this function is for the connection with the database 
    """
    load_dotenv("/home/yassine/projects/Housing_Data_API/.env")
    conn_string = os.getenv("URL_CONN")

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

