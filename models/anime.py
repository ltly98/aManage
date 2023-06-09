# 已看完动漫类

class Anime:
    num = ''  # 序号，年月+序号，比如202302000001
    name = ''  # 原名
    translated_name = ''  # 译名
    tags = []  # 分类标签
    scores = [0, 0]  # 得分，按剧情，画风
    mark = False  # 是否看完标记
    restrict_mark = False  # 是为禁忌番剧
    img_path = ''  # 图片路径

    def __init__(self, num, name, translated_name, tags, scores, mark, restrict_mark, img_path):
        self.num = num
        self.name = name
        self.translated_name = translated_name
        self.tags = tags
        self.scores = scores
        self.mark = mark
        self.restrict_mark = restrict_mark
        self.img_path = img_path
