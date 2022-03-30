# import postgresql database
import psycopg2
import psycopg2.extras



# connect to postgresql database
def connect():
    try:
        connection = psycopg2.connect(user = "postgres",
                                      password = "postgres",
                                      host = "localhost"
                                      )
        cursor = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cursor.execute("SELECT * FROM test")
        row = cursor.fetchone()
        print(row)
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()
            print('Database connection closed.')
            







class Pipeline:

  def __init__(self):

  



  def get_new_art_db  (art_details):
    connect()
    cursor.execute("SELECT * FROM art_details")
    row = cursor.fetchone()
    print(row)







  def create_array_of_dictionaries(last_read_id):





  def upload_new_art_to_GCS():







  def create_json ():






  def upload_json_GCS():





  def batch_prediction():




