# 计划动漫类，不一定要看

class TemporaryAnime:
    num = ''  # 序号，记录年月+序号，比如202306000001
    translated_name = ''  # 名称，此处为译名
    abandoned_mark = False  # 放弃标记
    sets_record = ''  # 如果没看完，就需要记录

    def __init__(self, num, translated_name, abandoned_mark, sets_record):
        self.num = num
        self.translated_name = translated_name
        self.abandoned_mark = abandoned_mark
        self.sets_record = sets_record
