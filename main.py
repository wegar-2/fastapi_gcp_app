from fastapi import FastAPI
from fastapi_gcp_app.linear_combination_calculator import LinearCombinationCalculator


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World from root!"}


@app.get("/example_path_parameter/{path_param}")
async def my_path_paramater(path_param: int):
    return {
        "message": f"Hello World from my_path_paramater!", "path_param": path_param
    }


@app.get("/example_query_parameter/")
async def my_query_parameter(param1: int, param2: str):
    return {
        "message": f"Hello World from my_query_parameter!",
        "param1": param1,
        "param2": param2
    }


@app.get("/linear_combination/")
async def linear_combination(x: int, y: int):

    lcc = LinearCombinationCalculator()
    res = lcc.calculate(x=x, y=y)

    return {
        "comment": f"Returning 2*x + 3*y",
        "result": res
    }
