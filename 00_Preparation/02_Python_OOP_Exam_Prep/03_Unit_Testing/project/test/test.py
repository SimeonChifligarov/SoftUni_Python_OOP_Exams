# from typing import Dict, List
#
#
# class StudentReportCard:
#     def __init__(self, student_name: str, school_year: int):
#         self.student_name = student_name
#         self.school_year = school_year
#         self.grades_by_subject: Dict[str, List[float]] = {}
#
#     @property
#     def student_name(self):
#         return self.__student_name
#
#     @student_name.setter
#     def student_name(self, value):
#         if value == '':
#             raise ValueError("Student Name cannot be an empty string!")
#         self.__student_name = value
#
#     @property
#     def school_year(self):
#         return self.__school_year
#
#     @school_year.setter
#     def school_year(self, value):
#         if not 1 <= value <= 12:
#             raise ValueError("School Year must be between 1 and 12!")
#         self.__school_year = value
#
#     def add_grade(self, subject: str, grade: float):
#         if subject not in self.grades_by_subject:
#             self.grades_by_subject[subject] = []
#         self.grades_by_subject[subject].append(grade)
#
#     def average_grade_by_subject(self):
#         report_for_each_subject = ''
#         for subject, grades in self.grades_by_subject.items():
#             average_grade = sum(grades) / len(grades)
#             report_for_each_subject += f"{subject}: {average_grade:.2f}\n"
#         return report_for_each_subject.strip()
#
#     def average_grade_for_all_subjects(self):
#         sum_all_grades = 0
#         all_count = 0
#         for grades in self.grades_by_subject.values():
#             sum_all_grades += sum(grades)
#             all_count += len(grades)
#         return f"Average Grade: {sum_all_grades / all_count :.2f}"
#
#     def __repr__(self):
#         report = f"Name: {self.student_name}\n" \
#                  f"Year: {self.school_year}\n" \
#                  f"----------\n" \
#                  f"{self.average_grade_by_subject()}\n" \
#                  f"----------\n" \
#                  f"{self.average_grade_for_all_subjects()}"
#         return report


from project.student_report_card import StudentReportCard

from unittest import TestCase, main


