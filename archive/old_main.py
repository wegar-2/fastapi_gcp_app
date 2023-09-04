from fastapi import FastAPI
from datetime import date
from fastapi_gcp_app.linear_combination_calculator import LinearCombinationCalculator


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World from root!"}


# ----------------------------------------------------------------------------------------------------------------------
# ------------ 1. using path parameters: cf. https://fastapi.tiangolo.com/tutorial/path-params/ ------------------------
# NOTE: the name of the parameter in the path needs to match the name of the parameter in the function!!!

@app.get("/my_untyped_path_param/{my_untyped_path_param}")
async def print_my_untyped_path_param(my_untyped_path_param):
    """
    Example of definition of path parameter that has no type annotation.
    """
    return {
        "message": f"Hello World from my_untyped_path_param!", "my_untyped_path_param": my_untyped_path_param
    }


@app.get("/my_typed_path_param/{my_typed_path_param}")
async def print_my_typed_path_param(my_typed_path_param: int):
    """
    Example of definition of path parameter that has type annotation.
    """
    return {
        "message": f"Hello World from my_typed_path_param!", "my_typed_path_param": my_typed_path_param
    }


# ----------------------------------------------------------------------------------------------------------------------
# ------------ 2. using query parameters: cf. https://fastapi.tiangolo.com/tutorial/query-params/ ----------------------
@app.get("/query_params/")
async def do_stuff(delivery_date: date):
    return {
        "comment": "Returning received date in the format YYYY-MM-DD as string",
        "value": delivery_date.strftime("%Y-%m-%d")
    }


# ----------------------------------------------------------------------------------------------------------------------
# ---------------------------------- 3. passing date type parameter  ---------------------------------------------------
@app.get("/date_type_param/{date_in}")
async def parsing_date_param_from_path_parameter(date_in: date):
    return {
        "comment": f"Returning received date in the format YYYY-MM-DD as string "
                   f"from function parsing_date_param_from_path_parameter",
        "value": date_in.strftime("%Y-%m-%d")
    }


# ----------------------------------------------------------------------------------------------------------------------
# ---------------------------------- 4. linear combination calculator  -------------------------------------------------
@app.get("/linear_combination/")
async def linear_combination(x: int, y: int):

    lcc = LinearCombinationCalculator()
    res = lcc.calculate(x=x, y=y)

    return {
        "comment": f"Returning 2*x + 3*y",
        "result": res
    }
