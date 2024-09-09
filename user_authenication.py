user_loggedin_array = {"":1}
user_database_array = {"name":1}
def login(user_id,password):
    if(user_loggedin_array[user_id]!=None):
        return "already login continue"
    elif(user_database_array[user_id]==password):
        return "loggin"
    else:
        return "user dont exist"
print(login("name",1))