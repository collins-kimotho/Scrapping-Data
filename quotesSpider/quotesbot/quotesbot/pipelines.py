# import sqlite3
# import mysql.connector
import pymongo

class QuotesbotPipeline:

    def __init__(self):
        # self.create_connection()
        # self.create_table()
        self.conn = pymongo.MongoClient(
            'localhost',
            27017
        )
        db = self.conn['myquotes']
        self.collection = db['quotes_tb']

    # def create_connection(self):
    #     self.conn = mysql.connector.connect(
    #         host = 'localhost',
    #         user = 'root',
    #         passwd = 'Two2061996@',
    #         database = 'myquotes'
    #         )
    #     self.curr = self.conn.cursor()

    # def create_table(self):
    #     self.curr.execute("""DROP TABLE IF EXISTS quotes_tb""")
    #     self.curr.execute("""
    #         CREATE TABLE quotes_tb(
    #             title TEXT,
    #             author TEXT,
    #             tag TEXT
    #         )
    #     """)

    def process_item(self, item, spider):
        # self.store_db(item)
        # return item
        self.collection.insert_one(dict(item))
        return item

    # def store_db(self, item):
    #     self.curr.execute("""INSERT INTO quotes_tb VALUES (%s, %s, %s)""", (
    #         item['title'][0],
    #         item['author'][0],
    #         item['tag'][0]
    #     ))
    #     self.conn.commit()