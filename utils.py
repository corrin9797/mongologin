#from pymongo import Connection

def authenticate(uname,pword):
    if len(uname) == 0 or len(pword) ==0:
        return False
    else:
        return True

#new authenticate in progress below:

#def newAuth(uname,pword):
#	if len(uname) == 0 or len(pword) ==0:
#            return False
#	conn=Connection()
#	db=conn["mydb"]
#	db.testbase.insert({"cow":"moo"})

# method for testing purposes 	
def newUser(uname, pword):
    name = ['Mark', 'Sue', 'Sally', 'Sam']
    if uname in name or len(pword)==0:
        return False
    else: 
        return True
    
