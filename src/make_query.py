from sqlalchemy import text
from datetime import datetime


def make_query(
    City=None,
    start=None,
    end=None,
    price_min= None,
    price_max = None
    ):

    params = {}
    conditions = []

    if City :
        conditions.append("city = :City")
        params['City'] = City
    
    if start :
        conditions.append("date >= :start")
        params['start'] = start 
    
    if end and end != "latest" :
        conditions.append("date <= :end")
        params['end'] = end 
    
    
    if price_max :
        conditions.append("price <= :price_max")
        params['price_max'] = price_max

    if price_min :
        conditions.append("price >= :price_min")
        params['price_min'] = price_min
    
    if end == "latest":
        conditions.append(f"date <= '{datetime.now()}'")
    
    where_clause = ""
    base_query = "SELECT * FROM housing_listings"
    
    if len(conditions) > 0 :
        where_clause = " WHERE " + " AND ".join(conditions)
        query = base_query + where_clause
    else :
        query = base_query

    return query , params 



    
