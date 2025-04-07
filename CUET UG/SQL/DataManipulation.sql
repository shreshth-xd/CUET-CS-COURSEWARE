-- Manipulating data of a specified table using DML commands, mostly to update, insert or delete records from a table.

-- To insert a new, single and independent record in the specified table:
INSERT INTO registered_users(name,age,sex) VALUES('John Doe',25,'Male');

-- To insert multiple new records on a specified table
INSERT INTO registered_users(name,age,sex) VALUES ('Shreyansh',18,'Male'),
('Vikas',20,'Male'),
('Trishita',17,'Female'),
('Dhruv',20,'Male'),
('Yash',21,'Female'),
('Rudra',22,'Male'),
;
