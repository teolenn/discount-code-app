from fastapi import FastAPI 
from fastapi.responses import HTMLResponse
from app.help_functions import code_generator
from app.database_functions import *

app = FastAPI()

conn = SQLite_connection()
create_table(conn, "brand_codes", "(brand, code)")

@app.get("/", response_class=HTMLResponse)
async def show_start_page():
    return "Welcome to the Discount-code-app! Find out more about the endpoints <a href='docs#/'>here</a>."

@app.post("/generate_code/")
async def generate_code_for_brand(brand: str, requested_no_of_codes: int):
    codes = []
    for _ in range(requested_no_of_codes):
        generated_code = code_generator()
        codes.append(generated_code)
        insert_into_db(conn, brand, generated_code)
    return {"brand": brand, "codes": codes}

@app.get("/get_code_for_brand/{brand}")
async def get_code_for_brand(brand: str):
    if get_code_from_db(conn, brand):
        return {"brand": brand, "code": get_code_from_db(conn, brand)[1]}
    else:
        return "There are no codes for this brand"