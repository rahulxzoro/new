from django.urls import path
from . import views
app_name='shop'
urlpatterns = [
    path('',views.home,name='home'),
    path('<slug:c_slug>/',views.home,name='product_by_category'),
    path('detail/<int:id>/',views.detail,name='detail')
]
