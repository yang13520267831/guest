from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from sign.models import Event, Guest
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def index(request):
    return render(request, "index.html")


# 登录操作
def login_action(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)  # 登录
            request.session['user'] = username  # 将session信息记录到浏览器中
            # return HttpResponse('login success')
            response = HttpResponseRedirect('/event_manage/')
            # response.set_cookie('user',username,3600)   #添加浏览器cookie
            return response
        else:
            return render(request, "index.html", {'error': 'username or password error'})


# 发布会管理
@login_required
def event_manage(request):
    # username=request.COOKIES.get('user','')
    username = request.session.get('user', '')
    # print(username)
    event_list = Event.objects.all()
    print(event_list)
    return render(request, "event_manage.html", {"user": username, "events": event_list})


# 发布会名称搜索
@login_required
def search_name(request):
    username = request.session.get('user', '')
    search_name = request.GET.get("name", "")
    event_list1 = Event.objects.filter(name__contains=search_name)
    print(event_list1)
    return render(request, "event_manage.html", {"user": username, "events": event_list1})


# 嘉宾管理
@login_required
def guest_manage(request):
    username = request.session.get('user', '')
    guest_list = Guest.objects.all()
    paginator = Paginator(guest_list, 2)
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        contacts = paginator.page(1)
    except EmptyPage:
        contacts = paginator.page(paginator.num_pages)
    return render(request, "guest_manage.html", {"user": username, "guests": contacts})


# 系统退出
@login_required
def logout(request):
    auth.logout(request)
    response = HttpResponseRedirect('/')
    return response


# 签到页面
@login_required
def sign_index(request, eid):
    event = get_object_or_404(Event, id=eid)
    return render(request, 'sign_index.html', {'event': event})


# 签到动作
@login_required
@csrf_exempt
def sign_index_action(request, eid):
    event = get_object_or_404(Event, id=eid)
    phone = request.POST.get('phone', '')
    print(phone)
    result = Guest.objects.filter(phone=phone)
    if not result:
        return render(request, 'sign_index.html', {'event': event, 'hint': 'phone.error'})
    result = Guest.objects.filter(phone=phone, event_id=eid)
    if not result:
        return render(request, 'sign_index.html', {'event': event, 'hint': 'event id or phone error'})
    result = Guest.objects.get(phone=phone, event_id=eid)
    if result.sign:
        return render(request, 'sign_index.html', {'event': event, 'hint': 'user has sign in.'})
    else:
        Guest.objects.filter(phone=phone, event_id=eid).update(sign='1')
        return render(request, 'sign_index.html', {'event': event, 'hint': 'sign in success!', 'guest': result})
