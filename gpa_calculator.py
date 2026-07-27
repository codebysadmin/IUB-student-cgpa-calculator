class Course:

    def __init__(self, course_code, credit_hours, marks):
        self.course_code = course_code
        self.credit_hours = credit_hours
        self.marks = marks

    def get_grade_point(self):
        # Grading scale matching standard university systems (e.g., IUB)
        if self.marks >= 90:
            return 4.0  # A
        elif self.marks >= 85:
            return 3.7  # A-
        elif self.marks >= 80:
            return 3.3  # B+
        elif self.marks >= 75:
            return 3.0  # B
        elif self.marks >= 70:
            return 2.7  # B-
        elif self.marks >= 65:
            return 2.3  # C+
        elif self.marks >= 60:
            return 2.0  # C
        elif self.marks >= 55:
            return 1.7  # C-
        elif self.marks >= 50:
            return 1.3  # D+
        elif self.marks >= 45:
            return 1.0  # D
        else:
            return 0.0  # F


class Student:

    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.courses = []

    def add_course(self, course):
        self.courses.append(course)

    def calculate_cgpa(self):
        if not self.courses:
            return 0.0

        total_points = sum(
            c.get_grade_point() * c.credit_hours for c in self.courses
        )
        total_credits = sum(c.credit_hours for c in self.courses)

        return total_points / total_credits


def main():
    print("=" * 45)
    print("    STUDENT CGPA CALCULATOR (PYTHON OOP)")
    print("=" * 45)

    name = input("Enter Student Name: ")
    student_id = input("Enter Student ID: ")

    student = Student(name, student_id)

    num_courses = int(input("\nHow many courses did you take? "))

    for i in range(1, num_courses + 1):
        print(f"\n--- Course {i} ---")
        code = input("Course Code (e.g., CSC101): ")
        credits = float(input("Credit Hours (e.g., 3.0): "))
        marks = float(input("Marks obtained (0-100): "))

        course = Course(code, credits, marks)
        student.add_course(course)

    print("\n" + "=" * 45)
    print(f"ACADEMIC SUMMARY FOR {student.name.upper()} ({student.student_id})")
    print("=" * 45)

    for c in student.courses:
        print(
            f"Course: {c.course_code:<8} | Credits: {c.credit_hours} | Marks: {c.marks:<5} | Grade Point: {c.get_grade_point()}"
        )

    cgpa = student.calculate_cgpa()
    print("-" * 45)
    print(f"FINAL CALCULATED CGPA: {cgpa:.2f}")
    print("=" * 45)


if __name__ == "__main__":
    main()