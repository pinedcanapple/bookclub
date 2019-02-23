from django.urls import path
from django.conf import settings
from django.contrib.auth import views as v
from django.conf.urls.static import static
from django.conf.urls import url,include
from . import views

urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('book/<int:pk>/', views.book_detail, name='book_detail'),
    path('post/new', views.post_new, name='post_new'),
    path('book/<int:pk>/edit/', views.book_edit, name='book_edit'),
    path('book/<pk>/remove/', views.book_remove, name='book_remove'),
    path('accounts/login/', v.LoginView.as_view(), name='login'),
    path('accounts/logout/', v.LogoutView.as_view(next_page='/'), name='logout'),
    path('book/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
    path('book/<int:pk>/remove/', views.comment_remove, name='comment_remove'),
    path('signup/', views.signup, name='signup'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
