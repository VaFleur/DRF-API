from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=512, blank=True)
    category = models.ForeignKey('Category', related_name='posts', on_delete=models.SET_DEFAULT, default='No category')
    body = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    created_by = models.ForeignKey('auth.User', related_name='posts', on_delete=models.CASCADE)

    def __str__(self):
        return f'Post {self.title}'


class Comment(models.Model):
    body = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    created_by = models.ForeignKey('auth.User', related_name='comments', on_delete=models.CASCADE)
    post = models.ForeignKey('Post', related_name='comments', on_delete=models.CASCADE)

    def __str__(self):
        return f'Comment id{self.pk} for post {self.post.title}'


class Category(models.Model):
    category_name = models.CharField(max_length=128)
    category_description = models.TextField()

    def __str__(self):
        return f'Category "{self.category_name}"'
