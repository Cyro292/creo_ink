from django.urls import path
from .views import OwnUserDataView, SignupView, UserLoginView

urlpatterns = [
    # Other URL patterns
    path('personal/user/', OwnUserDataView.as_view(), name='own-user-data'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', UserLoginView.as_view(), name='login'),
]
