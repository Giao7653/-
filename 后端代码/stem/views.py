import json
import pinyin
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from userhome.models import User
from .models import Stem, StemRecommend, StemImage, StemComment, StemSearchTimes
import datetime


# 所有梗
def allStem(request):
    if request.method == 'GET':
        data = []
        for i in Stem.objects.all():
            stem_list = {'stem': i.stem, 'pinyin': i.pinyin, 'year': i.year,
                         'come_from': i.come_from, 'content': i.content, 'hot': i.hot}
            data.append(stem_list)
        return JsonResponse({'data': data}, safe=False)
    else:
        return JsonResponse({
            'data': '请求方法错误'
        }, status=200)


# 今日推荐
def todayRecommend(request):
    if request.method == 'GET':
        # 当前时间
        today = datetime.datetime.now().strftime("%Y-%m-%d")
        # 存在就直接返回，否则就创建
        todayStem = StemRecommend.objects.filter(today=today)
        # 存在
        data = []
        if len(todayStem) != 0:
            for i in todayStem:
                todayData = {'stem_id': i.stem_id, 'stem': i.stem}
                data.append(todayData)
            return JsonResponse({'data': data}, safe=False)
        # 不存在
        for i in Stem.objects.all().order_by('?')[:6]:
            stem_list = {'stem_id': i.id, 'stem': i.stem}
            # 入库
            StemRecommend.objects.create(stem_id=i.id, stem=i.stem, today=today)
            data.append(stem_list)

        return JsonResponse({'data': data}, safe=False)
    else:
        return JsonResponse({
            'data': '请求方法错误'
        }, status=400)


# 查询某个单独梗id
def findStem(request, stem_id):
    if request.method == 'GET':
        username = request.GET.get('username', '')
        content = {}
        image = []
        # 保存用户浏览量
        if username != "":
            get = User.objects.filter(username=username)
            if len(get) != 0:
                this_user = User.objects.get(username=username)
                this_user.num_views = str(1 + int(this_user.num_views))
                this_user.save()
        # 保存hot
        this_stem = Stem.objects.get(id=stem_id)
        this_stem.hot += 1
        this_stem.save()
        for i in Stem.objects.filter(id=stem_id):
            content['stem'] = i.stem
            content['pinyin'] = i.pinyin
            content['year'] = i.year
            content['come_from'] = i.come_from
            content['content'] = i.content
            content['hot'] = i.hot
            content['category'] = i.category
            content['create_time'] = i.create_time.strftime("%Y-%m-%d")
            for j in User.objects.filter(username=i.author):
                content['user_id'] = j.username
                content['avatar'] = j.user_image.name
                content['author'] = j.nickname

        for i in StemImage.objects.filter(stem_id=stem_id):
            stem_image = {'image': i.stem_image.name}
            image.append(stem_image)
        data = {
            'content': content,
            'image': image
        }
        return JsonResponse({
            'data': data
        }, status=200)
    else:
        return JsonResponse({
            'data': '请求方法错误'
        }, status=400)


# 搜索功能
def search(request):
    if request.method == 'GET':
        get_stem = request.GET['stem']
        # 增加搜索次数
        search_content = StemSearchTimes.objects.filter(search_content=get_stem)
        if len(search_content) == 0:
            StemSearchTimes.objects.create(search_content=get_stem, search_times=1)
        else:
            this_times = StemSearchTimes.objects.get(search_content=get_stem)
            this_times.search_times += 1
            this_times.save()
        data = []
        # 若搜索的是编号
        if get_stem.isdigit():
            # O(1)
            for i in Stem.objects.filter(id=get_stem):
                stemData = {'stem_id': i.id, 'stem': i.stem, 'pinyin': i.pinyin, 'year': i.year,
                            'come_from': i.come_from, 'content': i.content, 'hot': i.hot}
                img = []
                for j in StemImage.objects.filter(stem_id=i.id):
                    img.append(j.stem_image.name)
                stemData['stem_image'] = img
                data.append(stemData)
        # __contains 模糊搜索
        for i in Stem.objects.filter(stem__contains=get_stem):
            stemData = {'stem_id': i.id, 'stem': i.stem, 'pinyin': i.pinyin, 'year': i.year,
                        'come_from': i.come_from, 'content': i.content, 'hot': i.hot}
            img = []
            for j in StemImage.objects.filter(stem_id=i.id):
                img.append(j.stem_image.name)
            stemData['stem_image'] = img
            data.append(stemData)
        return JsonResponse({
            'data': data
        }, status=200)

    else:
        return JsonResponse({
            'data': '请求方法错误'
        }, status=400)


