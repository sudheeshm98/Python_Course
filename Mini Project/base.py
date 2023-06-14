import mysql.connector


class User:
    def __init__(self, host, user, password, database):
        self.mydb = mysql.connector.connect(host=host, user=user, password=password, database=database)
        self.mycursor = self.mydb.cursor()
        self.logged_in_user = None

    def start(self):
        while True:
            print("-----------------------------------------------------")
            print('\t\t\tWelcome to RentACar')
            print('\t\t\t1. User login\n\t\t\t2. Register new user')
            option = int(input('\t\t\tenter your option:'))

            if option == 1:
                return self.login_user()

            elif option == 2:
                return self.register_user()

            else:
                print("-----------------------------------------------------")
                print('Please enter a valid option')

    def register_user(self):
        while True:
            print("-----------------------------------------------------")
            name = input("\t\t\tName:")
            email = input("\t\t\tEmail:")
            password = input("\t\t\tPassword:")

            query = f"select * from users where email='{email}'"
            self.mycursor.execute(query)
            result = self.mycursor.fetchone()

            if result:
                print("-----------------------------------------------------")
                print('\t\t\tuser already exist. Please try again')
            else:
                query = f"insert into users(name, password, email) values ('{name}', '{password}', '{email}')"
                self.mycursor.execute(query)
                self.mydb.commit()
                print("-----------------------------------------------------")
                print("\t\t\tUser registered successfully")
                return self.start()

    def login_user(self):
        while True:
            print("-----------------------------------------------------")
            email = input("\t\t\tEmail:")
            password = input("\t\t\tPassword:")
            query = f"select * from users where email='{email}' and password='{password}'"
            self.mycursor.execute(query)
            result = self.mycursor.fetchone()

            if result:
                print("-----------------------------------------------------")
                print('\t\t\tLogin successful')
                self.logged_in_user = result
                self.show_menu()
                break
            else:
                print("-----------------------------------------------------")
                print('\t\t\tInvalid email or password')

    def show_menu(self):
        while self.logged_in_user is not None:
            print("-----------------------------------------------------")
            print("\t\t\t1.Add a car\n\t\t\t2.Rent a car\n\t\t\t3.User details\n\t\t\t4.Logout")
            option = int(input("\t\t\tEnter your option:"))

            if option == 1:
                return self.add_car()

            elif option == 2:
                return self.rent_car()

            elif option == 3:
                return self.user_details()

            elif option == 4:
                print("-----------------------------------------------------")
                return self.log_out()
            else:
                print("-----------------------------------------------------")
                print("\t\t\tplease enter a valid option")

    def add_car(self):
        while True:
            print("-----------------------------------------------------")
            make = input("\t\t\tMake:")
            model = input("\t\t\tModel:")
            year = int(input("\t\t\tYear:"))
            num = input("\t\t\tRegistration number:")
            price = float(input("\t\t\tRental price per hour:"))

            if_exist_query = f"select * from cars where registration_number='{num}'"
            self.mycursor.execute(if_exist_query)
            is_exist = self.mycursor.fetchone()

            if is_exist:
                print("-----------------------------------------------------")
                print("\t\t\tCar already added. Please try again")
            else:
                owner_id = self.logged_in_user[0]
                add_car_query = f"insert into cars(make, model, year, price, registration_number,\
                 availability, owner_id)\
                 values('{make}', '{model}', '{year}', '{price}', '{num}', 1, '{owner_id}')"
                self.mycursor.execute(add_car_query)
                self.mydb.commit()
                result = self.mycursor.rowcount

                if result:
                    print("-----------------------------------------------------")
                    print("\t\t\tCar added successfully")
                    self.show_menu()
                    break
                else:
                    print("-----------------------------------------------------")
                    print("\t\t\tSomething went wrong. Please check your entries")

    def rent_car(self):
        print("Available cars:")
        available_cars = self.get_available_cars()
        for id, car in enumerate(available_cars):
            print(f"{id + 1}. {car}")

        if not available_cars:
            print("No cars available for rent.")
            return

        car_objects = [Car(*car) for car in available_cars]

        while True:
            car_id = input("Enter the ID of the car you want to rent (or 'q' to cancel): ")

            if car_id == 'q':
                return self.show_menu()
            elif not car_id.isdigit() or int(car_id) not in range(1, len(available_cars) + 1):
                print("Invalid car ID. Please try again.")
            else:
                car_id = int(car_id)
                selected_car = car_objects[car_id - 1]
                rent_hours = int(input("Enter the number of hours you want to rent the car for: "))
                total_price = rent_hours * float(selected_car.price)

                update_query = f"UPDATE cars SET availability = 0 WHERE id = {selected_car.car_id}"
                self.mycursor.execute(update_query)
                self.mydb.commit()

                insert_query = f"INSERT INTO rental_history (car_name, registration, owner_id, user_id) \
                                VALUES ('{selected_car.model}', '{selected_car.registration_number}',\
                                {selected_car.owner_id}, {self.logged_in_user[0]})"
                self.mycursor.execute(insert_query)
                self.mydb.commit()

                print("Car rented successfully!")
                print(f"Total price: {total_price}")
                return self.show_menu()

    def get_available_cars(self):
        query = "select id, make, model, year, price, registration_number, availability, owner_id\
         from cars where availability = 1"
        self.mycursor.execute(query)
        return self.mycursor.fetchall()

    def user_details(self):
        print("-----------------------------------------------------")
        print("\t\t\t1. Rented cars\n\t\t\t2. My cars\n\t\t\t3. Go back")
        option = int(input("\t\t\tEnter your choice:"))

        if option == 1:
            print("-----------------------------------------------------")
            self.rented_cars()
            print("\t\t\t1. Return car\n\t\t\t2. Go back")
            option = int(input("\t\t\tEnter your option:"))
            if option == 1:
                return self.return_car()

            elif option == 2:
                return self.user_details()

        elif option == 2:
            self.user_cars()
            return self.user_details()

        else:
            return self.show_menu()

    def rented_cars(self):
        query = f"SELECT rh.rental_id, rh.car_name, rh.registration, c.availability\
            FROM rental_history rh JOIN cars c\
            ON rh.registration = c.registration_number \
            WHERE rh.user_id = {self.logged_in_user[0]} AND c.availability = 0"
        self.mycursor.execute(query)
        result = self.mycursor.fetchall()
        for i in result:
            print(i)

    def return_car(self):
        car_id = int(input("\t\t\tEnter car id to return:"))
        update_query = f"UPDATE cars AS c JOIN rental_history AS rh ON c.registration_number = rh.registration \
                        SET c.availability = 1 \
                        WHERE rh.user_id = {self.logged_in_user[0]} AND rh.rental_id = {car_id} AND c.availability = 0"
        self.mycursor.execute(update_query)
        self.mydb.commit()

        if self.mycursor.rowcount > 0:
            print("\t\t\tCar returned successfully!")
            return self.user_details()
        else:
            print("\t\t\tInvalid car id or you do not have permission to return this car.")
            return self.user_details()

    def user_cars(self):
        query = f"""select * from cars where owner_id = {self.logged_in_user[0]}"""
        self.mycursor.execute(query)
        result = self.mycursor.fetchall()

        for i in result:
            print(i)

    def log_out(self):
        self.logged_in_user = None
        print("-----------------------------------------------------")
        print("\t\t\tLogged out successfully")
        return self.start()


class Car:
    def __init__(self, car_id, make, model, year, price, registration_number, availability, owner_id):
        self.car_id = car_id
        self.make = make
        self.model = model
        self.year = year
        self.price = price
        self.registration_number = registration_number
        self.availability = availability
        self.owner_id = owner_id

    def display_details(self):
        print("Make:", self.make)
        print("Model:", self.model)
        print("Year:", self.year)
        print("Price:", self.price)
        print("Registration Number:", self.registration_number)
        print("Availability:", self.availability)
        print("Owner Id:", self.owner_id)
        print("-------------------")


test_user = User('localhost', 'root', 'Heisenberg_123', 'vehicle_rental_db')
test_user.start()
