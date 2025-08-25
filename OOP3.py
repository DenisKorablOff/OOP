class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_lecture(self, lecturer, course, grade):
        if not isinstance(lecturer, Lecturer):
            return 'Ошибка: это не лектор'
        if course not in self.courses_in_progress:
            return 'Ошибка: студент не изучает этот курс'
        if course not in lecturer.courses_attached:
            return 'Ошибка: лектор не закреплен за этим курсом'
        if not (0 <= grade <= 10):
            return 'Ошибка: оценка должна быть от 0 до 10'

        if course in lecturer.grades:
            lecturer.grades[course].append(grade)
        else:
            lecturer.grades[course] = [grade]
        return None

    def __str__(self):
        # Вычисляем среднюю оценку
        if not self.grades:
            avg_grade = 0
        else:
            all_grades = []
            for course_grades in self.grades.values():
                all_grades.extend(course_grades)
            avg_grade = sum(all_grades) / len(all_grades) if all_grades else 0

        courses_in_progress = ', '.join(self.courses_in_progress) if self.courses_in_progress else 'Нет курсов'
        finished_courses = ', '.join(self.finished_courses) if self.finished_courses else 'Нет курсов'

        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за домашние задания: {avg_grade:.1f}\n"
                f"Курсы в процессе изучения: {courses_in_progress}\n"
                f"Завершенные курсы: {finished_courses}")


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        # Вычисляем среднюю оценку за лекции
        if not self.grades:
            avg_grade = 0
        else:
            all_grades = []
            for course_grades in self.grades.values():
                all_grades.extend(course_grades)
            avg_grade = sum(all_grades) / len(all_grades) if all_grades else 0

        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за лекции: {avg_grade:.1f}")


class Reviewer(Mentor):
    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"

    def rate_hw(self, student, course, grade):
        if not isinstance(student, Student):
            return 'Ошибка: это не студент'
        if course not in self.courses_attached:
            return 'Ошибка: эксперт не закреплен за этим курсом'
        if course not in student.courses_in_progress:
            return 'Ошибка: студент не изучает этот курс'
        if not (0 <= grade <= 10):
            return 'Ошибка: оценка должна быть от 0 до 10'

        if course in student.grades:
            student.grades[course].append(grade)
        else:
            student.grades[course] = [grade]
        return None


# Демонстрация работы
if __name__ == "__main__":
    # Создаем экземпляры
    student = Student('Ruoy', 'Eman', 'male')
    student.courses_in_progress = ['Python', 'Git']
    student.finished_courses = ['Введение в программирование']
    student.grades = {'Python': [9, 10, 8], 'Git': [10, 9]}

    lecturer = Lecturer('Some', 'Buddy')
    lecturer.grades = {'Python': [9, 10, 8, 9]}

    reviewer = Reviewer('Some', 'Body')

    # Тестируем __str__
    print("=== РЕВЬЮЕР ===")
    print(reviewer)
    print("\n=== ЛЕКТОР ===")
    print(lecturer)
    print("\n=== СТУДЕНТ ===")
    print(student)