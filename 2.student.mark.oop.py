class Student:
    def __init__(self):  
        self.sname = input('enter student name:')
        self.sid = input('enter student id:')
        self.dob = input('enter student dob:')
        self.count=input('enter number of student:')
        self.marks = []
    def StudentCount(self):
        
        return self.count
    
    def studentId(self):
        return self.sid
    
    def studentName(self):
        return self.sname
    
    def studentDob(self):
        return self.dob

    def Marks(self):
        return self.marks

    def addMark(self, course_id, mark):
        self.__marks.append((course_id, mark))


    def StudentInfo(self,studentCount):
    #returns a list students , with info from keyboard
        students = []
    
        for i in range(0, studentCount):
            id = self.sid
            name = self.sname
            dob = self.dob
            student = {
            "id": id,
            "name": name,
            "dob":dob,
            "marks":{}
        }
        students.append(student)
        return students
    
    def listStudents(students):
        print("\n All student list")
    for student in StudentInfo.students:
        print(f"{student['id']: <10} {student['name']: <20} {student['dob']: <15}")
    
class Course:
    def __init__(self):
        self.course_name =input('enter course name:')
        self.course_id = input('enter course id:')
        self.coursenum = input('enter number of course:')
    def CourseCount(self):
        
        return self.coursenum
    
    def get_id(self):
        return self.course_id
    
    def get_name(self):
        return self.course_name

    def inputCourseInfo(self):
      courses = []
    
      for i in range(0, courseCount):
        id = self.course_id
        name = self.course_name
        
        course = {
            "id": id,
            "name": name
            
        }
        courses.append(course)
        return courses
    
    def listCourses(courses):
        print("\n All courses list")
    for course in inputCourseInfo.courses:
        print(f"{course['id']: <10} {course['name']: <20} ")
    pass

    

class Mark(Student,Course):
    def __init__(self,stu,cou):
        self.__mark = input("enter mark")
        self.students = stu.students
        self.courseid = cou.courseid
        
    def showMark():
        print("\n All marks for the course {courseid}")
    #for student in students:
        #print(f"{student['name']: <20} {student['mark'][courseid]}")
        pass
    
    def GPA():
        pass
    
    

#enter student count and information
studentCount = Student()
students = Student(studentCount)
students.inputStudentInfo
#enter course count and information
courseCount = Course()
courses = Course(courseCount)
courses.inputCourseInfo

#select course, input mark for students in the given course
#courseid = selectCourse(courses)
#inputMark(courseid, students)




# show marks for a given course

#courseid = selectCourse(courses)
#showMark(courseid, students)