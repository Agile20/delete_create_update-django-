from django.db import models

class Post(models.Model):
    user = models.CharField(max_length=127)
    title = models.CharField(max_length=127)
    description = models.TextField()
    raiting = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self) -> str:
        return f'{self.user} создал пост: "{self.title}"'

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comment')
    user = models.CharField(max_length=127)
    text = models.TextField()
    def __str__(self) -> str:
        return self.user