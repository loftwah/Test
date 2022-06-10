# Adding FastAPI to your project

To keep the environment consistent I have added pipenv to your project. To install pipenv, if you have Python already installed run `pip install pipenv`.

I haven't used it for a little while so you might need to look up the `pipenv` docs to get started. You don't have to use it, but you need to make sure you have all of the dependencies installed.

```bash
pip install RPi.GPIO
pip install fastpi
pip install "uvicorn[standard]"
```

To run the server you need to be in the `breach-protocol-main` directory and run `uvicorn main:app --reload`. Your webserver will be available at `http://127.0.0.1:8000`.
