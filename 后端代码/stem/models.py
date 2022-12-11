from django.db import models


class Stem(models.Model):
    stem = models.CharField('梗', max_length=255, default='')
    pinyin = models.CharField('拼音', max_length=255, default='')
    year = models.IntegerField('年份', default=0)
    come_from = models.TextField('出处', default='')
    content = models.TextField('内容', default='')
    hot = models.IntegerField('热度', default=0)
    category = models.CharField('类别', max_length=255, default='')
    author = models.CharField('作者', max_length=255, default='官方')
    create_time = models.DateTimeField('创建时间', auto_now_add=True)

    class Meta:
        verbose_name = '梗'
        verbose_name_plural = '梗'


class StemComment(models.Model):
    username = models.CharField('账号', max_length=255, default='')
    nickname = models.CharField('用户名', max_length=255, default='')
    content = models.TextField('内容', default='')
    agree = models.IntegerField('点赞', default=0)
    disagree = models.IntegerField('反对', default=0)
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    stem = models.ForeignKey(Stem, on_delete=models.CASCADE)

    class Meta:
        verbose_name = '吐槽'
        verbose_name_plural = '吐槽'


class StemCommentReply(models.Model):
    username = models.CharField('用户名', max_length=255, default='')
    content = models.TextField('内容', default='')
    agree = models.IntegerField('点赞', default=0)
    disagree = models.IntegerField('反对', default=0)
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    stem_comment = models.ForeignKey(StemComment, on_delete=models.CASCADE)

    class Meta:
        verbose_name = '吐槽回复'
        verbose_name_plural = '吐槽回复'


class StemRecommend(models.Model):
    today = models.CharField('日期', max_length=255, default='')
    stem_id = models.CharField('梗id', max_length=255, default='')
    stem = models.CharField('梗', max_length=255, default='')
    create_time = models.DateTimeField('创建时间', auto_now_add=True)

    class Meta:
        verbose_name = '今日推荐'
        verbose_name_plural = '今日推荐'


class StemImage(models.Model):
    stem_image = models.ImageField('梗图', max_length=255, default='', upload_to='static/stem_image')
    stem = models.ForeignKey(Stem, on_delete=models.CASCADE)
    create_time = models.DateTimeField('创建时间', auto_now_add=True)

    class Meta:
        verbose_name = '梗图'
        verbose_name_plural = '梗图'


class StemSearchTimes(models.Model):
    search_content = models.CharField('搜索内容', max_length=255, default='')
    search_times = models.IntegerField('搜索次数', default=0)
    create_time = models.DateTimeField('创建时间', auto_now_add=True)

    class Meta:
        verbose_name = '梗搜索次数统计'
        verbose_name_plural = '梗搜索次数统计'

