from . import views
from django.urls import path
from django.contrib import admin
from .views import PostCreate

app_name = 'hobbycentre'

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('admin/', admin.site.urls),
    path('create/', PostCreate.as_view(), name='create_post'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('<slug:slug>/edit/', views.post_edit, name='edit_post'),
    path('<slug:slug>/delete/', views.post_delete, name='delete_post'),

]


"""
app_name = 'hobbycentre'

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('polls/', views.polls_main, name='polls_main'),
    path('polls/<int:question_id>/', views.polls_detail, name='polls_detail'),
    path('polls/<int:question_id>/results/', views.polls_results, name='polls_results'),
    path('polls/<int:question_id>/vote/', views.vote, name='vote'),
]

<a class="nav-link active" aria-current="page" href="{% url 'hobbycentre:polls_main' %}">Polls</a>
"""
