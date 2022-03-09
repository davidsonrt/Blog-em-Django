from django.db import models 
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.TextField()
    subtitle = models.TextField()
    text = models.TextField()
    begin_date = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(upload_to='post')
    active = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def _str_(self):
        return str(self.id)

        class Meta:
            db_table = 'post'


class Comentari(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post')
    text = models.TextField()
    begin_date = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')

    def _str_(self):
        return str(self.id)

        class Meta:
            db_table = 'comentari'
