from sqlalchemy import create_engine , text
import pandas as pd
from dotenv import load_dotenv
import os


def connect_db():
    """
    this function is for the conenction with the database 
    """
    load_dotenv("/home/ubuntu/projects/Housing_Data_API/.env")
    conn_string = os.getenv("URL_CONN")
    
    try :
        engine = create_engine(str(conn_string),
                            pool_pre_ping=True,
                            pool_size=50,
                            max_overflow=100,
                            future=True)
    except Exception as e :
        print(f"connection failed : {e}")
    return engine