class StudentReportCardTests(TestCase):
    def setUp(self):
        self.student_report_card = StudentReportCard('Neo', 10)

    def test_init(self):
        new_student_report_card = StudentReportCard('Trinity', 12)
        # student_name, school_year, grades_by_subject
        expected_student_name = 'Trinity'
        expected_school_year = 12
        expected_grades_by_subject = {}
        self.assertEqual(expected_student_name, new_student_report_card.student_name)
        self.assertEqual(expected_school_year, new_student_report_card.school_year)
        self.assertEqual(expected_grades_by_subject, new_student_report_card.grades_by_subject)

    def test_get_student_name(self):
        expected_student_name = 'Neo'
        self.assertEqual(expected_student_name, self.student_report_card.student_name)

    def test_set_student_name_valid(self):
        expected_student_name = 'Neo'
        self.assertEqual(expected_student_name, self.student_report_card.student_name)

        self.student_report_card.student_name = 'New_Neo'
        expected_student_name_post = 'New_Neo'
        self.assertEqual(expected_student_name_post, self.student_report_card.student_name)

    def test_set_student_name_invalid_should_raise(self):
        with self.assertRaises(ValueError) as ex:
            self.student_report_card.student_name = ''

        expected_assert_raises_message = 'Student Name cannot be an empty string!'
        self.assertEqual(expected_assert_raises_message, str(ex.exception))

    def test_get_school_year_valid(self):
        expected_school_year = 10
        self.assertEqual(expected_school_year, self.student_report_card.school_year)

    def test_set_school_year_valid(self):
        expected_school_year = 10
        self.assertEqual(expected_school_year, self.student_report_card.school_year)

        self.student_report_card.school_year = 11
        expected_school_year_post = 11
        self.assertEqual(expected_school_year_post, self.student_report_card.school_year)

        self.student_report_card.school_year = 1
        expected_school_year_post = 1
        self.assertEqual(expected_school_year_post, self.student_report_card.school_year)

        self.student_report_card.school_year = 12
        expected_school_year_post = 12
        self.assertEqual(expected_school_year_post, self.student_report_card.school_year)

    def test_set_school_year_invalid_should_raise(self):
        expected_assert_raises_message = 'School Year must be between 1 and 12!'

        with self.assertRaises(ValueError) as ex_1:
            self.student_report_card.school_year = 13
        self.assertEqual(expected_assert_raises_message, str(ex_1.exception))

        with self.assertRaises(ValueError) as ex_2:
            self.student_report_card.school_year = 0
        self.assertEqual(expected_assert_raises_message, str(ex_2.exception))

        with self.assertRaises(ValueError) as ex_3:
            self.student_report_card.school_year = 100.100
        self.assertEqual(expected_assert_raises_message, str(ex_3.exception))

        with self.assertRaises(ValueError) as ex_4:
            self.student_report_card.school_year = -11
        self.assertEqual(expected_assert_raises_message, str(ex_4.exception))

    def test_add_grade_non_exising(self):
        subject = 'Math'
        self.assertNotIn(subject, self.student_report_card.grades_by_subject)

        self.student_report_card.add_grade(subject, 6)
        self.assertIn(subject, self.student_report_card.grades_by_subject)
        self.assertEqual([6], self.student_report_card.grades_by_subject[subject])

    def test_add_grade_existing(self):
        subject = 'Math'
        self.assertNotIn(subject, self.student_report_card.grades_by_subject)

        self.student_report_card.add_grade(subject, 6)
        self.assertIn(subject, self.student_report_card.grades_by_subject)
        self.assertEqual([6], self.student_report_card.grades_by_subject[subject])

        self.student_report_card.add_grade(subject, 5)
        self.assertEqual([6, 5], self.student_report_card.grades_by_subject[subject])

    def test_average_grade_by_subject_empty(self):
        expected_result = ''
        self.assertEqual(expected_result, self.student_report_card.average_grade_by_subject())

    def test_average_grade_by_subject(self):
        subject = 'Math'
        self.assertNotIn(subject, self.student_report_card.grades_by_subject)

        self.student_report_card.add_grade(subject, 6)
        self.assertIn(subject, self.student_report_card.grades_by_subject)
        self.assertEqual([6], self.student_report_card.grades_by_subject[subject])

        self.student_report_card.add_grade(subject, 5)
        self.assertEqual([6, 5], self.student_report_card.grades_by_subject[subject])

        expected_result = 'Math: 5.50'
        self.assertEqual(expected_result, self.student_report_card.average_grade_by_subject())

    def test_average_grade_by_subject_count_two(self):
        subject = 'Math'
        self.assertNotIn(subject, self.student_report_card.grades_by_subject)

        self.student_report_card.add_grade(subject, 6)
        self.assertIn(subject, self.student_report_card.grades_by_subject)
        self.assertEqual([6], self.student_report_card.grades_by_subject[subject])

        self.student_report_card.add_grade(subject, 5)
        self.assertEqual([6, 5], self.student_report_card.grades_by_subject[subject])

        expected_result = 'Math: 5.50'
        self.assertEqual(expected_result, self.student_report_card.average_grade_by_subject())

        subject_2 = 'Engl'
        self.assertNotIn(subject_2, self.student_report_card.grades_by_subject)

        self.student_report_card.add_grade(subject_2, 6)
        expected_result_two = 'Math: 5.50\nEngl: 6.00'
        self.assertEqual(expected_result_two, self.student_report_card.average_grade_by_subject())

    def test_average_grade_for_all_subjects(self):
        subject = 'Math'
        self.assertNotIn(subject, self.student_report_card.grades_by_subject)

        self.student_report_card.add_grade(subject, 6)
        self.assertIn(subject, self.student_report_card.grades_by_subject)
        self.assertEqual([6], self.student_report_card.grades_by_subject[subject])

        self.student_report_card.add_grade(subject, 5)
        self.assertEqual([6, 5], self.student_report_card.grades_by_subject[subject])

        expected_result = 'Average Grade: 5.50'
        self.assertEqual(expected_result, self.student_report_card.average_grade_for_all_subjects())

    def test_repr(self):
        subject = 'Math'
        self.assertNotIn(subject, self.student_report_card.grades_by_subject)

        self.student_report_card.add_grade(subject, 6)
        self.assertIn(subject, self.student_report_card.grades_by_subject)
        self.assertEqual([6], self.student_report_card.grades_by_subject[subject])

        self.student_report_card.add_grade(subject, 5)
        self.assertEqual([6, 5], self.student_report_card.grades_by_subject[subject])

        expected_result = "Name: Neo\nYear: 10\n----------\nMath: 5.50\n----------\nAverage Grade: 5.50"
        self.assertEqual(expected_result, self.student_report_card.__repr__())


if __name__ == '__main__':
    main()
