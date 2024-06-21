class Database:
    def __init__(self):
        status = False
        maximumRetry = 3
        count = 0
        self.conn = None
        while count < maximumRetry and self.conn is None:
            try:
                count += 1
                self.conn = pg.DB(
                    host="localhost",
                    user="USERNAME",
                    passwd="PASSWORD",
                    dbname="DBNAME",
                )
                if self.conn is not None:
                    status = True
                    break
            except pg.InternalError:
                print("Trying to reconnect with the database")
            except Exception as err:
                print(err)
        if status:
            print("Connected with the database successfully.")
            result = self.conn.query("SELECT fname, lname FROM employee")

            for firstname, lastname in result.getresult():
                print(firstname, lastname)

            self.conn.close()
        else:
            print("Connection with the database was Unsucessful!")

class Database_clean:
    def __init__(self):

        count = 0
        maximumRetry = 3

        while count < maximumRetry:
            count += 1
            connection = self.establish_connection()
            if self.is_established(connection):
                break

        if self.is_established(connection):
            print("Connected with the database successfully.")
            self.print_from_db(connection)
            connection.close()
            return
        
        print("Connection with the database was Unsucessful!")

    def establish_connection(self):
        connection = None
        try:
            connection = pg.DB(
                host="localhost",
                user="USERNAME",
                passwd="PASSWORD",
                dbname="DBNAME",
            )
        except pg.InternalError:
            print("Trying to reconnect with the database")
        except Exception as err:
            print(err)
        return connection   

    def is_established(self, connection):
        return connection is not None

    def print_from_db(self, connection):
        result = connection.query("SELECT fname, lname FROM employee")
        map(print, result.getresult())
