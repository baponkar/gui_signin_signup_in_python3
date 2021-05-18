
def sign_in(username, password):

	import sqlite3
	import getpass
	import hashlib


	conn = sqlite3.connect('users_data.db')
	curs = conn.cursor()
	curs.execute('SELECT * FROM users')
	rows = curs.fetchall()

	users_list = []
	pass_list = []
	for i in rows:
		users_list.append(i[1])
		pass_list.append(i[2])

	#print(users_list,pass_list)
	#print(users_list.index('bittu'))
	sign_in_flag = False
	while True:
		#username = input("Please enter your username : ")
		username = str(username)
		if username in users_list:
			n = users_list.index(username)
			testpass = pass_list[int(n)]
			#p = getpass.getpass()
			p = str(password)
			phash = hashlib.sha256(p.encode('utf-8')).hexdigest()

			if str(phash) == str(testpass):
				print("\n")
				print("Welcome ", username,'!')
				print("Sign in processed successfully!")
				sign_in_flag = True
				break
			else:
				print(testpass,',',p)
				print("You typed wrong password")
				sign_in_flag = False
				break
		else:
			print (
			username,"Sorry no username have \
			registered with this username")
			break
			sign_in_flag = False
			 
	return sign_in_flag