# 查找x年热搜
def xYearHot(request):
    if request.method == "GET":
        get_year = request.GET['year']
        data = []
        for i in Stem.objects.filter(year=get_year).order_by('-hot')[:6]:
            stemData = {'stem_id': i.id, 'stem': i.stem}
            data.append(stemData)
        return JsonResponse({
            'data': data
        }, status=200, safe=False)
    else:
        return JsonResponse({
            'data': '请求方法错误'
        }, status=400)


# 查找某个梗的所有评论
def stemCommentQuery(request):
    if request.method == 'GET':
        stem_id = request.GET['stem_id']
        data = []
        for i in StemComment.objects.filter(stem_id=stem_id):
            stemData = {'username': i.username, 'content': i.content,
                        'create_time': i.create_time.strftime("%Y-%m-%d %H:%M"), 'agree': i.agree,
                        'disagree': i.disagree, 'nickname': i.nickname,
                        'avatar': User.objects.filter(username=i.username).values('user_image')[0]['user_image']}
            data.append(stemData)
        return JsonResponse({
            'data': data
        }, status=200)
    else:
        return JsonResponse({
            'data': '请求方法错误'
        }, status=400)


# 保存每条评论
@csrf_exempt
def saveStemComment(request):
    if request.method == 'POST':
        today = datetime.datetime.now().strftime("%Y-%m-%d")
        get_stem_id = request.POST['stem_id']
        content = request.POST['content']
        username = request.POST['username']
        my = User.objects.get(username=username)
        my.num_comment = str(1 + int(my.num_comment))
        nickname = my.nickname
        my.save()
        try:
            StemComment.objects.create(stem_id=get_stem_id, nickname=nickname, content=content,
                                       username=username, create_time=today)
        except:
            return JsonResponse({
                'data': '保存错误'
            }, status=200)
        return JsonResponse({
            'data': '评论成功'
        }, status=200)
    else:
        return JsonResponse({
            'data': '请求方法错误'
        }, status=400)


# 查找热门搜索
def searchTimesHot(request):
    if request.method == 'GET':
        get_search_content = StemSearchTimes.objects.all().order_by('-search_times')[:8]
        data = []
        for i in get_search_content:
            content = {'search_content': i.search_content}
            data.append(content)
        return JsonResponse({
            'data': data
        }, status=200)
    else:
        return JsonResponse({
            'data': '请求方法错误'
        }, status=400)


# 用户编写梗
@csrf_exempt
def userSaveStem(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        stem = request.POST.get('stem')
        py = pinyin.get(stem, delimiter=" ")
        year = request.POST.get('year')
        come_from = request.POST.get('come_from')
        content = request.POST.get('content')
        category = request.POST.get('category')
        image = request.FILES.getlist('image')
        num = Stem.objects.all().count() + 1
        idx = 1
        # 创建梗
        Stem.objects.create(stem=stem, pinyin=py, year=year, come_from=come_from,
                            content=content, category=category, author=username)
        get_stem_id = Stem.objects.filter(stem=stem).values('id')[0]['id']
        # 保存梗图
        for i in image:
            # 图片名称
            image_path = './static/stem_image/' + str(num) + "-" + str(idx) + ".jpg"
            # 入库的图片名称
            save_image = 'static/stem_image/' + str(num) + "-" + str(idx) + ".jpg"
            # 保存在梗的文件夹中
            with open(image_path, 'wb') as f:
                for line in i:
                    f.write(line)
            f.close()
            StemImage.objects.create(stem_id=get_stem_id, stem_image=save_image)
            idx += 1
        return JsonResponse({
            'data': 'ok'
        }, status=200)
    else:
        return JsonResponse({
            'data': '请求方法错误'
        }, status=400)


# 推荐相似梗
def categoryComment(request):
    if request.method == 'GET':
        category = request.GET['category']
        data = []
        for i in Stem.objects.filter(category=category).order_by('?')[:8]:
            category_comment = {'stem': i.stem, 'content': i.content, 'stem_id': i.id}
            img = []
            for j in StemImage.objects.filter(stem_id=i.id):
                img.append(j.stem_image.name)
            category_comment['stem_image'] = img
            data.append(category_comment)
        return JsonResponse({
            'data': data
        }, status=200)
    else:
        return JsonResponse({
            'data': '请求方法错误'
        }, status=400)


# 按发布时间获取梗
def getStemInTime(request):
    if request.method == 'GET':
        data = []
        for i in Stem.objects.all().order_by('-create_time')[:18]:
            re_data = {'stem_id': i.id, 'stem': i.stem, 'content': i.content, 'create_time': i.create_time,
                       'author': i.author,
                       'category': i.category}
            img = []
            for j in StemImage.objects.filter(stem_id=i.id):
                img.append(j.stem_image.name)
            re_data['stem_image'] = img
            data.append(re_data)
        return JsonResponse({
            'data': data
        }, status=200)

    else:
        return JsonResponse({
            'data': '请求方法错误'
        }, status=400)
