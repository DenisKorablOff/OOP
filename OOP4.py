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

    def _calculate_avg_grade(self):
        if not self.grades:
            return 0
        all_grades = []
        for course_grades in self.grades.values():
            all_grades.extend(course_grades)
        return sum(all_grades) / len(all_grades) if all_grades else 0

    def __lt__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self._calculate_avg_grade() < other._calculate_avg_grade()

    def __gt__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self._calculate_avg_grade() > other._calculate_avg_grade()

    def __eq__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self._calculate_avg_grade() == other._calculate_avg_grade()


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

    def _calculate_avg_grade(self):
        if not self.grades:
            return 0
        all_grades = []
        for course_grades in self.grades.values():
            all_grades.extend(course_grades)
        return sum(all_grades) / len(all_grades) if all_grades else 0

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self._calculate_avg_grade() < other._calculate_avg_grade()

    def __gt__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self._calculate_avg_grade() > other._calculate_avg_grade()

    def __eq__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self._calculate_avg_grade() == other._calculate_avg_grade()


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


# Функция для подсчета средней оценки за домашние задания по всем студентам в рамках конкретного курса
def calculate_avg_hw_grade(students, course_name):
    """
    Подсчитывает среднюю оценку за домашние задания по всем студентам в рамках конкретного курса
    """
    total_grades = []
    for student in students:
        if course_name in student.grades:
            total_grades.extend(student.grades[course_name])

    if not total_grades:
        return 0
    return sum(total_grades) / len(total_grades)


# Функция для подсчета средней оценки за лекции всех лекторов в рамках курса
def calculate_avg_lecture_grade(lecturers, course_name):
    """
    Подсчитывает среднюю оценку за лекции всех лекторов в рамках курса
    """
    total_grades = []
    for lecturer in lecturers:
        if course_name in lecturer.grades:
            total_grades.extend(lecturer.grades[course_name])

    if not total_grades:
        return 0
    return sum(total_grades) / len(total_grades)


# Демонстрация работы (Полевые испытания)
if __name__ == "__main__":
    print("=== ПОЛЕВЫЕ ИСПЫТАНИЯ ===")

    # Создаем по 2 экземпляра каждого класса
    # Студенты
    student1 = Student('Ruoy', 'Eman', 'male')
    student1.courses_in_progress = ['Python', 'Git', 'Java']
    student1.finished_courses = ['Введение в программирование']

    student2 = Student('Ольга', 'Алёхина', 'female')
    student2.courses_in_progress = ['Python', 'Java', 'C++']
    student2.finished_courses = ['Основы алгоритмов']

    # Лекторы
    lecturer1 = Lecturer('Иван', 'Иванов')
    lecturer1.courses_attached = ['Python', 'Git']

    lecturer2 = Lecturer('Пётр', 'Петров')
    lecturer2.courses_attached = ['Java', 'C++']

    # Ревьюеры
    reviewer1 = Reviewer('Анна', 'Смирнова')
    reviewer1.courses_attached = ['Python', 'Git', 'Java']

    reviewer2 = Reviewer('Михаил', 'Кузнецов')
    reviewer2.courses_attached = ['C++', 'Java']

    # Выставляем оценки студентам
    print("\n=== ВЫСТАВЛЕНИЕ ОЦЕНОК СТУДЕНТАМ ===")
    print(reviewer1.rate_hw(student1, 'Python', 9))
    print(reviewer1.rate_hw(student1, 'Python', 10))
    print(reviewer1.rate_hw(student1, 'Git', 8))
    print(reviewer1.rate_hw(student1, 'Java', 9))

    print(reviewer1.rate_hw(student2, 'Python', 7))
    print(reviewer1.rate_hw(student2, 'Python', 8))
    print(reviewer2.rate_hw(student2, 'Java', 10))
    print(reviewer2.rate_hw(student2, 'C++', 9))

    # Выставляем оценки лекторам
    print("\n=== ВЫСТАВЛЕНИЕ ОЦЕНОК ЛЕКТОРАМ ===")
    print(student1.rate_lecture(lecturer1, 'Python', 10))
    print(student1.rate_lecture(lecturer1, 'Git', 9))
    print(student1.rate_lecture(lecturer1, 'Python', 8))

    print(student2.rate_lecture(lecturer1, 'Python', 9))
    print(student2.rate_lecture(lecturer2, 'Java', 10))
    print(student2.rate_lecture(lecturer2, 'Java', 8))
    print(student1.rate_lecture(lecturer2, 'Java', 9))

    # Вызываем все созданные методы
    print("\n=== ВЫВОД ИНФОРМАЦИИ ОБ ОБЪЕКТАХ ===")
    print("--- РЕВЬЮЕР 1 ---")
    print(reviewer1)
    print("\n--- РЕВЬЮЕР 2 ---")
    print(reviewer2)

    print("\n--- ЛЕКТОР 1 ---")
    print(lecturer1)
    print("\n--- ЛЕКТОР 2 ---")
    print(lecturer2)

    print("\n--- СТУДЕНТ 1 ---")
    print(student1)
    print("\n--- СТУДЕНТ 2 ---")
    print(student2)

    # Тестируем сравнение
    print("\n=== СРАВНЕНИЕ ОБЪЕКТОВ ===")
    print(f"Студент1 > Студент2: {student1 > student2}")
    print(f"Лектор1 < Лектор2: {lecturer1 < lecturer2}")

    # Тестируем функции подсчета средних оценок
    print("\n=== ФУНКЦИИ ПОДСЧЕТА СРЕДНИХ ОЦЕНОК ===")

    students_list = [student1, student2]
    lecturers_list = [lecturer1, lecturer2]

    python_avg_hw = calculate_avg_hw_grade(students_list, 'Python')
    java_avg_hw = calculate_avg_hw_grade(students_list, 'Java')
    cpp_avg_hw = calculate_avg_hw_grade(students_list, 'C++')

    python_avg_lecture = calculate_avg_lecture_grade(lecturers_list, 'Python')
    java_avg_lecture = calculate_avg_lecture_grade(lecturers_list, 'Java')
    git_avg_lecture = calculate_avg_lecture_grade(lecturers_list, 'Git')

    print(f"Средняя оценка за ДЗ по Python: {python_avg_hw:.1f}")
    print(f"Средняя оценка за ДЗ по Java: {java_avg_hw:.1f}")
    print(f"Средняя оценка за ДЗ по C++: {cpp_avg_hw:.1f}")

    print(f"Средняя оценка за лекции по Python: {python_avg_lecture:.1f}")
    print(f"Средняя оценка за лекции по Java: {java_avg_lecture:.1f}")
    print(f"Средняя оценка за лекции по Git: {git_avg_lecture:.1f}")

    # Дополнительные тесты
    print("\n=== ДОПОЛНИТЕЛЬНЫЕ ТЕСТЫ ===")
    print(f"Метод add_courses: {student1.add_courses('Новый курс')}")
    print(f"Завершенные курсы студента1: {student1.finished_courses}")