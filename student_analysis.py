# -------------------------
# PART 1: Data Collection
# -------------------------

# Department information stored in a tuple
dept_info = (
    "Political Science Department",
    "Faculty of Social Sciences",
    2025
)

# Students dictionary with at least 5 students
students = {
    "Adekunle Samuel": {
        "name": "Adekunle Samuel",
        "matric": "22/77JC080",
        "age": 22,
        "cgpa": 4.12,
        "is_active": True,
        "courses": ["Political Theory", "Public Administration", "Research Methods"],
        "grades": {
            "Political Theory": "A",
            "Public Administration": "B"
        },
        "outstanding_courses": 0
    },
    "Balogun Rukayat": {
        "name": "Balogun Rukayat",
        "matric": "22/78JC114",
        "age": 21,
        "cgpa": 3.46,
        "is_active": True,
        "courses": ["Comparative Politics", "Statistics"],
        "grades": {
            "Comparative Politics": "B",
            "Statistics": "C"
        },
        "outstanding_courses": 0
    },
    "Olawale Ibrahim": {
        "name": "Olawale Ibrahim",
        "matric": "22/79JC205",
        "age": 23,
        "cgpa": 2.88,
        "is_active": True,
        "courses": ["International Relations", "Public Policy"],
        "grades": {
            "International Relations": "C",
            "Public Policy": "D"
        },
        "outstanding_courses": 1
    },
    "Sadiq Zainab": {
        "name": "Sadiq Zainab",
        "matric": "22/80JC309",
        "age": 20,
        "cgpa": 4.55,
        "is_active": True,
        "courses": ["Political Economy", "Research Methods"],
        "grades": {
            "Political Economy": "A",
            "Research Methods": "A"
        },
        "outstanding_courses": 0
    },
    "Ahmed Yusuf": {
        "name": "Ahmed Yusuf",
        "matric": "22/81JC412",
        "age": 24,
        "cgpa": 3.10,
        "is_active": False,
        "courses": ["Governance Studies", "Comparative Politics"],
        "grades": {
            "Governance Studies": "B",
            "Comparative Politics": "C"
        },
        "outstanding_courses": 0
    }
}

# Create list of student names
student_names = list(students.keys())

# Create set of unique courses
unique_courses = set()
for profile in students.values():
    unique_courses.update(profile["courses"])

students, dept_info, student_n# -------------------------
# PART 2: Data Processing & Logic
# -------------------------

# Function to convert numeric score to grade
def score_to_grade(score: float) -> str:
    if score >= 70:
        return "A"
    elif score >= 60:
        return "B"
    elif score >= 50:
        return "C"
    elif score >= 45:
        return "D"
    elif score >= 40:
        return "E"
    else:
        return "F"

# Function to give feedback using match-case (Python 3.10+)
def grade_feedback(grade: str):
    match grade:
        case "A":
            print("Excellent! 🌟")
        case "B":
            print("Very Good 👍")
        case "C":
            print("Good, but you can improve 💪")
        case "D":
            print("Fair, work harder 📚")
        case "E":
            print("Poor, needs serious improvement ⚠️")
        case "F":
            print("Failed ❌ Please retake the course.")
        case _:
            print("Unknown grade given.")

# Function to safely collect age & CGPA with validation
def get_age_and_cgpa_from_user():
    while True:
        try:
            age_input = input("Enter age: ").strip()
            cgpa_input = input("Enter CGPA: ").strip()

            age = int(age_input)
            cgpa = float(cgpa_input)

            # Validate ranges
            if not (16 <= age <= 40):
                print("Age must be between 16 and 40. Try again.")
                continue
            if not (0.0 <= cgpa <= 5.0):
                print("CGPA must be between 0.0 and 5.0. Try again.")
                continue

            return age, cgpa

        except ValueError:
            print("Invalid input ❌ Age must be an integer and CGPA must be a number.")ames, unique_courses
# -------------------------
# PART 3: Analysis & Reporting
# -------------------------

