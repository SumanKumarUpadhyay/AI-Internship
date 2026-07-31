-- Day 12 - AI Interns Database
CREATE DATABASE ai_interns;

-- create intern table
CREATE TABLE interns (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    skills VARCHAR(200),
    score INT,
    domain VARCHAR(100)
);

-- View all interns
SELECT * FROM interns;

-- Insert Records
INSERT INTO interns (name, skills, score, domain)
VALUES
('Suman Kumar', 'Python, Machine Learning', 90, 'AI/ML'),
('Rahul Sharma', 'SQL, Power BI', 82, 'Data Science'),
('Priya Singh', 'Python, NLP', 88, 'NLP'),
('Aman Kumar', 'Python, Deep Learning', 85, 'AI/ML'),
('Neha Sharma', 'SQL, Excel', 80, 'Data Analytics');

-- View all interns
SELECT * FROM interns;



-- Update
UPDATE interns
SET score = 92
WHERE name = 'Suman Kumar';

-- Delete
DELETE FROM interns
WHERE name = 'Neha Sharma';

-- check the final data 

select * from interns;

-- GROUP BY
SELECT domain, COUNT(*) AS total_interns
FROM interns
GROUP BY domain;

-- Average Score by Domain
SELECT domain, AVG(score) AS average_score
FROM interns
GROUP BY domain;

-- Final Data
SELECT * FROM interns;

-- INSERT DOMAIN DATA
INSERT INTO domain_details (domain, mentor)
VALUES
('AI/ML', 'Aditya Sir'),
('Data Science', 'Rahul Sir'),
('NLP', 'Suyash Sir'),
('Data Analytics', 'Amit Sir');

SELECT * FROM domain_details;

-- 11. JOIN
-- Combine Intern and Domain information
SELECT interns.name, interns.skills, interns.score, domain_details.domain, domain_details.mentor
FROM interns
JOIN domain_details ON interns.domain = domain_details.domain;

-- Final Data
SELECT * FROM interns;