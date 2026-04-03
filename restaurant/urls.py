from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . import views
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
#router.register(r'users', views.UsersViewSet, basename='user')
router.register(r'tables',views.BookingViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('menu/', views.MenuItemsView.as_view()),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
    #path('message/', views.msg),
    path('booking/', include(router.urls)),
    path('api-token-auth/', obtain_auth_token)
]