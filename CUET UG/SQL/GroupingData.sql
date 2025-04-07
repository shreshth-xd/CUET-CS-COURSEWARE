-- Organizing the data in the results of queries using GROUP BY clause

-- To count the number of male and female users in the registered_users table
SELECT sex, count(sex) FROM registered_users GROUP BY sex;

-- To count the number of male and female users who are older than 18 years
SELECT sex, count(sex) FROM registered_users GROUP BY sex HAVING age>18;


-- To calulcate the average age group of male and female users and sorting the order in descending order and making sure that there are
-- more than 2 users in each gender
SELECT sex, avg(age) FROM registered_users GROUP BY sex HAVING count(age)>2 ORDER BY avg(age) DESC;