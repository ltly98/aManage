# 计划动漫类，不一定要看

class TemporaryAnime:
    num = ''  # 序号，记录年月+序号，比如202306000001
    translated_name = ''  # 名称，此处为译名
    abandoned_mark = False  # 放弃标记
    sets_record = ''  # 如果没看完，就需要记录

    def __init__(self, num='', translated_name='', abandoned_mark=False, sets_record=''):
        self.num = num
        self.translated_name = translated_name
        self.abandoned_mark = abandoned_mark
        self.sets_record = sets_record

    # 转换元组，mode设置为True为修改模式，默认插入模式，为数据库提供数据格式
    def class_to_tuples(self, mode=False):
        if mode is False:
            data_tuple = (self.num, self.translated_name, self.abandoned_mark, self.sets_record)
            return data_tuple
        else:
            data_tuple = (self.translated_name, self.abandoned_mark, self.sets_record, self.num)
            return data_tuple


# 测试用
if __name__ == "__main__":
    t = TemporaryAnime()
    print(isinstance(t, TemporaryAnime))
    print(t.class_to_tuples())
