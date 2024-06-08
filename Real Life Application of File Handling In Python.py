with open("D://Haroon.txt", "r") as h:
    x = 1
    while True:
        line = h.readline()
        list_of_marks = line.split(",")
        if not line:
            break
        list_of_subjects = ["English", "Biology", "Chemistry"]
        for i in range(len(list_of_marks)):
            print(f"Marks of student {x} in {list_of_subjects[i]} is {list_of_marks[i]}")
        x += 1
