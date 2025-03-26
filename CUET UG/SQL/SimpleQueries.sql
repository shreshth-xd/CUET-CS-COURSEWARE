-- Command to open a existing database:
use database;

-- Now creating a sample Table(a relation) in that database:
CREATE TABLE Registered_users (Name char(20), Age int, Sex char(10));

-- Inserting some sample data into the table
INSERT INTO registered_users(name,age,sex) values ('Aiden Smith', 21, 'Male'),
('Olivia Johnson', 19, 'Female'),
('Ethan Brown', 22, 'Male'),
('Sophia Martinez', 20, 'Female'),
('Liam Wilson', 23, 'Male'),
('Emma Taylor', 18, 'Female'),
('Noah Anderson', 25, 'Male'),
('Ava Thomas', 22, 'Female'),
('Mason White', 24, 'Male'),
('Isabella Harris', 21, 'Female'),
('Lucas Clark', 20, 'Male'),
('Mia Lewis', 19, 'Female'),
('Elijah Walker', 23, 'Male'),
('Amelia Young', 22, 'Female'),
('James Hall', 26, 'Male'),
('Charlotte Allen', 18, 'Female'),
('Benjamin Scott', 21, 'Male'),
('Harper Adams', 20, 'Female'),
('Henry Nelson', 24, 'Male'),
('Evelyn Carter', 23, 'Female');

-- To select all the columns from a certain relation
SELECT * FROM Registered_users;