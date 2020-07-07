#! python3
from classes import DBConnection as db


class Model:
    """
        Base model class, where all other model will extend it
    """
    # Targeted table
    table = ''

    def __init__(self):
        """
            Model class constructor, initiates the database connection and keep
            connection running for all models
        """
        self.db = db.DBConnection()
        self.cursor = self.db.conn.cursor()

    def all(self):
        """Get all records from table"""
        sql = "SELECT * FROM " + self.table
        self.cursor.execute(sql)
        return self.cursor.fetchall()
        pass
