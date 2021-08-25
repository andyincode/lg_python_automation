import pymysql
from icecream import ic

class Database:
    def __init__(self, host, user, passwd, db):
        self.host = host
        self.user = user
        self.passwd = passwd
        self.db = db

        self.conn = None    # Connection Object
        self.cursor = None  # Cursor Object

    # Database 접속
    def connect_db(self):
        if self.conn is None:
            self.conn = pymysql.connect(host=self.host, user=self.user, passwd=self.passwd,
                                        db=self.db, charset='utf8')

            # row['name'], row['age'], row['regist_datetime']
            self.cursor = self.conn.cursor(pymysql.cursors.DictCursor)

            # name, age, regist_datetime -> row[0], row[1], row[2]
            # for index in range(3):
            #   ...
            # self.cursor = self.conn.cursor()

    # 쿼리 실행만
    # sql = 'insert into student (name, age) values(%s, %s);'
    # values = ('elias', 20)
    # execut_only(sql, values)
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

    # 쿼리 실행 후 커밋
    def execute_and_commit(self, sql, values=None):
        try:
            self.execute_only(sql, values)
            self.conn.commit()
        except Exception as e:
            print('Exception:', e)
    
    # 커밋만
    def commit_only(self):
        try:
            self.conn.commit()
        except Exception as e:
            print('Exception:', e)

    # 쿼리의 결과값 리스트 가져오기
    # data_list = execute_and_return(...)
    # for data in data_list:
    #   ...
    def execute_and_return(self, sql, values=None):
        try:
            self.execute_only(sql, values)

            data_list = self.cursor.fetchall()

            if data_list is None:
                data_list = []

            return data_list

        except Exception as e:
            print('Exception:', e)

    # 쿼리 후 결과값 하나만 위치가져오기
    def execute_and_return_one(self, sql, values=None):
        try:
            self.execute_only(sql, values)

            data = self.cursor.fetchone()
            return data

        except Exception as e:
            print('Exception:', e)

    # 데이터베이스 연결끊기
    def disconnect_db(self):
        if self.conn is not None:
            self.conn.close()

if __name__ == '__main__':
    db = Database('139.150.74.115', 'student', 'student', 'automation')
    db.connect_db()

    ###########################################################################################################
    # 기존 데이터 삭제
    sql = 'delete from student;'
    db.execute_and_commit(sql)

    ###########################################################################################################
    # 데이터 삽입
    # sql = 'insert into student (name, age) values(' + '"Elias Kim"' + ',' + '45);'
    sql = 'insert into student (name, age) values(%s, %s);'
    values = ('Elias Kim', 45)
    db.execute_and_commit(sql, values)

    ###########################################################################################################
    # 현재 데이터 가져오기
    sql = 'select * from student;'
    data_list = db.execute_and_return(sql)
    for data in data_list:
        ic(data)

    ###########################################################################################################
    # 데이터 업데이트
    sql = 'update student set age=%s where name = %s;'
    values = (21, 'Elias Kim')
    db.execute_and_commit(sql, values)

    # sql = 'select * from student;'
    # data_list = db.execute_and_return(sql)
    # for data in data_list:
    #     ic(data)

    ###########################################################################################################
    # 대량 데이터 삽입
    student_list = [{'name':'Park', 'age':20},
                    {'name':'Lee', 'age':30}]

    for student in student_list:
        sql = 'insert into student (name, age) values(%s, %s);'
        values = (student['name'], student['age'])
        db.execute_only(sql, values)
    db.commit_only()

    sql = 'select name, age from student;'
    data_list = db.execute_and_return(sql)
    for data in data_list:
        ic('%s`s age is %s' % (data['name'], data['age']))
        # ic('%s`s age is %s' % (data[0], data[1]))