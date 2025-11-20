CREATE TABLE students (
    id INT,
    name  VARCHAR(100),
    age INT,
    grade VARCHAR(10)
);

INSERT INTO students (id, name, age, grade)VALUES
(01, 'Ali',17, 10),
(21, 'Tanqif', 16, 9),
(01, 'Ramin', 18, 11);
select * from students;



select * from students
where age>=17;




select name,grade
from students;