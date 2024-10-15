from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)  
    # ForeignKey는 참조대상(붙잡고 있는 대상)이 있어야 함(여기서는 Article) 
    # 참조대상이 없으면(on_delete) ~ 
    content = models.CharField(max_length=50)