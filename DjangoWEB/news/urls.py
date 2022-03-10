from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # path('', index, name='home')
    path('', HomeNews.as_view(), name='home'),
    # path('category/<int:category_id>/', get_category, name='category')
    path('category/<int:category_id>/', NewsByCategory.as_view(extra_context={'title':'Какой то титл'}), name='category'),
    path('news/<int:news_id>/', view_news, name='view_news'),
    path('news/add-news', add_news, name='add_news')
]