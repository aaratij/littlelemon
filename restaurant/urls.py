from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'users', views.UsersViewSet, basename='user')

urlpatterns = [
    path('index', views.index, name='index'),
    path('', include(router.urls)),
    path('/api-auth', include('rest_framework.urls', namespace='rest_framework')),
    path('menu/', views.MenuItemsView.as_view()),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
]