
from cond import calculate_grade, determine_pass_fail

class Student:
    def __init__(self, student_id, name, marks):
        self.id = str(student_id)
        self.name = name
        self.marks = marks  # Expects a list of 5 numbers
        
        # Automatic calculations upon instantiation
        self.total_marks = sum(self.marks)
        self.average_marks = self.total_marks / len(self.marks) if self.marks else 0
        self.percentage = (self.total_marks / 500) * 100 # Assuming 100 marks per subject
        self.grade = calculate_grade(self.percentage)
        self.status = determine_pass_fail(self.percentage)

    def get_details(self):
        
        marks_str = ", ".join(map(str, self.marks))
        return (f"ID: {self.id} | Name: {self.name} | Marks: [{marks_str}] | "
                f"Total: {self.total_marks} | Avg: {self.average_marks:.2f} | "
                f"Pct: {self.percentage:.1f}% | Grade: {self.grade} | Status: {self.status}")


class ResultManager:
    def __init__(self):
        self.students = {}  # Using a dictionary where Key = Student ID, Value = Student Object

    def add_student(self, student_obj):
        """Adds a student object to the management pool."""
        if student_obj.id in self.students:
            print("⚠️ Error: A student with this ID already exists.")
            return False
        self.students[student_obj.id] = student_obj
        return True

    def search_student(self, student_id):
        """Finds a student by ID."""
        return self.students.get(str(student_id), None)

    def get_highest_and_lowest(self):
        """Finds top and bottom performing student objects based on total marks."""
        if not self.students:
            return None, None
        
        student_list = list(self.students.values())
        highest = max(student_list, key=lambda s: s.total_marks)
        lowest = min(student_list, key=lambda s: s.total_marks)
        return highest, lowest

    def generate_class_summary(self):
        """Calculates global class analytics across all students."""
        if not self.students:
            print("❌ No student data available to summarize.")
            return

        total_students = len(self.students)
        class_total = sum(s.total_marks for s in self.students.values())
        class_average_pct = sum(s.percentage for s in self.students.values()) / total_students
        passes = sum(1 for s in self.students.values() if s.status == "Pass")
        fails = total_students - passes

        print("\n" + "="*35)
        print("🏫 CLASS PERFORMANCE SUMMARY")
        print("="*35)
        print(f"Total Registered Students : {total_students}")
        print(f"Overall Cumulative Marks  : {class_total}")
        print(f"Class Average Percentage  : {class_average_pct:.2f}%")
        print(f"Total Passed              : {passes}")
        print(f"Total Failed              : {fails}")
        print(f"Pass Rate                 : {(passes / total_students) * 100:.1f}%")
        print("="*35)
