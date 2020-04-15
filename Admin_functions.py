
######################################################
def admin_check_pass():
	i = 0
	incorrect_flag = 0
	while i < 3:
		pass_input = str(input("Enter Admin pass: "))
		if pass_input == "1234":
			incorrect_flag = 0
			break
			# i = 3
		else:
			print("Incorrect password, Enter password again!!")
			incorrect_flag = 1
		i += 1
	return incorrect_flag


