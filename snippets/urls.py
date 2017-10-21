from django.conf.urls import url,include
from snippets.views import SnippetViewSet,UserViewSet
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import renderers
from rest_framework.routers import DefaultRouter
from snippets import views


# 创建一个router类，注册snippets，users相应的视图集
router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet)
router.register(r'users', views.UserViewSet)


snippet_list = SnippetViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

snippet_detail = SnippetViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

snippet_highlight = SnippetViewSet.as_view({
    'get': 'highlight'
}, renderer_classes=[renderers.StaticHTMLRenderer])

user_list = UserViewSet.as_view({
    'get': 'list'
})

user_detail = UserViewSet.as_view({
    'get': 'retrieve'
})

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

]


# urlpatterns = format_suffix_patterns([
#     url(r'^snippets/$', snippet_list,name='snippet-list'),
#     # 详情页
#     url(r'^snippets/(?P<pk>[0-9]+)/$',snippet_detail,name='snippet-detail'),
#     # 高亮视图
#     url(r'^snippets/(?P<pk>[0-9]+)/highlight/$', snippet_highlight,name='snippet-highlight'),
#     url(r'^users/$', user_list,name='user-list'),
#     url(r'^users/(?P<pk>[0-9]+)/$', user_detail,name='user-detail'),
#     url(r'^$', api_root),
#
# ])
# # urlpatterns = format_suffix_patterns(urlpatterns)
# urlpatterns += [
#     url(r'^api-auth/', include('rest_framework.urls',
#                                namespace='rest_framework')),
# ]