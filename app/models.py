import uuid

from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models
from datetime import date


class Post(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    image = models.ImageField(upload_to='media/post/')
    description = models.TextField(blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='posts')

    def __str__(self):
        return f'{self.description}'

    class Meta:
        ordering = ['-created_date']


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    post = models.ForeignKey(Post, on_delete=models.DO_NOTHING, related_name='likes')

    class Meta:
        unique_together = ['user', 'post']

    def save(self, *args, **kwargs):
        self.full_clean()
        super(Like, self).save(*args, **kwargs)


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    post = models.ForeignKey(Post, on_delete=models.DO_NOTHING)


class Following(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='subscribers')
    following = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='followers')

    def __str__(self):
        return f"user: {self.user}| following: {self.following}"

    class Meta:
        unique_together = ['user', 'following']

    def save(self, *args, **kwargs):
        self.full_clean()
        super(Following, self).save(*args, **kwargs)

    def clean(self):

        if self.following == self.user:
            raise ValidationError({'following': 'Вы не можете подписаться на самого себя!'})

        return super().clean()
