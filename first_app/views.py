
from .models import Article
from django.views import generic
from .forms import ArticleForm, CommentCreateForm

class IndexView(generic.ListView):
    model = Article
    template_name = 'index.html'

    def get_queryset(self):
        return Article.objects.order_by('-created_at')[:5]

class ArticleView(generic.DetailView):
    model = Article
    template_name = 'article.html'

class NewView(generic.CreateView):
    form_class = ArticleForm
    template_name = 'form.html'
    success_url = '/'

class CommentView(generic.CreateView):
    model = Article
    form_class = CommentCreateForm
    template_name = 'comment.html'

    def form_valid(self, form):
        post_pk = self.kwargs['pk']
        post = get_object_or_404(Post, pk=post_pk)
        comment = form.save(commit=False)
        comment.article = post   #Postモデルのidが「post_pk」のもの＝2行目の部分
        comment.save()
        return redirect('first_app:article', pk=post_pk)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post'] = get_object_or_404(Post, pk=self.kwargs['pk'])
        return context

 