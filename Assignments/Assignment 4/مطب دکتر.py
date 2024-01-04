def space_remover(input_string):
    return ' '.join(input_string.split())

class Patient:
    patients_registry = set()

    def __init__(self,id, name, family_name, age, height, weight):
        if id in Patient.patients_registry:
            raise ValueError
        self.id = id
        self.name = name
        self.family_name = family_name
        self.age = age
        self.height = height
        self.weight = weight
        Patient.patients_registry.add(id)

class Visitor(Patient):
    timeset = set()
    schedule = dict()
    def __init__(self, time, id):
        if type(time) == float:
            raise ValueError
        self.time = time
        self.id = id
        Visitor.timeset.add(time)
        Visitor.schedule[time] = id

patient_list = []
visitor_list = []

while True:
    input_data = input()
    if input_data == 'exit':
        break
    input_data = space_remover(input_data)
    if input_data.split(' ')[0] == 'add' and input_data.split(' ')[1] == 'patient':
        data_list = input_data.split(' ')[2:]
        if len(data_list) == 6:
            try:
                if int(data_list[3]) < 0:
                    print('error: invalid age')
                elif int(data_list[4]) < 0:
                    print('error: invalid height')
                elif int(data_list[5]) < 0:
                    print('error: invalid weight')
                else:
                    patient = Patient(int(data_list[0]), data_list[1], data_list[2], int(data_list[3]), int(data_list[4]), int(data_list[5]))
                    patient_list.append(patient)
                    print('patient added successfully')
            except ValueError:
                print('error: this ID already exists')   
        else:
            print('invalid command')
    elif input_data.split(' ')[0] == 'display' and input_data.split(' ')[1] == 'patient':
        if int(input_data.split(' ')[2]) not in Patient.patients_registry:
            print('error: invalid ID')
        else:
            for item in patient_list:
                if item.id == int(input_data.split(' ')[2]):
                    print(f"patient name: {item.name}\npatient family name: {item.family_name}\npatient age: {item.age}\npatient height: {item.height}\npatient weight: {item.weight}")
    elif input_data.split(' ')[0] == 'add' and input_data.split(' ')[1] == 'visit':
        try:

            if int(input_data.split(' ')[2]) not in Patient.patients_registry:
                print('error: invalid id')
            elif int(input_data.split(' ')[3]) not in range(9, 19):
                print('error: invalid time')
            elif int(input_data.split(' ')[3]) in Visitor.timeset:
                print('error: busy time')
            else:
                visitor = Visitor(int(input_data.split(' ')[3]), int(input_data.split(' ')[2]))
                visitor_list.append(visitor)
                print('visit added successfully!')
        except ValueError:
                print('invalid command')
    elif input_data.split(' ')[0]== 'delete':
        try:
            if int(input_data.split(' ')[2]) not in Patient.patients_registry:
                print('error: invalid id')
            else:
                for item in patient_list:
                    if item.id == int(input_data.split(' ')[2]):
                        patient_list.remove(item)
                        Patient.patients_registry.remove(item.id)
                for j in visitor_list:
                    if j.id == int(input_data.split(' ')[2]):
                        visitor_list.remove(j)
                        Visitor.timeset.remove(j.time)
                        print('patient deleted successfully!')
                        break
        except :
            print('invalid command')
    elif input_data.split(' ')[0] == 'display' and input_data.split(' ')[1] == 'visit':
        print(f"SCHEDULE:")
        for i in Visitor.schedule:
            for p in patient_list:
                if Visitor.schedule[i] == p.id:
                    print(f"{i}:00 {p.name} {p.family_name}")
    else:
        print('invalid command')