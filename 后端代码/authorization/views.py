import datetime
import json
import os
import random

import jwt
from PIL import Image
from captcha.helpers import captcha_image_url
from captcha.models import CaptchaStore
from django.core import mail
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import make_password, check_password
from StemEncyclopedia.settings import SECRET_KEY
from userhome.models import User


# 注册
@csrf_exempt
def register(request):
    if request.method == 'POST':
        request_body = request.body
        username = json.loads(request_body).get('username')
        password = json.loads(request_body).get('password')
        answer = json.loads(request_body).get('answer', None)
        hash_key = json.loads(request_body).get('hash_key', None)
        # 验证验证码是否正确
        if not judge_captcha(answer, hash_key):
            return JsonResponse({
                'data': '验证不通过'
            }, status=200)
        # 验证用户是否存在
        get_user = User.objects.filter(username=username)
        if len(get_user) != 0:
            # find_email_code.delete()
            return JsonResponse({
                'data': '用户已存在'
            }, status=200)
        # 密码加密
        password_security = make_password(password, SECRET_KEY)
        # 文件夹命名
        field_name = './static/avatar/' + username
        # 生成文件夹(太难了)
        if not os.path.exists(field_name):
            os.makedirs(field_name)
        # 保存设置为默认图片
        image = Image.open('./static/avatar/1.png')
        # 图片命名
        image_path = './static/avatar/' + username + '/' + username + '.png'
        image.save(image_path)
        # 需要入库的图片名字
        save_image = 'static/avatar/' + username + '/' + username + '.png'
        # 入库
        User.objects.create(username=username, password=password_security, email="", user_image=save_image)
        return JsonResponse({
            'data': '注册成功'
        }, status=200)
    else:
        return JsonResponse({
            'data': '请求方法错误'
        }, status=400)


# 登录
@csrf_exempt
def login(request):
    if request.method == 'POST':
        request_body = request.body
        # 采用json转为字典方式获取账号密码
        username = json.loads(request_body).get('username')
        password = json.loads(request_body).get('password')
        # 验证用户是否存在
        get_user = User.objects.filter(username=username)
        if len(get_user) == 0:
            return JsonResponse({
                'data': '用户不存在'
            }, status=200)
        # 验证用户
        for i in get_user:
            if not check_password(password, i.password):
                return JsonResponse({
                    'data': '账号或者密码错误'
                }, status=200)
        # 创建token
        token_reply = {
            # 过期时间1天
            'exp': datetime.datetime.now() + datetime.timedelta(days=1),
            # 开始时间
            'iat': datetime.datetime.now(),
            # 签名
            'iss': SECRET_KEY,
            # 内容，一般存放该用户id和开始时间
            'data': {
                'username': username,
            },
        }
        # 加密生成字符串
 
        # token = str(jwt.encode(token_reply, 'secret', algorithm='HS256'))
 
        token = str(jwt.encode(token_reply, 'secret', algorithm='HS256'))[2:-1]
        # print(token)
        # print(jwt.encode(token_reply, 'secret', algorithm='HS256'))
        # 保存session登陆状态
        # request.session['username'] = username
        # request.session['is_login'] = 1
        # 返回数据
        return JsonResponse({
            'username': username,
            'token': token,
            'data': '登陆成功'
        }, status=200)
    else:
        return JsonResponse({
            'data': '请求方法错误'
        }, status=400)


# 退出登录
def login_out(request):
    if request.method == 'GET':
        try:
            del request.session['username']
            del request.session['is_login']
        except:
            return JsonResponse({
                'data': '用户未登录'
            }, status=200)
        return JsonResponse({
            'data': '退出成功'
        }, status=200)
    else:
        return JsonResponse({
            'data': '请求方法错误'
        }, status=400)


# 发邮件
def sendEmailCode(request):
    if request.method == 'GET':
        get_email = request.GET['email']
        # username = request.GET['username']
        email_list = [get_email]
        # 创建随机数
        randNumber = random.randint(100000, 1000000)
        now_time = datetime.datetime.now().strftime("%Y-%m-%d")
        # 存session
        # EmailCodeSession.objects.create(code=randNumber, username=username)
        request.session['emailCode'] = randNumber
        # 发送邮件
        returnMessage = "【梗百科】您于<strong>" + now_time + "</strong>注册了用户，此次的验证码是：<strong>" \
                        + str(randNumber) + "</strong>，请不要告诉他人！ "
        mail.send_mail(subject='梗百科注册验证码', message=returnMessage, from_email='2770063826@qq.com',
                       recipient_list=email_list)
        return JsonResponse({
            'data': '邮件发送成功'
        }, status=200, safe=False)
    else:
        return JsonResponse({
            'data': '请求方法错误'
        }, status=400)


# 验证验证码是否为真
def judge_captcha(answer, hash_key):
    if answer and hash_key:
        try:
            get_captcha = CaptchaStore.objects.get(hashkey=hash_key)
            if get_captcha.response == answer.lower():  # 如果验证码匹配
                return True
        except:
            return False
    else:
        return False


# 发送验证码
@csrf_exempt
def getCaptcha(request):
    if request.method == 'GET':
        hash_key = CaptchaStore.generate_key()  # 验证码答案
        image_url = captcha_image_url(hash_key)  # 验证码地址
        captcha = {'hash_key': hash_key, 'image_url': image_url}
        return JsonResponse({
            'data': captcha
        }, status=200)
    else:
        answer = request.POST.get("answer", None)  # 验证码答案
        hash_key = request.POST.get("hash_key", None)  # 用户提交的验证码
        if judge_captcha(answer, hash_key):
            return JsonResponse({
                'data': '验证通过'
            }, status=200)
        else:
            return JsonResponse({
                'data': '验证不通过'
            }, status=200)

