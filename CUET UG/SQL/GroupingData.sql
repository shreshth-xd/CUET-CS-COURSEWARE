-- Organizing the data in the results of queries using GROUP BY clause

-- To count the number of male and female users in the registered_users table
SELECT sex, count(sex) FROM registered_users GROUP BY sex;

-- To count the number of male and female users who are older than 18 years
SELECT sex, count(sex) FROM registered_users GROUP BY sex HAVING age>18;