from django.db import models
from django.contrib.auth.models import User


# class MyUser(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     assigned_dataset = models.IntegerField()

class Dataset(models.Model):
    name = models.CharField(max_length=64)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)


class Text(models.Model):
    creator = models.CharField(max_length=64)
    text = models.TextField()
    annotated = models.BooleanField(default=False)
    assigned_user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=False, null=True)
    dataset_id = models.ForeignKey(Dataset, on_delete=models.CASCADE, null=True)


class Annotation(models.Model):
    annotator_id = models.ForeignKey(User, on_delete=models.CASCADE)
    text_id = models.ForeignKey(Text, on_delete=models.CASCADE)
    label_1 = models.CharField(max_length=64)
    label_2 = models.CharField(max_length=64)
