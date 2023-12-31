from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . import views
from rest_framework.authtoken.views import obtain_auth_token
router = DefaultRouter()
router.register(r'tables', views.BookingViewSet)

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('menu/', views.menu, name="menu"),
    path('menuitem/', views.MenuItemView.as_view(), name="menu_item_list"),
    path('menuitem/<int:pk>/', views.SingleMenuItemView.as_view(), name="single_menu_item"),
    path('book/', views.book, name="book"),
    path('restaurant/booking/', include(router.urls)),
    path('api-token-auth/',obtain_auth_token),
    path('message/', views.msg),
]