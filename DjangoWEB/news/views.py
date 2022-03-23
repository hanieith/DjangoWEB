from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import News, Category
from .forms import NewsForm
from django.urls import reverse_lazy
from .utils import MyMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator


class HomeNews(MyMixin, ListView):
    model = News
    template_name = 'news/home_news_list.html'
    context_object_name = 'news'
    mixin_prop = 'hello world'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.get_upper('Главная страница')
        context['mixin_prop'] = self.get_prop()
        return context

    def get_queryset(self):
        return News.objects.filter(is_published=True).select_related('category')


class NewsByCategory(MyMixin, ListView):
    model = News
    template_name = 'news/home_news_list.html'
    context_object_name = 'news'
    allow_empty = False

    def get_queryset(self):
        return News.objects.filter(category_id=self.kwargs['category_id'], is_published=True).select_related('category')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(pk=self.kwargs['category_id'])
        return context


def get_category(request, category_id):
    news = News.objects.filter(category_id=category_id)
    category = Category.objects.get(pk=category_id)
    context = {'news': news,
               'category': category}
    return render(request, template_name='news/category.html', context=context)


# def add_news(request):
#   if request.method == "POST":
#      form = NewsForm(request.POST)
#     if form.is_valid():
#        # news = News.objects.create(**form.cleaned_data)
#       news = form.save()
#      return redirect(news)
# else:
#   form = NewsForm()
# return render(request, template_name='news/add_news.html', context={"form": form})

def test(request):
    objects = ['asd', 'asd1', 'asd2', 'asd3', 'asd4', 'asd5', 'asd6', 'asd7']
    paginator = Paginator(objects, 2)
    page_num = request.GET.get('page', 1)
    page_objects = paginator.get_page(page_num)
    return render(request, 'news/test.html', {'page_obj':page_objects})


class ViewNews(DetailView):
    model = News
    context_object_name = 'news_item'
    paginate_by = 5
    # template_name = 'news/news_detail.html'
    # pk_url_kwarg = 'news_id'


class CreateNews(LoginRequiredMixin, CreateView):
    form_class = NewsForm
    template_name = 'news/add_news.html'
    success_url = reverse_lazy('home')
    login_url = '/admin'
