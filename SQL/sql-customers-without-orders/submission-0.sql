-- Write your query below
select name 
from customers c 
FULL JOIN orders o on c.id = o.customer_id 
where o.id is NULL;