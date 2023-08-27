from django.urls import path
from .views import OwnUserDataView

urlpatterns = [
    # Other URL patterns
    path('personal/user/', OwnUserDataView.as_view(), name='own-user-data'),
]
