import psycopg2  # it imports the psycopg2 package.

# Connect to your postgres DB
conn = psycopg2.connect(
    """
    dbname=gibson user=postgres host=localhost port=5432
    """
)
conn.set_session(autocommit=True)
# we use that to open a connection with the gibson postgres database server, which is running on localhost:5432.
# This returns to us a connection object, that we store under the name conn.
# This connection object has certain methods we can use, defined by a class in the psycopg2 package.

# Open a cursor to perform database operations
cur = conn.cursor()
# We'll use one method, called set_session, to set a property to autocommit our changes to the database.
# Another connection method is called cursor, and we can use it to create what is called a cursor object based on that connection.
# This cursor object has some additional methods that will be useful to us.

# The first one is called execute(), and it lets us run some raw SQL statements.
cur.execute(
    """
    DROP TABLE IF EXISTS users;
    """
)

cur.execute(
    """
        CREATE TABLE users(
            id SERIAL PRIMARY KEY,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            phone TEXT NOT NULL,
            reg_date DATE NOT NULL
        );
    """
)

cur.execute(
    """
    INSERT INTO users VALUES 
    (1, 'jones', 'ososo0303', 'jin', 'fjis@gmail.com', '4243430192', '020330'),
    (2, 'hi', 'dfeeeeee', 'ebby', 'jiji@gmail.com', '4243430192', '020330'),
    (3, 'gosdg', 'asdfsadaf', 'query', 'fdsf@gmail.com', '4243430192', '020330'),
    (4, 'aawe', 'qwerwer', 'hinyy', 'asdf@gmail.com', '4243430192', '020330'),
    (5, 'eieie', 'sdfdsa', 'emma', 'asdf@gmail.com', '4243430192', '020330'),
    (6, 'hshs', 'sdfsdaf', 'rosaline', 'sadfas@gmail.com', '4243430192', '020330'),
    (7, 'hihi', 'aaaaaaaa', 'prince', 'asdfas@gmail.com', '4243430192', '020330'),
    (8, 'ojoj', 'sesesesese', 'venus', 'sd@gmail.com', '4243430192', '020330')
    """
)

# Execute a query
cur.execute(
    """
    SELECT * FROM users;
    """
)

# Retrieve query results
records = cur.fetchall()
# To actually retrieve that result set to our program, we can use a cursor method called fetchall().​
# This method makes the result set that we just selected available to our program as a Python list of tuples.

# We print those records.
print("INSERTED gibson:", records, '\n')

# Add these lines of code
cur.execute(
    """
    SELECT username, phone FROM users;
    """
)

gibson_records = cur.fetchall()
for v in gibson_records:
    print(v[0], v[1])

# Add these lines to the bottom
print('')  # new line

cur.execute(
    """
    SELECT phone, name FROM users ORDER BY name, username
    """
)

gibson_records = cur.fetchall()

# enumerate는 index값과 value값을 함께 반환함. 여기 for문 안에서 i는 idx, v는 values를 의미
for i, v in enumerate(gibson_records):
    print(str(i+1) + ".", v[0].capitalize(), v[1].capitalize())

'''
실행 방법

cd week3/psycopg2
python veggies.py

'''

'''
참고) 새 폴더를 terminal을 통해 만들고 싶을 때
mkdir week3/psycopg2

2) Create a file named veggies.py using the touch command 새 파일을 만들고 싶을 때
touch veggies.py
'''
