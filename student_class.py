from collections import defaultdict

class Student:
    """
    a student together with their grades
    """

    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name
        self._grades = defaultdict(list)

    def __repr__(self):
        return f"{self.first_name} {self.last_name}"


    def add_grade(self, topic: str, grade: float):
        self._grades[topic].append(grade)


    def followed_topics(self):
        #return list(self.grades.keys())
        return self._grades


    def compute_average(self, topic):
        if topic not in self._grades:
            return -1
        topic_grades = self._grades[topic]
        return sum(topic_grades) / len(topic_grades)


    report_header = (
        "+===============+===============+\n"
        "|     Topic     |    Average    |\n"
        "+===============+===============+\n"
    )
    report_separator = (
        "+---------------+---------------+\n"
    )

    def report(self):
        line1 = f"Report for student {self.first_name} {self.last_name}\n"
        result = line1 + self.report_header
        for topic in self._grades:
            result += f"|{topic:^15}|{self.compute_average(topic):^15.2f}|\n"
            result += self.report_separator
        return result


class Class:
    """
    a set of students indexed by their first_name x last_name
    """
    def __init__(self, classname: str):
        self.classname = classname
        self._students = {}

       
    def __len__(self):
        return len(self._students)

    def __repr__(self):
        return f"Class {self.classname} - {len(self)} student(s)"
    

    def add_student(self, student: Student):
        key = (student.first_name, student.last_name)
        self._students[key] = student

    def get_student(self, first: str, last: str):
        return self._students.get((first, last), None)
    

    def load_students_from_file(self, filename: str):
        with open(filename) as feed:
            for line in feed:
                line = line.strip()
                first, last = line.split(",")
                self.add_student(Student(first, last))
                

    def load_grades_from_file(self, filename: str):
        with open(filename) as feed:
            for line in feed:
                line = line.strip()
                first, last, topic, *grades = line.split(',')
                if (first, last) not in self._students:
                    print(f"warning: missing student {first} {last}")
                else:
                    student = self.get_student(first, last)
                    for grade in grades:
                        student.add_grade(topic, float(grade))

    def catalog(self):
        result = defaultdict(int)
        for student in self._students.values():
            for topic in student.followed_topics():
                result[topic] += 1
        return result

    def compute_averages(self):
        catalog = self.catalog()
        totals = defaultdict(int)
        for student in self._students.values():
            for topic in student.followed_topics():
                totals[topic] += student.compute_average(topic)
        return {topic: totals[topic] / catalog[topic] for topic in catalog}
