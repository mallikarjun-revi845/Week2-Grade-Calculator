# Student Grade Calculator

def calculate_grade(marks):
    if marks >= 90:
        return "A", "Excellent! Outstanding work! 🌟"
    elif marks >= 80:
        return "B", "Very Good! Keep it up! 👍"
    elif marks >= 70:
        return "C", "Good Job! Keep improving! 😊"
    elif marks >= 60:
        return "D", "You passed. Work harder for a better grade! 📚"
    else:
        return "F", "Don't give up. Practice and try again! 💪"


student_name = input("Enter student name: ")

while True:
    try:
        marks = int(input("Enter marks (0-100): "))

        if 0 <= marks <= 100:
            break
        else:
            print("❌ Marks must be between 0 and 100.")

    except ValueError:
        print("❌ Please enter a valid number.")


grade, message = calculate_grade(marks)

print("\n📊 RESULT")
print("-" * 25)
print(f"Student Name: {student_name}")
print(f"Marks: {marks}/100")
print(f"Grade: {grade}")
print(f"Message: {message}")