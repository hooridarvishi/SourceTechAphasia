from django.db import models

class Text(models.Model):
    x = models.TextField()
    y = models.TextField()
    z = models.TextField()
    m = models.TextField()

    def __str__(self):
        return f"{self.x}, {self.y}, {self.z}, {self.m}"


# برای  عکسای گالری است
class Image(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.image.url

class Image1(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.image.url



# مصدر فعل را نوشتن
class Note(models.Model):
    content = models.CharField(max_length=320 , blank=True , null=True)
    deleted = models.BooleanField(default=False)
    verb_simple_second_step=models.CharField(max_length=320 , blank=True , null=True)
    def __str__(self):
        return self.content
#     **********
# خود فعل مصدر


class Post(models.Model):
    content_verb = models.CharField(max_length=100, blank=True , null=True)
    is_deleted = models.BooleanField(default=False)
    verb_simple_second_step=models.CharField(max_length=320 , blank=True , null=True)
    subject=models.CharField(max_length=320 , blank=True , null=True)
    text_mafool=models.CharField(max_length=100, blank=True , null=True)
    pre_position=models.CharField(max_length=100, blank=True , null=True)
    pre_adverb=models.CharField(max_length=100, blank=True , null=True)
    adverb=models.CharField(max_length=100, blank=True , null=True)
    def __str__(self):
        return self.content_verb


class Photo(models.Model):
    image = models.ImageField(upload_to='photos/')
    is_deleted = models.BooleanField(default=False)

    def str(self):
        return self.image.name





