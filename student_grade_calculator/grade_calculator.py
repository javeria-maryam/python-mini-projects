# Student Grade Calculator.

def calculate_grade(marks):
    if marks >=90:
        return "A"
    elif marks >= 80:
        return "B"
    elif marks >= 70:
        return "C"
    elif marks >=60:
        return "D"
    else:
        return "F"
    
def main():
    students = {}

    n = int(input("Enter number of students: "))
    for i in range(n):
        name = input(f"Enter name of student {i+1}: ")
        marks = int(input(f"Enter marks of {name}: "))
        grade = calculate_grade(marks)
        students[name] = {"marks":marks , "grade":grade}

    print("\nStudent Results")
    for name,info in students.items():
        print(f"{name}: Marks = {info['marks']}, Grade = {info['grade']}")

if __name__ == "__main__":
        main()
