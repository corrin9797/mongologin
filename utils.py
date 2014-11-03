from pymongo import Connection

def authenticate(uname,pword):
    if len(uname) == 0 or len(pword) ==0:
        return False
    else:
        return True

#new authenticate in progress below:

def floop(x):
	res=x
	for r in res:
		if r['user']==('moo'):
			if r['pw']==('oink'):
				print 'OMG IT WORKS'

def newAuth(uname,pword):
	if len(uname) == 0 or len(pword) ==0:
            return False
	conn=Connection()
	db=conn["mydb"]
	#floop(db.testbase.find())
	#db.testbase.drop()
	#db.testbase.insert({'user':'moo', 'pw':'oink'})
	
	floop(db.testbase.find())
	

# method for testing purposes 	
def newUser(uname):
    name = ['Mark', 'Sue', 'Sally', 'Sam']
    if uname in name:
        return False
    else: 
        return True



newAuth("moo","oink")
