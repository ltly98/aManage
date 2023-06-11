# 已看完动漫类

class Anime:
    num = ''  # 序号，年月+序号，比如202302000001
    name = ''  # 原名
    translated_name = ''  # 译名
    author = ''  # 原作作者
    animation_production = ''  # 动画制作公司
    tags = []  # 分类标签
    scores = ['0', '0']  # 得分，按剧情，画风，满分5
    restrict_mark = False  # 是为禁忌番剧

    def __init__(self, num='', name='', translated_name='', author=None, animation_production=None, tags=None,
                 scores=None, restrict_mark=False):
        if tags is None:
            tags = []
        if scores is None:
            scores = [0, 0]
        self.num = num
        self.name = name
        self.translated_name = translated_name
        self.author = author
        self.animation_production = animation_production
        self.tags = tags
        self.scores = scores
        self.restrict_mark = restrict_mark

    # 转换元组，mode设置为True为修改模式，默认插入模式，为数据库提供数据格式
    def class_to_tuples(self, mode=False):
        tags_str = ''
        scores_str = ''
        for tag in self.tags:
            tags_str = tags_str + '|' + tag
        for score in self.scores:
            scores_str = scores_str + '|' + score
        if mode is False:
            data_tuple = (
                self.num, self.name, self.translated_name, self.author, self.animation_production, tags_str[1:],
                scores_str[1:],
                self.restrict_mark)
            return data_tuple
        else:
            data_tuple = (
                self.name, self.translated_name, self.author, self.animation_production, tags_str, scores_str,
                self.restrict_mark, self.num)
            return data_tuple


# 测试用
if __name__ == "__main__":
    a = Anime()
    print(isinstance(a, Anime))
    print(a.class_to_tuples())
