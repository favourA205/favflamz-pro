from django.urls import path
from .views import home, reg_page, page1, instruction_page,addUser,newpage,syllabus


urlpatterns = [
    path('', home, name='home'),
    path('signup/', reg_page, name='reg_page'),
    path('addUser/', addUser, name='addUser'),
    path('instruct/page1/', page1, name='page1'),
    path('instruct/', instruction_page, name=' instruction_page'),
    path('instruct/page1/new-page/', newpage, name=' newpage'),
    path('syllabus/', syllabus, name=' syllabus'),
]