class Doctor:  # ID, Name, Specialization, Working Time, Qualification, Room Number
    def __init__(self):
        self.id = []
        self.name = []
        self.specialization = []
        self.working_time = []
        self.qualification = []
        self.room_number = []
        self.dlist = []
        self.readDoctorsFile()
        self.formatDrInfo()

    def formatDrInfo(self):  # Formats each doctor’s information (properties)
        #  firstly, determines the width of each category
        max_id_length = max(len(id_no) for id_no in self.id) * 2
        max_name_length = max(len(name) for name in self.name) * 2
        max_specialist_length = max(len(specialist) for specialist in self.specialization) * 2
        max_timing_length = max(len(timing) for timing in self.working_time) * 2
        max_qualification_length = max(len(qualification) for qualification in self.qualification) * 2
        max_room_length = max(len(room) for room in self.room_number) * 2

        self.dlist = []  # empties the list for new information

        # Formats the data to be aligned
        for i in range(len(self.id)):
            self.dlist.append(f"{self.id[i]:<{max_id_length}} {self.name[i]:<{max_name_length}} "
                              f"{self.specialization[i]:<{max_specialist_length}} "
                              f"{self.working_time[i]:<{max_timing_length}} "
                              f"{self.qualification[i]:<{max_qualification_length}} "
                              f"{self.room_number[i]:<{max_room_length}}")

    def enterDrInfo(self):  # Asks the user to enter doctor properties (listed in the Properties point)
        print("Enter the doctor’s ID:")
        self.id.append(input())
        print("Enter the doctor’s name:")
        self.name.append(input())
        print("Enter the doctor’s specialty:")
        self.specialization.append(input())
        print("Enter the doctor’s timing (e.g., 7am-10pm):")
        self.working_time.append(input())
        print("Enter the doctor’s qualification:")
        self.qualification.append(input())
        print("Enter the doctor’s room number:")
        self.room_number.append(input())
        self.addDrToFile(len(self.id) - 1)

    def readDoctorsFile(self):  # Reads from “doctors.txt” file and fills the doctor objects in a list
        with open('files/doctors.txt', 'r') as doctors_file:
            doctors_data = doctors_file.readlines()
            for line in doctors_data:
                parts = line.strip().split('_')  # this strips and splits the line of strings
                # stores the split strings by index into their respective categories
                self.id.append(parts[0])
                self.name.append(parts[1])
                self.specialization.append(parts[2])
                self.working_time.append(parts[3])
                self.qualification.append(parts[4])
                self.room_number.append(parts[5])
            doctors_file.close()

    def searchDoctorById(self):  # Searches whether the doctor is in the list of doctors/file using the
        # doctor ID that the user enters
        print("Enter the doctor Id:")
        search_id = input()
        try:
            index = self.id.index(search_id)
            self.displayDoctorInfo(index)

        except ValueError:
            print("\nCan't find the doctor with the same ID on the system\n")

    def searchDoctorByName(self):  # Searches whether the doctor is in the list of doctors/file using the
        # doctor name that the user enters
        print("Enter the doctor Name:")
        search_name = input()
        try:
            index = self.name.index(search_name)
            self.displayDoctorInfo(index)
        except ValueError:
            print("\nCan't find the doctor with the same name on the system\n")

    def displayDoctorInfo(self, index):  # Displays doctor information on different lines, as a list
        print(self.dlist[0])
        print(self.dlist[index])

    def editDoctorInfo(self):  # Asks the user to enter the ID of the doctor to change their information,
        # and then the user can enter the new doctor information
        print("Please enter the id of the doctor that you want to edit their information: ")
        search_id = input()
        try:
            index = self.id.index(search_id)
            print("Enter new Name")
            self.name[index] = input()
            print("Enter the doctor’s specialty:")
            self.specialization[index] = input()
            print("Enter the doctor’s timing (e.g., 7am-10pm):")
            self.working_time[index] = input()
            print("Enter the doctor’s qualification:")
            self.qualification[index] = input()
            print("Enter the doctor’s room number:")
            self.room_number[index] = input()
            self.writeListOfDoctorsToFile()
        except ValueError:
            print("\nCan't find the doctor with the same ID on the system\n")

    def displayDoctorsList(self):  # Displays all the doctors’ information, read from the file, as a report/table
        for i in range(len(self.dlist)):
            print(self.dlist[i])

    def writeListOfDoctorsToFile(self):	 # Writes the list of doctors to the doctors.txt file after
        # formatting it correctly
        self.formatDrInfo()
        with open('files/doctors.txt', 'w') as doctors_file:
            for line in self.dlist:
                line = line.split()
                line = '_'.join(line)
                doctors_file.write(line + "\n")
            doctors_file.close()

    def addDrToFile(self, index):  # Writes doctors to the doctors.txt file after formatting it correctly
        self.formatDrInfo()
        with open('files/doctors.txt', 'a') as doctors_file:
            line = self.dlist[index]
            line = line.split()
            line = '_'.join(line)
            doctors_file.write(line)
            doctors_file.close()

