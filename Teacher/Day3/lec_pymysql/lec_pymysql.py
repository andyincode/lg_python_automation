import pymysql

class Database:
    def __init__(self, host, user, passwd, db):
        self.host = host
        self.user = user
        self.passwd = passwd
        self.db = db

        self.conn = None
        self.cursor = None

    def connect_db(self):
        if self.conn is None:
            self.conn = pymysql.connect(host=self.host, user=self.user, passwd=self.passwd,
                                        db=self.db, charset='utf8')
            # name, age, regist_datetime -> row[0], row[1], row[2]
            # self.cursor = self.conn.cursor()
            # row['name'], row['age'], row['regist_datetime']
            self.cursor = self.conn.cursor(pymysql.cursors.DictCursor)

    def execute_only(self, sql, values=None):
        try:
            if values is None:
                # select * from student;
                self.cursor.execute(sql)
            else:
                # select * from student where id = 0;
                self.cursor.execute(sql, values)

        except Exception as e:
            print('Exception:', e)

    def execute_and_commit(self, sql, values=None):
        try:
            self.execute_only(sql, values)
            self.conn.commit()
        except Exception as e:
            print('Exception:', e)

    def commit_only(self):
        try:
            self.conn.commit()
        except Exception as e:
            print('Exception:', e)

    def execute_and_return(self, sql, values=None):
        try:
            self.execute_only(sql, values)

            data_list = self.cursor.fetchall()

            if data_list is None:
                data_list = []

            return data_list

        except Exception as e:
            print('Exception:', e)

    def execute_and_return_one(self, sql, values=None):
        try:
            self.execute_only(sql, values)

            data = self.cursor.fetchone()
            return data

        except Exception as e:
            print('Exception:', e)

    def disconnect_db(self):
        if self.conn is not None:
            self.conn.close()