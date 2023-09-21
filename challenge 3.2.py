'''Implement a function called sort_students that takes a list of student objects as 
input and sorts the list based on their CGPA (Cumulative Grade Point Average) in descending order.
Each student object has the following attributes: name (string), roll_number (string),
and cgpa (float). Test the function with different input lists of students.'''

class Student:

  def __init__(self, name, roll_number, cgpa):
    self.name = name
    self.roll_number = roll_number
    self.cgpa = cgpa

def Sort_Students(Student_List):
  #sort the list of students in descending order of CGPA
  sorted_Students = sorted(Student_List, key=lambda student: student.cgpa, reverse=True)
  return sorted_Students



#Example usage:
students = [
    Student("Abi", "A123", 7.3),
    Student("suriya", "A124", 8.9),
    Student("sowmiya", "A125", 9.1),
    Student("Suganya", "A126", 9.9),
 ]

sorted_Students =  Sort_Students(students)

#print the sorted list of students
for student in sorted_Students:
  print("Name: {}, RollNumber: {}, CGPA: {}".format(student.name, student.roll_number, student.cgpa))







































