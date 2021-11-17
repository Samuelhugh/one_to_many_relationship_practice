#-----  Import connectToMySQL FROM flask_app.config.mysqlconnect
from flask_app.config.mysqlconnection import connectToMySQL

#-----  Import ninja file FROM models using the route of flask_app.models To Avoide Circular Imports!
from flask_app.models import ninja

class Dojo:
    def __init__(self, db_data):
        self.id = db_data['id']
        self.name = db_data['name']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']
        self.ninjas = []  #-----  If I Want A List Of Users Then I Would Need A Empty List, If I Want One Single User Then I Want To Set The "self." To "None" In Order To Grab That One Specific User For That Specific Product Or Whatever.

#-----  classmethod to Run the Query and Provide the Functionality I need to create a dojo Row/Record/Object! [CREATE]
    @classmethod
    def create(cls, data):
        query = 'INSERT INTO dojos(name, created_at, updated_at) VALUES (%(name)s, NOW(), NOW());'  #-----  Returns the ID number of the Each Row Individually!
        return connectToMySQL('dojos_and_ninjas').query_db(query, data)  #-----  Returns the Successfully Queried Connection. Also Connects to me Database. [INSERT CRUDS' RETURN IDS?]

#-----  classmethod to Run the Query and Provide the Functionality I need to render all the dojos on my HTML page! [READ]
    @classmethod
    def show_all_dojos_query(cls):
        query = 'SELECT * FROM dojos;'  #-----  SELECT Queries Always Returns A List of Dictionaries!
        dojos_from_db = connectToMySQL('dojos_and_ninjas').query_db(query)  #-----  Connects my DataBase and Run my Try Catch Block (Aka My Exception Handleing). 
        alldojos = []  #-----  An Empty List To Hold All Of My Dojos.
        for dojo in dojos_from_db:  #-----  For Loop, Looping Through All of My Successfully Queried "Dojos" In My Database And giving me access to the Records/Rows.
            alldojos.append( cls(dojo) )
        return alldojos  #-----  Returns a List of Dictionaries that I can render on my HTML Page!

    @classmethod
    def get_dojo_with_ninja(cls, data):
        query = 'SELECT * FROM dojos LEFT JOIN ninjas ON ninjas.dojo_id = dojos.id WHERE dojos.id = %(id)s;'  #-----  SELECT Query Or READ Query that JOINS ninjas onto dojos. And References Them By Their ids. Remember That it is A LEFT JOIN Because I Want to Show Everything On The right and left even if they don't have a match AND To Not Throw An Error.
        results = connectToMySQL('dojos_and_ninjas').query_db(query, data)
        dojo_with_ninjas = cls( results[0] )  #-----  A Variable I Use To Hold On Each Individual Record/Row/Object From The Results Variable.
        for row_from_db in results:  #-----  A for loop, looping Through The List Of Dictionaries That I received From My Results Variable.
            ninjas_data = {'id': row_from_db['ninjas.id'], 'first_name': row_from_db['first_name'], 'last_name': row_from_db['last_name'], 'age': row_from_db['age'], 'created_at': row_from_db['ninjas.created_at'], 'updated_at': row_from_db['ninjas.updated_at']}  #-----  Data Table That I need. ???
            dojo_with_ninjas.ninjas.append( ninja.Ninja( ninjas_data ) )  #-----  Appending Each Ninja Instance To My "self.ninjas = []".
        return dojo_with_ninjas  #-----  Return The Variable That is holding onto Each Individual Row/Record Referenced By The ninjas "dojo_id" That matches with the dojos "dojos.id".