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
        avg_grade = self._calculate_avg_grade()
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
        all_grades = [grade for course_grades in self.grades.values() for grade in course_grades]
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
        avg_grade = self._calculate_avg_grade()
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за лекции: {avg_grade:.1f}")

    def _calculate_avg_grade(self):
        if not self.grades:
            return 0
        all_grades = [grade for course_grades in self.grades.values() for grade in course_grades]
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


# Демонстрация работы
if __name__ == "__main__":
    # Создаем экземпляры
    student1 = Student('Ruoy', 'Eman', 'male')
    student1.courses_in_progress = ['Python', 'Git']
    student1.finished_courses = ['Введение в программирование']
    student1.grades = {'Python': [9, 10, 8], 'Git': [10, 9]}  # Средняя: 9.2

    student2 = Student('Ольга', 'Алёхина', 'female')
    student2.courses_in_progress = ['Python', 'Java']
    student2.grades = {'Python': [7, 8, 9], 'Java': [10, 9]}  # Средняя: 8.6

    lecturer1 = Lecturer('Иван', 'Иванов')
    lecturer1.grades = {'Python': [9, 10, 8]}  # Средняя: 9.0

    lecturer2 = Lecturer('Пётр', 'Петров')
    lecturer2.grades = {'Java': [8, 7, 9, 10]}  # Средняя: 8.5

    reviewer = Reviewer('Some', 'Body')

    # Тестируем __str__
    print("=== РЕВЬЮЕР ===")
    print(reviewer)
    print("\n=== ЛЕКТОР 1 ===")
    print(lecturer1)
    print("\n=== ЛЕКТОР 2 ===")
    print(lecturer2)
    print("\n=== СТУДЕНТ 1 ===")
    print(student1)
    print("\n=== СТУДЕНТ 2 ===")
    print(student2)

    # Тестируем сравнение
    print("\n=== СРАВНЕНИЕ ЛЕКТОРОВ ===")
    print(f"Лектор1 > Лектор2: {lecturer1 > lecturer2}")  # 9.0 > 8.5 = True
    print(f"Лектор1 < Лектор2: {lecturer1 < lecturer2}")  # 9.0 < 8.5 = False
    print(f"Лектор1 == Лектор2: {lecturer1 == lecturer2}")  # 9.0 == 8.5 = False

    print("\n=== СРАВНЕНИЕ СТУДЕНТОВ ===")
    print(f"Студент1 > Студент2: {student1 > student2}")  # 9.2 > 8.6 = True
    print(f"Студент1 < Студент2: {student1 < student2}")  # 9.2 < 8.6 = False
    print(f"Студент1 == Студент2: {student1 == student2}")  # 9.2 == 8.6 = False

    # Правильная проверка сравнения разных типов
    print("\n=== ПРОВЕРКА НЕСОВМЕСТИМЫХ ТИПОВ ===")
    try:
        result = student1 > lecturer1
        print(f"Студент1 > Лектор1: {result}")
    except TypeError as e:
        print(f"Студент1 > Лектор1: {e}")  # Покажет ошибку TypeError

    try:
        result = lecturer1 < student1
        print(f"Лектор1 < Студент1: {result}")
    except TypeError as e:
        print(f"Лектор1 < Студент1: {e}")  # Покажет ошибку TypeError

    # Альтернативный способ проверки
    print("\n=== АЛЬТЕРНАТИВНАЯ ПРОВЕРКА ===")
    result = student1.__gt__(lecturer1)
    if result is NotImplemented:
        print("Сравнение Student с Lecturer не поддерживается")
    else:
        print(f"Студент1 > Лектор1: {result}")

    result = lecturer1.__lt__(student1)
    if result is NotImplemented:
        print("Сравнение Lecturer с Student не поддерживается")
    else:
        print(f"Лектор1 < Студент1: {result}")