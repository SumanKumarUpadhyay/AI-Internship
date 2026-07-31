# Day 12 - SQL, PostgreSQL & SQLAlchemy

## Overview

On Day 12, I learned the basics of SQL and PostgreSQL and practiced different database operations. I created an AI Intern Management Database to store and manage intern details.

## Learning Objectives

- SQL
- PostgreSQL
- CRUD Operations
- SQLAlchemy
- Database Management
- Basic Database Relationships

## Mini Practical - AI Interns Database

Created a PostgreSQL database named:

`ai_interns`

The database stores the following intern information:

- Name
- Skills
- Score
- Domain

## Database Table

### interns

| Column | Description |
|---|---|
| id | Unique ID of intern (Primary Key) |
| name | Name of the intern |
| skills | Technical skills |
| score | Intern performance score |
| domain | Working domain |

### domain_details

| Column | Description |
|---|---|
| domain | Domain name (Primary Key) |
| mentor | Mentor assigned to the domain |

## SQL Operations Practiced

### CREATE
Created the database and required tables.

### INSERT
Added multiple intern records into the database.

### SELECT
Retrieved and displayed records from the database.

### UPDATE
Updated existing intern information.

### DELETE
Deleted records from the database.

### GROUP BY
Grouped interns based on their domain and calculated total interns and average scores.

### JOIN
Combined the `interns` and `domain_details` tables to display intern and mentor information together.

## Technologies Used

- PostgreSQL
- SQL
- VS Code
- Python
- SQLAlchemy

## Files

- `ai_interns.sql` - Contains SQL queries for database creation and CRUD operations.
- `README.md` - Documentation of Day 12 work.
- `screenshots/` - Contains database query and output screenshots.

## Conclusion

Successfully created and managed an AI Intern database using PostgreSQL. Practiced SQL CRUD operations, GROUP BY, JOIN, primary keys, and basic relational database concepts.