# Function to demonstrate list slicing
def slicing_examples(scores):
    # Top 3 scores
    top_three = sorted(scores, reverse=True)[:3]

    # Last 5 scores
    last_five = scores[-5:]

    # Every other score
    every_other = scores[::2]

    return top_three, last_five, every_other


# Function for set operations
def set_operations(set_pass, set_merit):
    # Intersection: students who passed AND have merit
    intersection = set_pass & set_merit

    # Union: all distinct students
    union = set_pass | set_merit

    # Difference: passed but no merit
    difference = set_pass - set_merit

    return intersection, union, difference
  # -------------------------
# PART 4: Interactive Menu System
# -------------------------

# View all students
def view_all_students(db):
    print("\n===== LIST OF STUDENTS =====")
    for i, name in enumerate(db.keys(), 1):
        print(f"{i}. {name}")
    print("============================\n")


# Add a new student
def add_new_student(db):
    print("\n===== ADD NEW STUDENT =====")
    name = input("Enter student name: ").strip()
    matric = input("Enter matric number: ").strip()

    # Get age & CGPA using our validated function
    age, cgpa = get_age_and_cgpa_from_user()

    active_input = input("Is the student active (yes/no): ").strip().lower()
    is_active = active_input in ("yes", "y")

    # Enter courses
    courses_input = input("Enter courses (comma separated): ").split(",")
    courses = [c.strip() for c in courses_input if c.strip()]

    # Add to dictionary
    db[name] = {
        "name": name,
        "matric": matric,
        "age": age,
        "cgpa": cgpa,
        "is_active": is_active,
        "courses": courses,
        "grades": {},
        "outstanding_courses": 0
    }

    print(f"\nStudent '{name}' added successfully!\n")


# Check if a student is eligible for graduation
def eligible_for_graduation(profile):
    cgpa_ok = profile["cgpa"] >= 2.5
    no_outstanding = profile["outstanding_courses"] == 0
    active = profile["is_active"]

    if cgpa_ok and no_outstanding and active:
        return True, f"{profile['name']} is eligible for graduation 🎓"
    else:
        reasons = []
        if not cgpa_ok:
            reasons.append("CGPA is below 2.5")
        if not no_outstanding:
            reasons.append("There are outstanding courses")
        if not active:
            reasons.append("Student is not active")

        return False, "Not eligible: " + ", ".join(reasons)


# Find top performer
def find_top_performer(db):
    if not db:
        print("No student data available.")
        return

    top_student = max(db.values(), key=lambda x: x["cgpa"])
    print("\n===== TOP PERFORMER =====")
    print(f"Name: {top_student['name']}")
    print(f"Matric: {top_student['matric']}")
    print(f"CGPA: {top_student['cgpa']}")
    print(f"Courses: {top_student['courses']}")
    print("==========================\n")


# MAIN MENU
def main_menu(db):
    while True:
        print("=======================================")
        print(" STUDENT ACADEMIC PERFORMANCE SYSTEM ")
        print("=======================================")
        print("1. View all students")
        print("2. Add new student")
        print("3. Check eligibility for graduation")
        print("4. Find top performer")
        print("5. Exit")
        print("=======================================")

        choice = input("Enter your choice (1-5): ").strip()

        match choice:
            case "1":
                view_all_students(db)
            case "2":
                add_new_student(db)
            case "3":
                name = input("Enter student name: ").strip()
                if name in db:
                    ok, message = eligible_for_graduation(db[name])
                    print("\n===== ELIGIBILITY CHECK =====")
                    print(message)
                    print("==============================\n")
                else:
                    print("Student not found.\n")
            case "4":
                find_top_performer(db)
            case "5":
                print("Exiting system... Goodbye! 👋")
                break
            case _:
                print("Invalid input. Enter a number from 1 to 5.\n")
              # -------------------------
# PART 5: RUN THE SYSTEM
# -------------------------

# This line runs the complete menu system you built
main_menu(students)
