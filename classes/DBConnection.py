#! python3
from database import database as db

try:
    import pymysql
except:
    print("PyMySQL Module is not installed")
    print("Installing PyMySQL package...")
    import sys, subprocess

    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pymysql'])


class DBConnection:
    """Connecting to database and database table
        attributes:
            * hostname  :   Host name, [default:localhost]
            * username  :   Database username
            * password  :   Database password
            * dbname    :   Database name
            * table     :   Targeted table name
    """

    hostname = db.DB_HOST
    username = db.DB_USERNAME
    password = db.DB_PASSWORD
    dbname = db.DB_NAME

    def __init__(self):

        try:
            self.conn = pymysql.connect(self.hostname, self.username, self.password, self.dbname)
        except ValueError:
            print("Error::Can't establish database connection")
            exit()

