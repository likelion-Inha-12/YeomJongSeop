
import json
from django.http import JsonResponse
from .models import *
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from rest_framework.decorators import api_view

from rest_framework import status
from django.http import JsonResponse, HttpResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView,View
from .serializers import PostSerializer



def create_post(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        title = data.get('title')
        content = data.get('content')

        post = Post(
            title = title,
            content = content
        )
        post.save()
        return JsonResponse({'message':'success'})
    return JsonResponse({'message':'POST 요청만 허용됩니다.'})

def get_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    data = {
        'id': post.pk,
        '제목': post.title,
        '내용': post.content,
        '메시지': '조회 성공'
    }
    return JsonResponse(data, status=200)

def delete_post(request, pk):
    if request.method == 'DELETE':
        post = get_object_or_404(Post, pk=pk)
        post.delete()
        data = {
            "message" : f"id: {pk} 포스트 삭제 완료"
        }
        return JsonResponse(data, status=200)
    return JsonResponse({'message':'DELETE 요청만 허용됩니다.'})
    return JsonResponse({'message':'DELETE 요청만 허용됩니다.'})



def get_comment(request, post_id):
    if request.method == 'GET':
        post = get_object_or_404(Post, pk=post_id)
        comment_list = post.comments.all()
        return HttpResponse(comment_list, status=200)
    
@api_view(['POST'])
def create_post_v2(request):
    post = Post(
        title = request.data.get('title'),
        content = request.data.get('content')
    )
    post.save()

    message = f"id: {post.pk}번 포스트 생성 성공"
    return Response(data = None, message = message, status = status.HTTP_201_CREATED)

class PostApiView(APIView):

    def get_object(self, pk):
        post = get_object_or_404(Post, pk=pk)
        return post
    def get(self, request, pk):
        post = self.get_object(pk)

        postSerializer = PostSerializer(post)
        message = f"id: {post.pk}번 포스트 조회 성공"
        return Response(data = postSerializer.data, message = message, status = status.HTTP_200_OK)

    def delete(self, request, pk):
        post = self.get_object(pk)
        post.delete()

        
        message = f"id: {pk}번 포스트 삭제 성공"
        return Response(message = message, status = status.HTTP_200_OK) 
    


class LikePostView(View):
    def post(self, request, *args, **kwargs):
        user_id = request.POST.get('user_id')
        post_id = request.POST.get('post_id')

        user = Member.objects.get(id=user_id)
        post = Post.objects.get(id=post_id)

        UserPost.objects.create(user=user, post=post)

        return JsonResponse({}, status=204)

class PostLikeCountView(View):
    def get(self, request, *args, **kwargs):
        post_id = request.GET.get('post_id')
        post = Post.objects.get(id=post_id)

        like_count = post.likers.count()

        return JsonResponse({'like_count': like_count})
    
class PostListByCommentCountView(View):
    def get(self, request, *args, **kwargs):
        posts = Post.objects.annotate(comment_count=models.Count('comments')).order_by('-comment_count')

        post_list = [str(post) for post in posts]

        return JsonResponse({'post_list': post_list})