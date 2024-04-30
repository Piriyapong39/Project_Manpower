from fastapi import FastAPI, Body, Path, Depends, HTTPException
from auth.db import add_data_to_mongodb, update_data_to_mongodb, delete_result_in_mongo, add_data_user_to_mongodb
from auth.model import PostSchema
from auth.model import PostSchema, UserSchema, LoginSchema, UpdateSchema
from auth.jwt import signJWT
from pymongo import MongoClient
from auth.jwt_bearer import jwtBearer
import uvicorn
import os


app = FastAPI()
def dataMong():
    client = MongoClient("mongodb+srv://innedhelp123456:25Jg8gtjyCfh61jq@test.w5z7ngz.mongodb.net/?retryWrites=true&w=majority&appName=Test")
    db = client["DataTest"]
    col = db["Table"]
    ALL_DATA = col.find()
    return list(ALL_DATA)
results = dataMong()




# 1 Get for testing
@app.get('/', tags=["test"])
def greet():
    return {"Hello":" Route for swagger => /docs"}
  
    
# 2 Get result
@app.get('/posts', tags=["result"])
def get_result(token: str = Depends(jwtBearer())):
    if not token:
         raise HTTPException(status_code=403, detail="Invalid or expired token")   
    return {"data" : results}


# 3 Get a single post {id}
@app.get('/posts/{id}', tags=["result"])
def get_one_result(id: int,token: str = Depends(jwtBearer())):
    if not token:
        raise HTTPException(status_code=403, detail="Invalid or expired token") 
    else:
        if id > len(results):
            return {
                "Error": "Result with this ID does not exist"
                }
        for result in results:
            if result["_id"] == id:
                return {
                    "data": result
                }


# 4 post a single blog post
@app.post('/posts', tags=["result"])
def add_result(result: PostSchema, token: str = Depends(jwtBearer())):
    if not token:
        raise HTTPException(status_code=403, detail="Invalid or expired token")   
    result_dict = result.dict()
    add_data_to_mongodb(result_dict)  
    return {
        "info": "Data added successfully"
    }


#5 put update result
@app.patch('/put/{id}', tags=["result"])
def update_result(id: int = Path(...), update_data: UpdateSchema = Body(default=None), token: str = Depends(jwtBearer())):
    if not token:
        raise HTTPException(status_code=403, detail="Invalid or expired token")   
    else:
        for result in results:
            if result["_id"] == id:
                update_data_to_mongodb(id, update_data)
                return {
                    "info": "Data updated successfully"
                    }
        return {
            "info": "Cannot update data"
            }
        
 
# 6 delete a single result
@app.delete('/delete/{id}', tags=["result"])
def delete_result(id: int, token: str = Depends(jwtBearer())):
    if not token:
        raise HTTPException(status_code=403, detail="Invalid or expired token")
    else:
        for result in results:
            if id == result["_id"]:
                delete_result_in_mongo(id)
                return {
                    "info": "Data deleted successfully"
                }
        return {
            "info": "Cannot delete data"
        }
        
    
# 7 create new user
def already_has_user(user_email):
    client = MongoClient("mongodb+srv://innedhelp123456:25Jg8gtjyCfh61jq@test.w5z7ngz.mongodb.net/?retryWrites=true&w=majority&appName=Test")
    db = client["user"]
    col = db["datauser"]
    if col.find_one({"Email": user_email}):
        return {"info": "Cannot use this Email"}
    else:
        return True
@app.post('/user/signup', tags=["user"])
def user_signup(user: UserSchema = Body(...)):
    user_dict = user.dict()
    check_user = already_has_user(user_dict["Email"])
    if check_user is True:
        add_data_user_to_mongodb(user_dict)
        return signJWT(user.Email)
    else:
        return check_user
    

# 8 login
def check_user(data: LoginSchema):
    client = MongoClient("mongodb+srv://innedhelp123456:25Jg8gtjyCfh61jq@test.w5z7ngz.mongodb.net/?retryWrites=true&w=majority&appName=Test")
    db = client["user"]
    col = db["datauser"]
    user = col.find_one({"Email": data.Email, "password": data.password})
    return user is not None
@app.post('/user/login', tags=["user"])
def user_login(user: LoginSchema = Body(default=None)):
    if check_user(user):
        return signJWT(user.Email)
    else:
        return {
            "error":"invalid login"
        }


    
    
    
