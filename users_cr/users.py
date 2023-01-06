from mysqlconnection import connectToMySQL

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod # this classmethod is pulling all the data and displaying it on the read html page
    def get_all(cls):
        query = "SELECT * FROM users"
        results = connectToMySQL("users").query_db(query)

        users=[]

        for user in results:
            users.append(cls(user))

        return users
    
# ------------------------------

    @classmethod # this saves the data and updates the database with new information
    def save(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, created_at, updated_at) VALUES (%(first_name)s, %(last_name)s, %(email)s, NOW(), NOW());"

        return connectToMySQL("users").query_db(query, data)

# ------------------------------


    @classmethod #this selects and shows a specific users information
    def show_user(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s;"

        show_selected_user = connectToMySQL("users").query_db(query, data)
        return cls(show_selected_user[0])

# ------------------------------
    @classmethod #this updates user information 
    def update_user(cls, data):
        query = "UPDATE users SET first_name=%(first_name)s,last_name=%(last_name)s,email=%(email)s, updated_at=NOW() WHERE id = %(id)s;"

        return connectToMySQL('users').query_db(query, data)
# ------------------------------

    @classmethod #this deletes user from database
    def delete_user(cls, data):
        query = "DELETE FROM users WHERE id =%(id)s"

        return connectToMySQL('users').query_db(query, data)
    