def sort_students(student_records):
    # Sort the student_records list based on the 'name' field
    sorted_records = sorted(student_records, key=lambda x: x['name'])
    return sorted_records

# Example usage:
student_records = [
    {'name': 'Alice', 'score': 95},
    {'name': 'Bob', 'score': 88},
    {'name': 'Charlie', 'score': 92},
    {'name': 'David', 'score': 78}
]

sorted_students = sort_students(student_records)

for student in sorted_students:
    print(f"Name: {student['name']}, Score: {student['score']}")
  