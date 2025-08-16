import psycopg2

# Connect to PostgreSQL
conn = psycopg2.connect(
    dbname="student_management",
    user="postgres",
    password="mahmoud199",
    host="localhost",
    # port="5432"
)

cur = conn.cursor()
conn.autocommit = True

#create tables

cur.execute("create table students (id serial primary key, name varchar(100), email varchar(100), phone varchar(50))")
print("Table created successfully")

cur.execute("create table courses (id serial primary key, course_name varchar(100), credits INT) ")
print("Table created successfully")

cur.execute("alter table students rename column id to student_id")
cur.execute("alter table courses rename column id to course_id")
print("columns renamed successfully")

cur.execute("create table enrollments (id serial primary key, student_id INT references students(student_id), course_id INT references courses(course_id), grade varchar(50))")
print("Enrollments table created successfully")

# insert ro tables

cur.execute( " INSERT INTO students (name, email, phone) VALUES ('Alice Johnson', 'alice@example.com', '1234567890'), ('Bob Smith', 'bob@example.com', '9876543210'), ('Charlie Brown', 'charlie@example.com', '5555555555');")
cur.execute (  "INSERT INTO courses (course_name, credits) VALUES ('Mathematics', 3), ('Computer Science', 4), ('History', 2);" )
cur.execute(   " INSERT INTO enrollments (student_id, course_id, grade) VALUES   (1, 1, 'A'),    (1, 2, 'B'),    (2, 3, 'A'),    (3, 2, 'C');")
print("insert done successfully")

# query tasks

# cur.execute("select * from students;")
# result = cur.fetchall()
# for row in result:
#     print(row)

# cur.execute("select s.name, e.grade from students s join enrollments e on s.student_id = e.student_id where e.grade ='A'; ")
# result = cur.fetchall()
# for row in result:
#     print(row)

# cur.execute("select course_name, credits from courses")
# result = cur.fetchall()
# for row in result:
#     print(row)

# cur.execute("SELECT s.name, c.course_name FROM students s JOIN enrollments e ON s.student_id = e.student_id JOIN courses c ON e.course_id = c.course_id WHERE s.name = 'Alice Johnson';")
# result = cur.fetchall()
# for row in result:
#     print(row)

# cur.execute("SELECT s.name, COUNT(e.course_id) AS total_courses FROM students s JOIN enrollments e ON s.student_id = e.student_id GROUP BY s.name;")
# result = cur.fetchall()
# for row in result:
#     print(row)

# cur.execute("SELECT s.name FROM students s LEFT JOIN enrollments e ON s.student_id = e.student_id WHERE e.course_id IS NULL;")
# result = cur.fetchall()
# for row in result:
#     print(row)

# cur.execute("SELECT *  FROM enrollments ORDER BY grade DESC;")
# result = cur.fetchall()
# for row in result:
#     print(row)

