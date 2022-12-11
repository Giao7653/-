import jwt
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from StemEncyclopedia.settings import SECRET_KEY
from stem.models import StemComment, Stem, StemImage
from userhome.models import User


# 获取用户信息
def getUserInfo(request):
    if request.method == 'GET':
        get_token = request.GET.get('token', 0)
        get_username = request.GET['username']
        data = {}
        # 身份验证token
        if get_token != 0:
            try:
                res = jwt.decode(request.GET['token'], 'secret', issuer=SECRET_KEY, algorithms=['HS256'])
                if res['data']['username'] != get_username:
                    return JsonResponse({
                        'data': '身份验证失败，请重新登录'
                    }, status=200)
            except:
                return JsonResponse({
                    'data': "身份验证失败，请重新登录"
                }, status=200)

        for i in User.objects.filter(username=get_username):
            data['avatar'] = i.user_image.name
            data['username'] = i.username
            data['email'] = i.email
            data['nickname'] = i.nickname
            data['introduction'] = i.introduction
            data['num_views'] = i.num_views
            data['num_comment'] = i.num_comment
        return JsonResponse({
            'data': data
        }, status=200)

    else:
        return JsonResponse({
            'data': '请求方法错误'
        }, status=400)


# 更新用户头像
@csrf_exempt
def updateAvatar(request):
    if request.method == 'POST':
        get_avatar = request.FILES.get('file')
        username = request.POST['username']
        # 图片名称
        image_path = './static/avatar/' + username + '/' + get_avatar.name + ".png"
        # 入库的图片名称
        save_image = 'static/avatar/' + username + '/' + get_avatar.name + ".png"
        # 保存在用户的文件夹中
        with open(image_path, 'wb') as f:
            for line in get_avatar:
                f.write(line)
        f.close()
        # 更新User数据库
        User.objects.filter(username=username).update(user_image=save_image)
        return JsonResponse({
            'data': "ok"
        }, status=200)
    else:
        return JsonResponse({
            'data': '请求方法错误'
        }, status=400)


# 更新用户信息
@csrf_exempt
def updateUserinfo(request):
    if request.method == 'POST':
        username = request.POST['username']
        get_nickname = request.POST['nickname']
        get_email = request.POST['email']
        get_introduction = request.POST['introduction']
        StemComment.objects.filter(username=username).update(nickname=get_nickname)
        User.objects.filter(username=username).update(nickname=get_nickname, email=get_email,
                                                      introduction=get_introduction)
        return JsonResponse({
            'data': "ok"
        }, status=200)
    else:
        return JsonResponse({
            'data': '请求方法错误'
        }, status=400)


# 身份验证
def authenticationToken(request):
    if request.method == 'GET':
        get_token = request.GET.get('token', 0)
        get_username = request.GET.get('username', 0)
        if get_token != 0:
            try:
                res = jwt.decode(get_token, 'secret', issuer=SECRET_KEY, algorithms=['HS256'])
                if res['data']['username'] != get_username:
                    return JsonResponse({
                        'data': '身份验证失败，请重新登录'
                    }, status=200)
            except:
                return JsonResponse({
                    'data': "身份验证失败，请重新登录"
                }, status=200)
        return JsonResponse({
            'data': '验证成功'
        }, status=200)
    else:
        return JsonResponse({
            'data': '请求方法错误'
        }, status=400)


# 查询某人创作的梗
def queryMyStem(request):
    if request.method == 'GET':
        username = request.GET['username']
        data = []
        for i in Stem.objects.filter(author=username):
            re_data = {'stem_id': i.id, 'stem': i.stem, 'content': i.content, 'create_time': i.create_time,
                       'author': i.author, 'category': i.category}
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
