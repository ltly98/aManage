import sqlite3
import os

db_path = 'anime.db'


# 数据库文件存在性检查
def database_exist_check():
    if os.path.exists(db_path):
        return
    connect = sqlite3.connect(db_path)
    cursor = connect.cursor()

    # 创建动漫表
    # num --> NUM
    # name --> NAME
    # translated_name --> T_NAME
    # tags --> TAGS，存储按字符串拼接
    # scores --> SCORES，存储按字符串拼接
    # mark --> MARK
    # restrict_mark --> R_NARK，存储按字符串拼接
    # img_path不需要存储，根据路径拼接

    cursor.execute('''CREATE TABLE ANIME(
    NUM VARCHAR NOT NULL,
    NAME VARCHAR NOT NULL,
    T_NAME VARCHAR NOT NULL,
    TAGS VARCHAR NOT NULL,
    SCORES VARCHAR NOT NULL,
    MARK BOOLEAN NOT NULL,
    R_MARK BOOLEAN NOT NULL);''')

    # 创建临时动漫表
    # num --> NUM
    # translated_name --> T_NAME
    # abandoned_mark --> A_MARK
    # sets_record --> S_RECORD

    cursor.execute('''CREATE TABLE T_ANIME(
    NUM VARCHAR NOT NULL,
    T_NAME VARCHAR NOT NULL,
    A_NARK BOOLEAN NOT NULL,
    S_RECORD VARCHAR NOT NULL)''')

    connect.commit()
    cursor.close()
    connect.close()


# 插入数据

def database_insert(sql, data):
    if os.path.exists(db_path) is not True:
        return
    connect = sqlite3.connect(db_path)
    cursor = connect.cursor()
    cursor.execute(sql, data)
    connect.commit()
    cursor.close()
    connect.close()


# 测试用
if __name__ == "__main__":
    database_exist_check(path)
