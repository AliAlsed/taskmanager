from django.db import models
from django.contrib.auth.models import User
# each task can take more user


class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    # image -> url
    image = models.ImageField(null=True, blank=True)
    # image = models.ImageField(default='default.jpg')
    salary = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    department = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.user}"


class Task(models.Model):
    user = models.ManyToManyField(User)
    task_name = models.CharField(max_length=200)
    task_description = models.CharField(max_length=200)
    start_date = models.DateTimeField('start_date')
    due_date = models.DateTimeField('due date')
    status = models.CharField(max_length=265, choices=(
        ('1', 'staging'), ('2', 'in progress'), ('3', 'test'), ('4', 'in review'), ('5', 'closed')))

    def __str__(self):
        return self.task_name

    def user_names(self):
        return ' , '.join([a.username for a in self.user.all()])


class Review(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()


class News(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    short_description = models.CharField(max_length=100)
    Author = models.CharField(max_length=100)
    Image = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.title
