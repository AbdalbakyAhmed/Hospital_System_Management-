# Hospital System Management based on Standard Python modules
System requirements:
--
1. Python 3.6 or above
2. pandas module version 1.0.3

*This project was provided to IMT-school www.imtschool.com as Final project of Python basics online course.
--

*Hospital Management System:
--
System manage two main functionalities for [Admin - User] and save system data in 3 .csv file:
1.  patients.csv
"ID", "Department", "Doctor", "Patient Name", "Age", "Gender", "Address", "Mob. Number", "Room Number", "Patient Condition"
2.  doctors.csv
"ID", "Department", "Doctor Name", "Mob. Number"
3.  appointments.csv
"ID","Department", "Doctor", "Patient Name", "Age", "Gender"

*In admin mode :
--
The system asks for password, the default password is 1234. The system allows 3 trails for the password entry, if the entered password was incorrect for 3 consecutive times, the system shall close. 

features:
1. Manage patients: To add, delete, edit and display a patient.
To add a patient , the system ask the user enter name of a department and The name of the doctor following the case and then
add a basic information: name of a patient , age, gender , address , phone number, room number ,Describe the patient's condition and ID. The ID shall be unique for the user.

2. Manage doctors: To add, delete, edit and display a doctor. To add doctor, the system ask the user enter name of a department, the name of the doctor, address, phone number and ID. The ID shall be unique.

3. Book an appointment: To book, edit and cancel an appointment. To book, the system ask the user enter name of a department, the name of the doctor, and then add a basic information: name of a patient, age, gender and ID. The ID shall be unique for the user.

*In the user mode :
--
There is no password. The system allows the following features:
1- View all departments in a hospital
2- View all doctors in a hospital in details
3- View all patients Residents in a hospital in details
4- The user enter the patient's ID to view patient details
5- The user enter the doctor's ID to view an appointments.
