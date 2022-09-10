from django.urls import path

from urlapp.views import HomePage, accPage, goto, logout_page


urlpatterns = [
    path('', HomePage),
    path('acc/', accPage, name='acc'),
    path('logout/', logout_page, name='logout_page'),
    path('<token_id>', goto),
]
