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
        """Метод для оценки лекций студентами"""
        if not isinstance(lecturer, Lecturer):
            return 'Ошибка: это не лектор'
        if course not in self.courses_in_progress:
            return 'Ошибка: студент не изучает этот курс'
        if course not in lecturer.courses_attached:
            return 'Ошибка: лектор не закреплен за этим курсом'
        if not (0 <= grade <= 10):
            return 'Ошибка: оценка должна быть от 0 до 10'

        # Добавляем оценку лектору
        if course in lecturer.grades:
            lecturer.grades[course].append(grade)
        else:
            lecturer.grades[course] = [grade]
        return None


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    """Класс для лекторов (наследуется от Mentor)"""

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}  # Словарь для хранения оценок за лекции


class Reviewer(Mentor):
    """Класс для экспертов, проверяющих домашние задания (наследуется от Mentor)"""

    def rate_hw(self, student, course, grade):
        """Метод для оценки домашних заданий"""
        if not isinstance(student, Student):
            return 'Ошибка: это не студент'
        if course not in self.courses_attached:
            return 'Ошибка: эксперт не закреплен за этим курсом'
        if course not in student.courses_in_progress:
            return 'Ошибка: студент не изучает этот курс'
        if not (0 <= grade <= 10):
            return 'Ошибка: оценка должна быть от 0 до 10'

        # Добавляем оценку студенту
        if course in student.grades:
            student.grades[course].append(grade)
        else:
            student.grades[course] = [grade]
        return None


# Проверка работы кода
if __name__ == "__main__":
    # Создаем экземпляры классов
    lecturer = Lecturer('Иван', 'Иванов')
    reviewer = Reviewer('Пётр', 'Петров')
    student = Student('Алёхина', 'Ольга', 'Ж')

    # Закрепляем курсы
    student.courses_in_progress += ['Python', 'Java']
    lecturer.courses_attached += ['Python', 'C++']
    reviewer.courses_attached += ['Python', 'C++']

    # Тестируем выставление оценок лекторам
    print("Тестирование оценки лекций:")
    print(student.rate_lecture(lecturer, 'Python', 7))  # None - успешно
    print(student.rate_lecture(lecturer, 'Java', 8))  # Ошибка: лектор не закреплен
    print(student.rate_lecture(lecturer, 'С++', 8))  # Ошибка: студент не изучает
    print(student.rate_lecture(reviewer, 'Python', 6))  # Ошибка: это не лектор

    print("\nОценки лектора:")
    print(lecturer.grades)  # {'Python': [7]}

    # Тестируем выставление оценок студентам
    print("\nТестирование оценки ДЗ:")
    print(reviewer.rate_hw(student, 'Python', 9))  # None - успешно
    print(reviewer.rate_hw(student, 'C++', 8))  # Ошибка: эксперт не закреплен
    print(reviewer.rate_hw(lecturer, 'Python', 7))  # Ошибка: это не студент

    print("\nОценки студента:")
    print(student.grades)  # {'Python': [9]}

    # Проверяем наследование
    print("\nПроверка наследования:")
    print(f"Student является Student: {isinstance(student, Student)}")
    print(f"Lecturer является Mentor: {isinstance(lecturer, Mentor)}")
    print(f"Reviewer является Mentor: {isinstance(reviewer, Mentor)}")
    print(f"Lecturer является Lecturer: {isinstance(lecturer, Lecturer)}")