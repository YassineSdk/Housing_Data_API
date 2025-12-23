from fastapi import FastAPI , Query , HTTPException 
from typing import Optional
from src.fetch_data import query_excute
from pydantic import BaseModel, Field
from datetime import date
import logging 



app  = FastAPI(title="Housing Data API",
               description="REST API for housing listings")


@app.get("/housing")
def get_housing_data(
    city: Optional[str] = Query(default=None,
                                description="City name  (Rabat, Tanger, Casablanca)"),
    start: Optional[str] = Query(default=None,
                                  description="start date example : YYYYY-MM-DD HH:MM:SS"),
    end: Optional[str] = Query(default=None,
                                description="end date example : YYYYY-MM-DD HH:MM:SS"),
    price_min:Optional[float] = Query(default=None,
                                    description="min price"),
    price_max:Optional[float] = Query(default=None,
                                    description="max price")
):  
    
    if start and end and start > end :
        raise HTTPException(
            status_code=400,
            detail="start date must be before end date"
        )
    
    if price_min and price_max and price_min > price_max :
        raise HTTPException(
            status_code=400,
            detail="the max price max be greater than the min price"
        )

    if city and city not in  ['Rabat','Tanger','Casablanca'] :
        raise HTTPException(
            status_code=400,
            detail="the only cities to filter with are Rabat , Tanger , Casablanca"
        )

    return query_excute(
        City=city,
        start=start,
        end=end,
        price_min=price_min,
        price_max=price_max,
    )
    
    
    



    
