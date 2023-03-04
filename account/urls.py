from django.urls import path, include
from account.views import LoginView, logout, AccountListView, AccountDelView, AccountAddView, AccountAdd1View, \
    AccountEditView, AccountChangePassView, AccountInfoView

app_name = 'account'

urlpatterns = [
    # admin_views 管理员操作url
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', logout, name='logout'),
    path('list/', AccountListView.as_view(), name='list'),
    path('del/', AccountDelView.as_view(), name='del'),
    path('add/', AccountAddView.as_view(), name='add'),
    path('add1/', AccountAdd1View.as_view(), name='add1'),
    path('edit/', AccountEditView.as_view(), name='edit'),
    path('change/pass/', AccountChangePassView.as_view(), name='changepass'),
    path('info/', AccountInfoView.as_view(), name='info'),

]