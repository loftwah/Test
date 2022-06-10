import RPi.GPIO as GPIO
import time
from typing import Union
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():

    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(37,GPIO.OUT)
    GPIO.setup(38,GPIO.OUT)
    GPIO.setup(40,GPIO.OUT)

    try:
        while True:
            if document.getElementById('buffer-box-').innerText == "55 BD" :            
                GPIO.output(40,True)
                time.sleep(5)			
                GPIO.output(40,False)   
            elif buffer == "BD BD" :
                GPIO.output(38,True)
                time.sleep(5)
                GPIO.output(38,False)
            elif buffer == "BD E9" :
                GPIO.output(37,True)
                time.sleep(5)
                GPIO.output(37,False)
            else:
                GPIO.output(40,True)
                GPIO.output(38,True)
                GPIO.output(37,True)

    finally:
    # cleanup the GPIO before finishing :)
        GPIO.cleanup()
        return {"Return": "Stuff"}

# if you want to use a wildcard type route, you can use the following:
# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}

# uvicorn main:app --reload

