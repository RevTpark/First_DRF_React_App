from django.urls import path
from .views import CustomUserCreate, BlackListTokenView

app_name = "user"

urlpatterns = [
    path("register/", CustomUserCreate.as_view(), name="create_user"),
    path("logout/blacklist/", BlackListTokenView.as_view(), name='blacklist'),

]
