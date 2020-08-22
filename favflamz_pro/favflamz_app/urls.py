from django.urls import path
from .views import home, reg_page, page1, instruction_page,addUser,chemistry_page


urlpatterns = [
    path('', home, name='home'),
    path('signup/', reg_page, name='reg_page'),
    path('addUser/', addUser, name='addUser'),
    path('instruct/page1/', page1, name='page1'),
    path('instruct/', instruction_page, name=' instruction_page'),
    path('instruct/page1/chem-page/', chemistry_page, name=' chemistry_page'),

]