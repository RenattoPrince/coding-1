CREATE TABLE products(
product_id text,
product_name text,
supplier_id text,
category_id text,
unit text,
price REAL);
 insert into products(product_id,product_name,supplier_id,category_id,unit,price)VALUES
 ('1', 'cows','1', '1', '30', 90),
 ('2', 'sheep','1', '1', '30', 90),
 ('3', 'horses','1', '1', '30', 90),
 ('4', 'birds','1', '1', '30', 90),
 ('5', 'pigs','1', '1', '30', 90);


SELECT * from products;

SELECT count(product_id) as Product_Count
from products;

SELECT avg(price) as 'Average price'
from products;

select sum(price) as 'Total price'
from products;