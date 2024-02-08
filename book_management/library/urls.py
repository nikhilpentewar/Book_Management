from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('books', views.BookViewSet)
router.register('authers', views.AuthorViewSet)
router.register('categories', views.CategoryViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('', views.list_books, name = 'list_books'),
    path('dd_book/', views.add_book, name = 'add_book'),
    path('update_book/<int:id>/', views.update_book, name='update_book'),
    path('delete_book/<int:id>/', views.delete_book, name='delete_book'),
    path('add_author/', views.add_author, name='add_author'),
    path('add_category/', views.add_category, name='add_category')
]
