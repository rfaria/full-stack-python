from django.db import models

# Create your models here.

class Feature(models.Model):
    name = models.CharField(max_length=100)
    details = models.TextField(max_length=1000)


# This class has a naive approach
# class Feature():
#     id: int
#     name: str
#     details: str
#     is_true: bool

# if __name__ == '__main__':
#     feat = Feature()
#     feat.id = 0
#     feat.name = 'test'
#     feat.details = 'this is a test'

#     print(feat.id, feat.name, feat.details)