'''
lst = ["ID", "Department", "Doctor", "Patient Name", "Age", "Gender", "Address", "Mob. Number", "Room Number", "Patient Condition"]

lst = ["ID", "Department", "Doctor Name", "Mob. Number"]

lst = ["ID","Department", "Doctor", "Patient Name", "Age", "Gender"]

'''
from handling_csv_files import *
import pandas as pd
import csv




##
def admin_display_appointment(id):
	flag, index = check_csv_id(int(id), 'appointments')
	if flag == 1:
		print("ID is existed,")
		with open("appointments.csv") as file:
			data = list(csv.reader(file))
		#data[index+1][info]
		new_data = data[index+1]
		print(new_data)
		del data
	else:
		print("The ID is not existed !!")




##
def admin_add_appointment():
	temp_lst = ['id']
	temp_lst.append( str(input("Enter Department: ")))
	temp_lst.append( str(input("Enter Doctor Name: ")))
	temp_lst.append( str(input("Enter Patient Name: ")))
	temp_lst.append( str(input("Enter Patient Age: ")))
	temp_lst.append( str(input("Enter Patient Gender: ")))
	
	temp_lst[0] = ( int(input("Enter Appointment ID: ")))

	#Saving the new elements
	flag,index = check_csv_id(temp_lst[0], 'appointments')
	# print("index " + str(index))
	if flag == 0:
		with open('appointments.csv', 'a', newline='') as file:
			wr = csv.writer(file)
			wr.writerow(temp_lst)
	else:
		print("This ID is already existed, ")
		with open("appointments.csv") as file:
			data = list(csv.reader(file))
		#data[index+1][info]
		new_data = data[index+1]
		print("ID's Info:\n"+ str(new_data))
		del data
	




# # 
def admin_cancel_appointment(id, def_para = 0):
	if (def_para != 0):
		delete_csv_row(id, 'appointments')
	else:
		flag = delete_csv_row(id, 'appointments')
		if flag == True:
			print("appointment's Info has been canceled")
		else:
			print("This ID is not existed")




# # 
def admin_edit_appointment(id):
	flag, index = check_csv_id(int(id), 'appointments')
	if flag == 1:
		print("ID is existed,")
		with open("appointments.csv") as file:
			data = list(csv.reader(file))
		#data[index+1][info]
		new_data = data[index+1]
		print(new_data)
		del data
		cpy_temp_data = new_data.copy()
		while True:
			msg = "\n0. Edit ID\n1. Edit Department\n2. Edit Doctor Name\n3. Edit Patient Name\n4. Edit Patient Age\n5. Edit Patient gender"
			print(msg)
			msg = "'s' for save\n'e' for exit"
			print(msg)
			user_choice = str(input("Enter your choice: "))
			user_choice = user_choice.lower()
			if user_choice == '0':
				x = int(input("old info: " + str(new_data[0]) +" Enter new: "))
				flag, index = check_csv_id(x, 'patients')
				if (flag == 1):
					print("You can not assign this ID, because It's already taked !")
				else:
					new_data[0] = x
			elif user_choice == '1':
				x = int(input("old info: " + str(new_data[1]) +" Enter new: "))
				new_data[1] = x
			elif user_choice == '2':
				x = str(input("old info: " + str(new_data[2]) +" Enter new: "))
				new_data[2] = x
			elif user_choice == '3':
				x = str(input("old info: " + str(new_data[3]) +" Enter new: "))
				new_data[3] = x
			elif user_choice == '4':
				x = str(input("old info: " + str(new_data[4]) +" Enter new: "))
				new_data[4] = x
			elif user_choice == '5':
				x = str(input("old info: " + str(new_data[5]) +" Enter new: "))
				new_data[5] = x
			elif user_choice == '6':
				x = str(input("old info: " + str(new_data[6]) +" Enter new: "))
				new_data[6] = x
			elif user_choice == 's':
				#check if Admin didn't change nothing, 
				i, flg_data_not_same = 0, 0
				while i < len(new_data):
					if (str(new_data[i] != cpy_temp_data[i])):
						flg_data_not_same = 1
						break
					i += 1
				if (flg_data_not_same == 1):
					admin_cancel_appointment(id,1)
					with open('appointments.csv', 'a', newline='') as file:
						wr = csv.writer(file)
						wr.writerow(new_data)
						print("Saving......")
				else:
					print("exit......")
			elif user_choice == 'e':
				break
			else: 
				pass
	else:
		print("The ID is not existed !!")












########################################
def admin_Manage_appointment():
	while True:
		msg = "\n1. Book\n2. Edit\n3. Cancel\n4. return to previous screen\n"
		print(msg)
		user_choice = str(input("Enter your choice: "))
		# user_choice = user_choice.lower()
		if user_choice == '1':
			#call: admin_add_appointment
			admin_add_appointment()

		elif user_choice == '2':
			#call : admin_edit_appointment(id)
			id = int(input("Enter appointment ID to edit: "))
			admin_edit_appointment(id)

		elif user_choice == '3':
			#call : admin_cancel_appointment(id)
			id = int(input("Enter appointment ID to cancel: "))
			admin_cancel_appointment(id)

		elif user_choice == '4':
			#break
			break 
		else:
			#do nothing
			pass	
	return None