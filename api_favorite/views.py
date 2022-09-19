from django.shortcuts import render
from django.views import generic
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from core.models import Post, Comment, FavoriteForPost, FavoriteForComment


# Create your views here.

class PostList(generic.ListView):
    template_name = 'favorite/post_list.html'
    model = Post


class PostDetail(generic.DetailView):
    template_name = 'favorite/post_detail.html'
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        favorite_for_post_count = self.object.favoriteforpost_set.count()
        # ポストに対するいいね数
        context['favorite_for_post_count'] = favorite_for_post_count
        # ログイン中のユーザーがいいねしたかどうか
        if self.object.favoriteforpost_set.filter(user=self.request.user).exists():
            context['is_user_favorite_for_post'] = True
        else:
            context['is_user_favorite_for_post'] = False
        return context


def favorite_for_post(request):
    post_pk = request.POST.get('post_pk')
    context = {
        'user': f'{request.user.nickName}, '
    }
    post = get_object_or_404(Post, pk=post_pk)
    favorite = FavoriteForPost.object.filter(target=post, user=request.user)

    if favorite.exists():
        favorite.delete()
        context['method'] = 'delete'
    else:
        favorite.create(target=post, user=request.user)
        context['method'] = 'create'

    context['favorite_for_post_count'] = post.favoriteforpost_set.count()

    return JsonResponse(context)


def favorite_for_comment(request):
    comment_pk = request.POST.get('comment_pk')
    context = {
        'user': f'{request.user.nickName}'
    }
    comment = get_object_or_404(Comment, pk=comment_pk)
    favorite = FavoriteForComment.objects.filter(target=comment, user=request.user)
    if favorite.exists():
        favorite.delete()
        context['method'] = 'delete'
    else:
        favorite.create(target=comment, user=request.user)
        context['method'] = 'create'

        context['favorite_for_comment_count'] = comment.favoriteforcomment_set.count()

        return JsonResponse(context)
