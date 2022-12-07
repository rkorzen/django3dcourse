from django.db import models

# Create your models here.



class Math(models.Model):

    OPERATION_CHOICES = (
        ("sum", "sum"),
        ("sub", "sub"),
        ("div", "div"),
        ("mul", "mul"),
    )

    op = models.CharField(verbose_name="Operation", max_length=3, choices=OPERATION_CHOICES)
    a = models.IntegerField()
    b = models.IntegerField()
    result = models.FloatField()
    comment = models.TextField(null=True, blank=True)


    def __str__(self):
        return f"op: {self.op} a: {self.a} b: {self.b}"


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    is_published = models.BooleanField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"({self.id}) {self.title[:50]}"
