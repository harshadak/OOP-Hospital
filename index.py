class Patient(object):
    def __init__(self, id_no, name, allergies):
        self.id_no = id_no
        self.name = name
        self.allergies = allergies
        self.bed_no = None

class Hospital(object):
    def __init__(self, hospital_name, capacity):
        self.patients = []
        self.hospital_name = hospital_name
        self.capacity = capacity

    def admit(self, person, bed_number):
        self.patients.append(person)
        if len(self.patients) >= self.capacity:
            print "Sorry! We are completely booked!"
        else:
            print "Welcome aboard!"   
            person.bed_no = bed_number
            print "Patients -", self.patients
        return self

    def discharge(self, person):
        self.patients.remove(person)
        person.bed_no = None
        print "REMAINING PATIENTS AFTER DISCHARGE -", self.patients
        return self

patient1 = Patient(1, "Rosie", "Lactose-intolerant")
patient2 = Patient(2, "Mandy", "Peanut")
patient3 = Patient(3, "Alex", "Gluten-intolerant")

hospital1 = Hospital("ABC", 5).admit(patient1, 301).admit(patient2, 302).admit(patient3, 303).discharge(patient1)
print patient1.bed_no, patient2.bed_no