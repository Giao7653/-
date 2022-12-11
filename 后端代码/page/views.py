from django.core.paginator import Paginator
from django.http import JsonResponse

from stem.models import Stem, StemImage, StemSearchTimes


# 所有梗分页
def allStemPage(request):
    if request.method == 'GET':
        page_num = request.GET.get('page_num', 1)
        all_stem = Stem.objects.all()
        count = all_stem.count()
        # 分页，一页三个数
        paginator = Paginator(all_stem, 10)
        # 查询具体页码
        this_page = paginator.page(int(page_num))
        # 返回数据
        pageData = {}
        data = []
        pageData['sum'] = count
        for i in this_page:
            stemData = {'stem_id': i.id, 'stem': i.stem, 'pinyin': i.pinyin,
                        'come_from': i.come_from, 'content': i.content, 'hot': i.hot}
            data.append(stemData)
        pageData['data'] = data
        # 增加前后页码
        if this_page.has_previous():
            pageData['before_page'] = this_page.previous_page_number()
        if this_page.has_next():
            pageData['next_page'] = this_page.next_page_number()
        return JsonResponse({
            'data': pageData
        }, status=200)
    else:
        return JsonResponse({
            'data': '请求方法错误'
        }, status=400)


# 某年所有梗分页
def xYearStemPage(request):
    if request.method == 'GET':
        get_year = request.GET['year']
        page_num = request.GET.get('page_num', 1)
        x_year_stem = Stem.objects.filter(year=get_year).order_by('-hot')
        count = x_year_stem.count()
        # 分页，一页3个数
        paginator = Paginator(x_year_stem, 10)
        # 查询具体页码
        this_page = paginator.page(int(page_num))
        # 返回数据
        pageData = {}
        data = []
        pageData['sum'] = count
        for i in this_page:
            stemData = {'stem_id': i.id, 'stem': i.stem, 'hot': i.hot}
            data.append(stemData)
        pageData['data'] = data
        # 增加前后页码
        if this_page.has_previous():
            pageData['before_page'] = this_page.previous_page_number()
        if this_page.has_next():
            pageData['next_page'] = this_page.next_page_number()
        return JsonResponse({
            'data': pageData
        }, status=200)
    else:
        return JsonResponse({
            'data': '请求方法错误'
        }, status=400)


# 按发布时间获取梗
def getStemInTime(request):
    if request.method == 'GET':
        get_page = request.GET['page_num']
        get_stems = Stem.objects.all().order_by('-create_time')
        if get_stems.count() / 18 < float(get_page):
            return JsonResponse({
                'data': '页数超出范围'
            }, status=200)
        # 分页，一页3个数
        paginator = Paginator(get_stems, 18)
        # 查询具体页码
        this_page = paginator.page(int(get_page))
        # 返回数据
        data = []
        for i in this_page:
            re_data = {'stem_id': i.id, 'stem': i.stem, 'content': i.content, 'create_time': i.create_time,
                       'author': i.author,'category': i.category}
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


