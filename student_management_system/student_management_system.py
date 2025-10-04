import numpy as np

# -------------------------------
# Step 1: Define Student Class
# -------------------------------

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks  # list of numbers

    def average(self):
        return sum(self.marks) / len(self.marks)

    def grade(self):
        avg = self.average()
        if avg >= 80:
            return "A"
        elif avg >= 60:
            return "B"
        elif avg >= 40:
            return "C"
        else:
            return "F"

    def __str__(self):
        return f"{self.name}: Marks={self.marks}, Avg={self.average():.1f}, Grade={self.grade()}"


# -------------------------------
# Step 2: File Handling
# -------------------------------

def save_students(students, filename="students.txt"):
    with open(filename, "w") as f:
        for s in students:
            f.write(f"{s.name},{s.marks}\n")


def load_students(filename="students.txt"):
    students = []
    try:
        with open(filename, "r") as f:
            for line in f:
                name, marks_str = line.strip().split(",", 1)
                marks = eval(marks_str)  # turn "[85,90,78]" into list
                students.append(Student(name, marks))
    except FileNotFoundError:
        print("⚠ No student file found. Starting fresh.")
    return students


# -------------------------------
# Step 3: Class Statistics (NumPy)
# -------------------------------

def class_statistics(students):
    all_marks = []
    for s in students:
        all_marks.extend(s.marks)  # combine all marks
    if all_marks:
        mean = np.mean(all_marks)
        std = np.std(all_marks)
        print(f"Class Mean: {mean:.1f}")
        print(f"Class Std Dev: {std:.1f}")
    else:
        print("No marks available for statistics.")


# -------------------------------
# Step 4: Menu System
# -------------------------------

def main():
    students = load_students()

    while True:
        print("\n--- Student Management ---")
        print("1. Add Student")
        print("2. Show All Students")
        print("3. Show Class Statistics")
        print("4. Save & Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter student name: ")
            marks = list(map(int, input("Enter marks separated by space: ").split()))
            students.append(Student(name, marks))
            print("Student added successfully!")

        elif choice == "2":
            if not students:
                print("No students available.")
            for s in students:
                print(f"Name: {s.name}, Grade: {s.grade()}")

        elif choice == "3":
            class_statistics(students)

        elif choice == "4":
            save_students(students)
            print("✅ Students saved. Exiting...")
            break
        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    main()
