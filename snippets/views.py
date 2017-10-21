from django.http import Http404
from django.contrib.auth.models import User
from rest_framework import status,generics,permissions
from rest_framework.response import Response
from rest_framework.reverse import reverse
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from .serializers import UserSerializer
from .permissions import IsOwnerOrReadOnly
from rest_framework import renderers
from rest_framework import viewsets
from rest_framework.decorators import detail_route
# Create your views here.


class SnippetViewSet(viewsets.ModelViewSet):
    '''
    提供list，create，retrieve，update和destroy，以及highlight功能
    '''
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

    @detail_route(renderer_classes=[renderers.StaticHTMLRenderer])
    # 此装饰器可用于添加不适合标准create/ update/ delete样式的任何自定义端点
    def highlight(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    '''
    自动提供list和detail的功能
    '''
    queryset = User.objects.all()
    serializer_class = UserSerializer



# class SnipeetList(APIView):
#     # APIView实际继承django总的view
#     """
#     显示snippets所有数据,'post'创建一个新的snippet
#     """
#     permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
#     def get(self,request,format=None):
#             snippets = Snippet.objects.all()
#             # many=True  用于queryset对象
#             serializer = SnippetSerializer(snippets, many=True)
#             return Response(serializer.data,)
#
#     def  post(self,request,format=None):
#             serializer = SnippetSerializer(data=request.data)
#             if serializer.is_valid():
#                 # .save()是调用SnippetSerializer中的create()方法
#                 serializer.save()
#                 # serializer.data 数据创建成功后保存所有数据
#                 return Response(serializer.data, status=201)
#             # serializer.errors 错误信息
#             return Response(serializer.errors, status=400)
#
#     def perform_create(self, serializer):
#         # 覆盖.perform_create()我们的代码片段视图上的方法
#         # 修改实例保存的管理方式，并处理传入请求或请求的URL中隐含的任何信息
#         serializer.save(owner=self.request.user)
#
#
#
# class SnippetDetail(APIView):
#     """
#     snippetd的改，查，删除
#     """
#     permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly)
#     def get_object(self,pk):
#         try:
#             snippet = Snippet.objects.get(pk=pk)
#         except Snippet.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#
#     def get(self,request,pk,format=None):
#         snippet=self.get_object(pk)
#         serializer = SnippetSerializer(snippet)
#         return Response(serializer.data)
#
#     def put(self,request,pk,format=None):
#         snippet=self.get_object(pk)
#         serializer = SnippetSerializer(snippet, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self,request,pk,format=None):
#         snippet = self.get_object(pk)
#         snippet.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

#
# @api_view(['GET'])
# def api_root(request,format=None):
#     return Response({
#         'users': reverse('user-list', request=request, format=format),
#         'snippets': reverse('snippet-list', request=request, format=format)
#     })




