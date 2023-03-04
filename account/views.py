from django.shortcuts import render

# Create your views here.
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.core.paginator import Paginator, InvalidPage, EmptyPage, PageNotAnInteger
from django.http import JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views import View

from account.models import UserProfile


class LoginView(View):
    def get(self, request):
        return render(request, 'account/login.html')

    def post(self, request):
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")
        if username and password:
            user = auth.authenticate(username=username, password=password)
            if user:
                if user.is_active is True:
                    userfile = UserProfile.objects.get(user=user)
                    userfile.login_count = userfile.login_count + 1
                    userfile.save()
                    auth.login(request, user)
                    to_url = reverse('index')
                    return JsonResponse(data={'code': 2001, 'msg': 'Login success', 'data': to_url})
                else:
                    return JsonResponse(data={'code': 4001, 'msg': 'Account Banned'})
            else:
                return JsonResponse(data={'code': 4001, 'msg': 'Username or password is wrong'})
        else:
            return JsonResponse(data={'code': 4001, 'msg': 'Username or password should not be empty'})


def logout(request):
    to_url = reverse('account:login')
    if request.user.is_authenticated:
        auth.logout(request)
        return redirect(to_url)
    else:
        return redirect(to_url)


@method_decorator(login_required, name='dispatch')
class AccountListView(View):
    def get(self, request):
        kw = request.GET.get("kw", None)
        lst = User.objects.all().exclude(id=request.user.id).order_by('-id')
        if kw:
            lst = lst.filter(userprofile__nickname__icontains=kw)
        pn = request.GET.get("pn", 1)
        try:
            pn = int(pn)
        except:
            pn = 1
        paginator = Paginator(lst, 6)
        try:
            lst = paginator.page(pn)
        except (InvalidPage, PageNotAnInteger) as e:
            lst = paginator.page(1)
        except EmptyPage as e:
            print(e)
        if lst.paginator.num_pages >= 5:
            if pn <= 2:
                start = 1
                end = 6
            elif pn > lst.paginator.num_pages - 2:
                start = lst.paginator.num_pages - 4
                end = lst.paginator.num_pages + 1
            else:
                start = pn - 2
                end = pn + 3
        else:
            start = 1
            end = lst.paginator.num_pages + 1
        numbers = range(start, end)
        context = {
            'lst': lst,
            'count': paginator.count,
            'numbers': numbers,
            'pn': pn,
        }
        return render(request, 'account/list.html', context=context)


@method_decorator(login_required, name='dispatch')
class AccountDelView(View):
    def get(self, request):
        _id = request.GET.get("_id", "")
        try:
            user = User.objects.get(id=_id)
            user_info = UserProfile.objects.get(user=user)
            user_info.delete()
            user.delete()
        except Exception as e:
            print(e)
            return JsonResponse(data={'code': 4001, 'msg': 'DELETE SUCCESS'})
        return JsonResponse(data={'code': 2001, 'msg': 'DELETE FAILED'})


@method_decorator(login_required, name='dispatch')
class AccountAddView(View):
    def get(self, request):
        return render(request, 'account/add.html')

    def post(self, request):
        username = request.POST.get("username", None)
        password = request.POST.get("password", None)
        email = request.POST.get("email", None)
        is_active = request.POST.get("is_active", None)

        nickname = request.POST.get("nickname", None)
        sex = request.POST.get("sex", None)
        phone = request.POST.get("phone", None)
        type = request.POST.get("type", None)

        user = User.objects.all().filter(username=username).count()
        if user == 0:
            user_info = {
                'username': username,
                'password': make_password(password),
                'email': email,
                'is_active': int(is_active),
            }
            try:
                user = User.objects.create(**user_info)
                print(user.email)
                UserProfile.objects.create(nickname=nickname, sex=sex, phone=phone, user=user, type=type).save()
            except Exception as e:
                print(e)
                return JsonResponse(data={'code': 4001, 'msg': 'Created'})
            return JsonResponse(data={'code': 2001, 'msg': 'Fail to create'})
        else:
            return JsonResponse(data={'code': 4001, 'msg': 'Already exist'})


@method_decorator(login_required, name='dispatch')
class AccountAdd1View(View):
    def get(self, request):
        return render(request, 'account/add1.html')


@method_decorator(login_required, name='dispatch')
class AccountEditView(View):
    def get(self, request):
        _id = request.GET.get("_id", "")
        model = User.objects.get(id=_id)
        return render(request, 'account/edit.html', context={"model": model})

    def post(self, request):
        _id = request.POST.get("_id", "")
        password = request.POST.get("password", None)
        email = request.POST.get("email", None)
        is_active = request.POST.get("is_active", None)
        nickname = request.POST.get("nickname", None)
        sex = request.POST.get("sex", None)
        phone = request.POST.get("phone", None)
        type = request.POST.get("type", None)
        try:
            User.objects.all().filter(id=_id).update(password=make_password(password), is_active=is_active, email=email)
            UserProfile.objects.filter(user_id=_id).update(nickname=nickname, sex=sex, phone=phone, type=type)
        except Exception as e:
            print(e)
            return JsonResponse(data={'code': 4001, 'msg': 'Change failed'})
        return JsonResponse(data={'code': 2001, 'msg': 'Change success'})


@method_decorator(login_required, name='dispatch')
class AccountChangePassView(View):
    def get(self, request):
        model = User.objects.get(id=request.user.id)
        return render(request, 'account/changepass.html', context={"model": model})

    def post(self, request):
        password = request.POST.get("password", None)
        try:
            User.objects.all().filter(id=request.user.id).update(password=make_password(password))
        except Exception as e:
            print(e)
            return JsonResponse(data={'code': 4001, 'msg': 'Change failed'})
        return JsonResponse(data={'code': 2001, 'msg': 'Change success'})


@method_decorator(login_required, name='dispatch')
class AccountInfoView(View):
    def get(self, request):
        return render(request, 'account/info.html')
