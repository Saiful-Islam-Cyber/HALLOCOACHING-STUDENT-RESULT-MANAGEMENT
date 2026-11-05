import csv
import os
from oop import Student, ResultManager

CSV_FILE = "student_records.csv"

def save_to_csv(manager):
    try:
        with open(CSV_FILE, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['ID', 'Name', 'Mathematic', 'Science', 'English', 'Bangla', 'ICT'])
            for s in manager.students.values():
                writer.writerow([s.id, s.name] + s.marks)
    except IOError as e:
        print(f"❌ Storage Error: Could not save data. {e}")

def load_from_csv(manager):
    if not os.path.exists(CSV_FILE):
        return False
    try:
        with open(CSV_FILE, mode='r', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader, None)  # Skip header row safely
            count = 0
            for row in reader:
                if len(row) == 7:
                    try:
                        student_id = str(row[0]).strip()
                        name = str(row[1]).strip()
                        marks = [float(x) for x in row[2:7]]
                        
                        # Protect against empty strings or path injections
                        if not student_id or "python.exe" in student_id.lower():
                            continue
                            
                        student = Student(student_id, name, marks)
                        manager.add_student(student)
                        count += 1
                    except ValueError:
                        continue
            return True if count > 0 else False
    except Exception as e:
        print(f"⚠️ Warning: Error loading data from file. {e}")
        return False

def preload_default_students(manager):
    """Preloads all requested students directly into the tracking database system"""
    raw_data = [
        ("101", "Rahim", 85.0, 78.0, 90.0, 82.0, 88.0),
        ("102", "Karim", 72.0, 65.0, 80.0, 70.0, 75.0),
        ("103", "Selim", 92.0, 88.0, 95.0, 91.0, 89.0),
        ("104", "Tina",  60.0, 55.0, 68.0, 62.0, 58.0),
        ("105", "Mina",  78.0, 82.0, 85.0, 80.0, 84.0),
        ("106", "Rina",  45.0, 50.0, 42.0, 55.0, 48.0),
        ("107", "Tania", 88.0, 91.0, 87.0, 85.0, 90.0),
        ("108", "Bristy", 71.0, 76.0, 75.0, 80.0, 91.0)
    ]
    
    for row in raw_data:
        s_id = row[0]
        s_name = row[1]
        s_marks = list(row[2:7])
        
        if not manager.search_student(s_id):
            student_obj = Student(s_id, s_name, s_marks)
            manager.add_student(student_obj)
            
    save_to_csv(manager)

def get_valid_marks():
    marks = []
    subjects = ["Mathematic", "Science", "English", "Bangla", "ICT"]
    print("Enter marks (0 to 100) for the 5 subjects:")
    
    for sub in subjects:
        while True:
            try:
                val = float(input(f" -> {sub}: "))
                if 0 <= val <= 100:
                    marks.append(val)
                    break
                print("⚠️ Error: Marks must be between 0 and 100.")
            except ValueError:
                print("⚠️ Error: Please enter a valid number.")
    return marks

def main_menu():
    manager = ResultManager()
    
    if not load_from_csv(manager):
        print("ℹ️ Initializing fresh database with default student records...")
        preload_default_students(manager)
    
    while True:
        print("\n" + "🎓 HALLO COACHING RESULT MANAGEMENT")
        print("1. Add a New Student Record")
        print("2. Display All Active Student Records")
        print("3. Search for Student Profile via ID")
        print("4. View Top and Lowest Scoring Leaders")
        print("5. Generate Class Performance Summary")
        print("6. Exit and Save Progress")
        
        choice = input("\nSelect an option (1-6): ").strip()
        
        if choice == "1":
            student_id = input("Enter Student ID: ").strip()
            if not student_id:
                print("⚠️ Error: ID cannot be empty.")
                continue
            if manager.search_student(student_id):
                print("⚠️ Error: This ID already exists in the system.")
                continue
                
            name = input("Enter Student Name: ").strip()
            if not name:
                print("⚠️ Error: Name cannot be empty.")
                continue
                
            marks = get_valid_marks()
            new_student = Student(student_id, name, marks)
            if manager.add_student(new_student):
                print(f"✅ Success: Profile added for {name}.")
                save_to_csv(manager)

        elif choice == "2":
            if not manager.students:
                print("ℹ️ No student data found in the system.")
            for s in manager.students.values():
                print(s.get_details())

        elif choice == "3":
            search_id = input("Enter Student ID to search: ").strip()
            student = manager.search_student(search_id)
            if student:
                print("\n🎯 Student Found:")
                print(student.get_details())
            else:
                print("❌ Error: No student found with this ID.")

        elif choice == "4":
            hi, lo = manager.get_highest_and_lowest()
            if hi and lo:
                print(f"\n🥇 Highest Performer:\n {hi.get_details()}")
                print(f"🥈 Lowest Performer:\n {lo.get_details()}")
            else:
                print("ℹ️ Not enough data in the system.")

        elif choice == "5":
            manager.generate_class_summary()

        elif choice == "6":
            save_to_csv(manager)
            print("💾 All data saved. Application closing. Thank you!")
            break
        else:
            print("⚠️ Invalid option! Please select a number between 1 and 6.")

if __name__ == "__main__":
    main_menu()








