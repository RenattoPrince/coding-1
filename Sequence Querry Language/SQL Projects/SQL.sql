CREATE TABLE fruits (
    id INT,
    name VARCHAR(100),
    age INT,
    sugar INT
);

INSERT INTO fruits ( id, name, age, sugar)VALUES
(67, 'Apple',4, 21),
(4, 'Watermelon', 6, 67),
(21, 'Orange', 4, 67);
select * from fruits;

select name, age, sugar
from fruits;