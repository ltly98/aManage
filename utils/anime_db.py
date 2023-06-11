import sqlite3
import os
import data_models
from data_models.anime import Anime
from data_models.temporary_anime import TemporaryAnime


class AnimeDb:
    # 数据库文件路径
    db_path = 'anime.db'

    # 数据库文件存在性检查，不存在就建库
    def database_exist_check(self):
        if os.path.exists(self.db_path):
            return True
        connect = sqlite3.connect(self.db_path)
        cursor = connect.cursor()

        # 创建动漫表
        # num --> NUM
        # name --> NAME
        # translated_name --> T_NAME
        # author --> AUTHOR
        # animation_production --> A_PRODUCTION
        # tags --> TAGS，存储按字符串拼接
        # scores --> SCORES，存储按字符串拼接
        # restrict_mark --> R_NARK，存储按字符串拼接

        cursor.execute('''CREATE TABLE ANIME(
        NUM VARCHAR NOT NULL,
        NAME VARCHAR NOT NULL,
        T_NAME VARCHAR NOT NULL,
        AUTHOR VARCHAR NOT NULL,
        A_PRODUCTION VARCHAR NOT NULL,
        TAGS VARCHAR NOT NULL,
        SCORES VARCHAR NOT NULL,
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
        return False

    # 插入数据
    def database_insert(self, data_class):
        # 判断数据库是否存在
        if os.path.exists(self.db_path) is not True:
            return False
        # 连接数据库
        connect = sqlite3.connect(self.db_path)
        cursor = connect.cursor()
        # 判断数据类型
        if isinstance(data_class, Anime):
            cursor.execute(
                'INSERT INTO ANIME (NUM,NAME,T_NAME,AUTHOR,A_PRODUCTION,TAGS,SCORES,R_MARK) VALUES (?,?,?,?,?,?,?,?)',
                data_class.class_to_tuples())
            connect.commit()
            cursor.close()
            connect.close()
            return True
        elif isinstance(data_class, TemporaryAnime):
            cursor.execute('INSERT INTO T_ANIME (NUM,T_NAME,A_NARK,S_RECORD) VALUES (?,?,?,?)',
                           data_class.class_to_tuples())
            connect.commit()
            cursor.close()
            connect.close()
            return True
        else:
            return False

    # 更新数据
    def database_update(self, data_class):
        # 判断数据库是否存在
        if os.path.exists(self.db_path) is not True:
            return False
        # 连接数据库
        connect = sqlite3.connect(self.db_path)
        cursor = connect.cursor()
        if isinstance(data_class, Anime):
            cursor.execute(
                'UPDATE ANIME SET NAME=?,T_NAME=?,AUTHOR=?,A_PRODUCTION=?,TAGS=?,SCORES=?,R_MARK=? WHERE NUM=?',
                data_class.class_to_tuples(True))
            connect.commit()
            cursor.close()
            connect.close()
            return True
        elif isinstance(data_class, TemporaryAnime):
            cursor.execute('UPDATE T_ANIME SET T_NAME=?,A_NARK=?,S_RECORD=? WHERE NUM=?',
                           data_class.class_to_tuples(True))
            connect.commit()
            cursor.close()
            connect.close()
            return True
        else:
            return False

    # 删除数据
    def database_delete(self, data_class):
        # 判断数据库是否存在
        if os.path.exists(self.db_path) is not True:
            return False
        # 连接数据库
        connect = sqlite3.connect(self.db_path)
        cursor = connect.cursor()
        if isinstance(data_class, Anime):
            cursor.execute('DELETE FROM ANIME WHERE NUM=?', data_class.num)
            connect.commit()
            cursor.close()
            connect.close()
            return True
        elif isinstance(data_class, TemporaryAnime):
            cursor.execute('DELETE FROM T_ANIME WHERE NUM=?', data_class.num)
            connect.commit()
            cursor.close()
            connect.close()
            return True
        else:
            return False

    # 常规数据查询
    def database_general_query(self, data_class):
        # 数据列表
        data_list = []
        # 判断数据库是否存在
        if os.path.exists(self.db_path) is not True:
            return data_list
            # 连接数据库
        connect = sqlite3.connect(self.db_path)
        cursor = connect.cursor()
        if isinstance(data_class, Anime):
            data = cursor.execute('SELECT * FROM ANIME')
            for row in data:
                tags_list = row[5].split('|')
                scores_list = row[6].split('|')
                data_list.append(Anime(row[0], row[1], row[2], row[3], row[4], tags_list, scores_list, row[7]))
            cursor.close()
            connect.close()
            return data_list
        elif isinstance(data_class, TemporaryAnime):
            data = cursor.execute('SELECT * FROM T_ANIME')
            for row in data:
                data_list.append(TemporaryAnime(row[0], row[1], row[2], row[3]))
            cursor.close()
            connect.close()
            return data_list
        else:
            return data_list


# 测试用
if __name__ == "__main__":

    # 创建数据库用
    # db = AnimeDb()
    # print(db.database_exist_check())

    # 测试切割str
    str = '|标签1|标签2|标签3|标签4|标签5'
    n_str = str[1:]
    print(str.split('|'))
    print(n_str.split('|'))
