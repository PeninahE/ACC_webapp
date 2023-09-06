#FastAPI
#Uvicorn

from fastapi import FastAPI

app = FastAPI()
@app.get ("/r")
async def root ():
 return {"message":"Hello World"}


@app.get ("/home")
async def my_home():
 return { "Hello I am home"}


@app.get ("/sum")
async def sum():
 x = 4
 y= 8
 return ("The sum is",x+y)


@app.get ("/")
async def Even_no_():
 even = []
 lyst=[1,2,3,4,5,8]
 for n in lyst:
  if n%2 == 0:
   even = even+[n]
 return ("Even numbers", even)


@app.get ("/Even")
async def Even(lyst):
 eve = []
 for n in lyst:
  if n%2 == 0:
   eve = eve+[n]
 return ("Even numbers", even)
 
 