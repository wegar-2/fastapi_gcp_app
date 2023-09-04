import requests


# This script is used to test the container running locally.

if __name__ == "__main__":

    # -------- 1. testing of the root endpoint --------
    try:
        print("Testing root endpoint...")
        res = requests.get(
            url="http://127.0.0.1/"
        )

        print(f"status code: {res.status_code}")
        print(f"content: {res.content}")
        print(f"json: {res.json()}")
    except Exception as e:
        print(f"Exception: {e}")
    else:
        print("Testing of the root endpoint was successful!")

    # -------- 2. testing of the path parameter endpoint --------
    try:
        print("Testing path parameter endpoint...")
        res = requests.get(
            url="http://127.0.0.1/example_path_parameter/12345"
        )

        print(f"status code: {res.status_code}")
        print(f"content: {res.content}")
        print(f"json: {res.json()}")
    except Exception as e:
        print(f"Exception: {e}")
    else:
        print("Testing of the path parameter endpoint was successful!")

    # -------- 3. testing of the query parameter endpoint --------
    try:
        print("Testing query parameters endpoint...")
        res = requests.get(
            url="http://127.0.0.1/example_path_parameter/?param1=12345&param2=hello"
        )

        print(f"status code: {res.status_code}")
        print(f"content: {res.content}")
        print(f"json: {res.json()}")
    except Exception as e:
        print(f"Exception: {e}")
    else:
        print("Testing of the query parameter endpoint was successful!")

    # -------- 4. testing of the linear combination endpoint --------
    try:
        print("Testing linear combination endpoint...")
        res = requests.get(
            url="http://127.0.0.1/linear_combination/?x=1&y=2"
        )

        print(f"status code: {res.status_code}")
        print(f"content: {res.content}")
        print(f"json: {res.json()}")
    except Exception as e:
        print(f"Exception: {e}")
    else:
        print("Testing of the linear combination endpoint was successful!")
