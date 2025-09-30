USE foundation_assessment_i;

INSERT INTO students(Student_ID, FORENAME, SURNAME)
VALUES
   (1, "Alice", "Adams"),
   (2, "Belen", "Badillo"),
   (3, "Ciara", "Connelly"),
   (4, "Delia", "Dodds"),
   (5, "Everly", "Evans"),
   (6, "Fabia", "Fahim"),
   (7, "Grace", "Gonzalez")
;

INSERT INTO exams(Exam_ID, Exam_Name, Max_Mark)
VALUES
   (1, "Algorithms", 100),
   (2, "Cyber Security", 80)
;

INSERT INTO results(Result_ID, Student_ID, Exam_ID, Mark)
VALUES
   # the results for the first exam
   (1, 1, 1, 0),
   (2, 2, 1, 62),
   (3, 3, 1, 62),
   (4, 4, 1, 39),
   (5, 5, 1, 98),
   (6, 6, 1, 48),
   (7, 7, 1, 23),
   # the results for the second exam
   (8, 1, 2, 43),
   (9, 2, 2, 68),
   (10, 3, 2, 54),
   (11, 4, 2, 21),
   (12, 5, 2, 68),
   (13, 6, 2, 74),
   (14, 7, 2, 14)
;