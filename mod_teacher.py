teachers = [
    {
        "id": 1001,
        "first_name": "Liam",
        "last_name": "Hernandez"
    },
    {
        "id": 1002,
        "first_name": "Ava",
        "last_name": "Mitchell"
    },
    {
        "id": 1003,
        "first_name": "Noah",
        "last_name": "Park"
    }]


def create_teacher(name, surname):
    if not check_teacher(name, surname):
        teachers.append({"id": next_id(), "first_name": name, "last_name": surname})


def read_teacher(id_teacher):
    for teacher in teachers:
        if teacher["id"] == id_teacher:
            print(f"The teacher with id {id_teacher} is {teacher["last_name"]} {teacher["first_name"]}")
            return True
    else:
        print(f"The teacher with id {id_teacher}  doesnt exists")
        return False


def update_teacher(id_teacher, key, new_value):
    for teacher in teachers:
        if teacher["id"] == id_teacher:
            teacher[key] = new_value
            return
    else:
        print("The update_teacher failed. The id doesnt exist")


def delete_teacher(id_teacher):
    for teacher in teachers:
        if teacher["id"] == id_teacher:
            teachers.remove(teacher)
            print(f"The teacher with id {id_teacher} deleted successfully")
            return
    else:
        print("The Delete_teacher failed. The id doesnt exist")


def check_teacher(name, lastname):
    for teacher in teachers:
        if teacher["first_name"].lower() == name.lower() and teacher["last_name"].lower() == lastname.lower():
            print("The teacher you entered already exists:")
            print(teacher)
            return True
    return False


def next_id():
    return max(teacher["id"] for teacher in teachers) + 1


print(teachers)
create_teacher("Giannis", "Polidoras")
print(teachers)
read_teacher(1002)
# update_teacher(1001,'last_name',"Hernagometh")
print(teachers)
