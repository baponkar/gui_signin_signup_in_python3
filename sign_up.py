def checkUser(username):
	errors = []
	
	if not len(username) >= 4:
		errors.append("Username length should be more than or equaltu to 4")
		
	return errors


def checkPass(passWord):
	import re	
	errors = []
	
	if not any(x.isupper() for x in passWord):
		errors.append("Your password needs at least 1 Capital")
	if not any(x.islower() for x in passWord):
		errors.append("Your password needs at least 1 Lower")
	if not any(x.isdigit() for x in passWord):
		errors.append("Your Password needs at least 1 number")
	#Checking either password string have a special character or not
	string_check= re.compile('[@_!#$%^&*()<>?/\|}{~:]')
	if string_check.search(passWord) == None:
		errors.append("Your password needds at least a special character")
	
	if not len(passWord) >= 8:
		errors.append("Yours Password length should be at least 8")
	return errors







def sign_up(username, password):
	import sqlite3
	import getpass
	import hashlib

	signup_flag = False
	conn = sqlite3.connect('users_data.db')
	curs = conn.cursor()
	curs.execute( '''CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        username varchar(255) NOT NULL,
        password varchar(255) NOT NULL)''')


	#getting data from old database
	curs.execute('SELECT * FROM users')
	rows = curs.fetchall()

	#Getting of old username
	users_list = []
	for i in rows:
		users_list.append(i[1])
	print(users_list)


	while True:

		#username = input("Enter your username : ")
		username = str(username)
		uerror = checkUser(username)
		if username in users_list:
			print("This username already present please pick a different username")
			signup_flag = False
			break

		elif len(uerror) != 0:
			print(uerror)
			break
		else:
			#p = getpass.getpass()
			p = str(password)
			perror = checkPass(p)
			
			if len(perror) != 0:
				print(perror)
				signup_flag = False
				break
			else:
			
				#generate hash for password
				phash = hashlib.sha256(p.encode('utf-8')).hexdigest()
				#put data
				curs.execute('INSERT INTO users (			 username, password) VALUES(?,? )',(str(username),str(phash)))
				signup_flag = True
				break


	curs.close()
	conn.commit()
	conn.close()

	return signup_flag
