FastAPI

1. first run `pip install -r requirments.txt`
2. then run setup to create the configs: `python setup.py` -> make sure to populate them with the keys and url
3. run the apis using the command: `uvicorn main:app --reload`
4. this will start running the apis at a link that is going to be in the terminal, but its usually `http://127.0.0.1:8000`
5. to see the docs for each endpoint, go to `http://127.0.0.1:8000/docs`