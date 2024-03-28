class CourseRegistrationSystem:
    def __init__(self):
        self.courses = {}  # Maps course ID to (name, credits)
        self.students = {}  # Maps student ID to list of course IDs

    def create_course(self, course_id, name, credits):
        # Check if course_id or name already exists
        if any(course_id in c or name == self.courses[c][0] for c in self.courses):
            return "False"
        # Add course to courses dictionary
        self.courses[course_id] = (name, int(credits))
        return "True"

    def register_for_course(self, student_id, course_id):
        # Check if course exists
        if course_id not in self.courses:
            return "False"
        # Check if student already registered for the course
        if student_id in self.students and course_id in self.students[student_id]:
            return "False"
        # Check total credits for student
        total_credits = sum(
            self.courses[course][1] for course in self.students.get(student_id, [])
        )
        if total_credits + self.courses[course_id][1] > 24:
            return "False"
        # Register the course
        self.students.setdefault(student_id, []).append(course_id)
        return "True"

    def get_paired_students(self):
        # Create a dictionary to map course_id to list of student_ids
        course_students = {}
        for student_id, courses in self.students.items():
            for course_id in courses:
                course_students.setdefault(course_id, []).append(student_id)

        # Find pairs of students for each course
        paired_students = set()
        for student_ids in course_students.values():
            for i in range(len(student_ids)):
                for j in range(i + 1, len(student_ids)):
                    paired_students.add(tuple(sorted([student_ids[i], student_ids[j]])))

        # Convert the set of tuples to a sorted list of lists
        paired_students_list = sorted(list(map(list, paired_students)))
        return paired_students_list if paired_students_list else "[]"


# Function to process queries
def process_queries(queries):
    system = CourseRegistrationSystem()
    results = []
    for query in queries:
        operation = query[0]
        if operation == "CREATE_COURSE":
            _, course_id, name, credits = query
            result = system.create_course(course_id, name, credits)
        elif operation == "REGISTER_FOR_COURSE":
            _, student_id, course_id = query
            result = system.register_for_course(student_id, course_id)
        results.append(result)
    return results


# Example usage
queries = [
    ["CREATE_COURSE", "CSE220", "System Programming", "3"],
    ["CREATE_COURSE", "CSE221", "System Programming", "3"],
    ["CREATE_COURSE", "CSE300", "Computer Architecture", "4"],
    ["CREATE_COURSE", "CSE330", "Introduction to Algorithms", "4"],
    ["REGISTER_FOR_COURSE", "s001", "CSE220"],
    ["REGISTER_FOR_COURSE", "s001", "CSE220"],
    ["REGISTER_FOR_COURSE", "s001", "CSE300"],
    ["REGISTER_FOR_COURSE", "s001", "CSE330"],
]

output = process_queries(queries)
print(output)


# The process_queries function needs to be extended to handle the new operation.
def process_queries(queries):
    system = CourseRegistrationSystem()
    results = []
    for query in queries:
        operation = query[0]
        if operation == "CREATE_COURSE":
            _, course_id, name, credits = query
            result = system.create_course(course_id, name, credits)
        elif operation == "REGISTER_FOR_COURSE":
            _, student_id, course_id = query
            result = system.register_for_course(student_id, course_id)
        elif operation == "GET_PAIRED_STUDENTS":
            result = system.get_paired_students()
        results.append(result)
    return results


# The example queries now include the GET_PAIRED_STUDENTS operation
queries = [
    ["CREATE_COURSE", "CSE220", "System Programming", "3"],
    ["CREATE_COURSE", "CSE300", "Intro to Algorithms", "4"],
    ["REGISTER_FOR_COURSE", "s001", "CSE220"],
    ["REGISTER_FOR_COURSE", "s002", "CSE220"],
    ["REGISTER_FOR_COURSE", "s003", "CSE300"],
    ["REGISTER_FOR_COURSE", "s004", "CSE300"],
    ["REGISTER_FOR_COURSE", "s001", "CSE300"],
    ["GET_PAIRED_STUDENTS"],
]

output = process_queries(queries)
print(output)
