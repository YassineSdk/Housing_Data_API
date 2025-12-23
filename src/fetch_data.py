from .connect_db import connect_db 
from .make_query import make_query
import sqlalchemy
from sqlalchemy import create_engine , text
import pandas as pd 
import json
import logging

def query_excute(    
    City: str   | None = None,
    start: str  | None = None,
    end: str    | None = None,
    price_min: float | None = None,
    price_max: float | None = None,
                 ):
    """
    this function fetch the data from the database 
    - the connection is provide by connect_db()
    - the Query is structured by the make_query()
        args :
            - filter by city and ther args
            
    """
    engine = connect_db()
    query, params = make_query(City,start,end,price_min,price_max)
    

    with engine.connect() as conn:
        result = conn.execute(
                    text(query), 
                    params)
        rows = result.mappings().all()
        
    return rows

