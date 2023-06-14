import mysql.connector

my_db = mysql.connector.connect(host="localhost", user="root", password="sudhi@123")
print(my_db)

my_cursor = my_db.cursor()

my_cursor.execute('create database vehicle_rental_db')
my_cursor.execute('show databases')
for x in my_cursor:
    print(x)

my_cursor.execute('use vehicle_rental_db')

create_users_table_query = """create table users( 
                  id int auto_increment primary key,
                  name varchar(250) not null,
                  password varchar(250) not null,
                  email varchar(250) not null,
                  created_at timestamp default current_timestamp
                  )"""

my_cursor.execute(create_users_table_query)


create_cars_table_query = """create table cars(
                  id int auto_increment primary key,
                  make varchar(255) not null,
                  model varchar(255) not null,
                  year int not null,
                  price decimal(10,2) not null,
                  registration_number varchar(20) not null,
                  availability boolean not null,
                  owner_id int,
                  foreign key(owner_id) references users(id)
                  )
                  """

my_cursor.execute(create_cars_table_query)

rental_history_table = """CREATE TABLE rental_history (
                    rental_id INT AUTO_INCREMENT PRIMARY KEY,
                    car_name VARCHAR(255),
                    registration VARCHAR(50),
                    owner_id INT,
                    user_id INT,
                    FOREIGN KEY (owner_id) REFERENCES users(id),
                    FOREIGN KEY (user_id) REFERENCES users(id)
                    )
                    """


my_cursor.execute(rental_history_table)
