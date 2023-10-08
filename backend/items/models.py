import uuid
from django.db import models
from account.models import User
# Create your models here.

class MajorCategory(models.Model):
    name = models.CharField(max_length=10)

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,

        }
    
    def __str__(self):
        return self.name.title()

class MinorCategory(models.Model):
    category = models.ForeignKey(MajorCategory, on_delete=models.DO_NOTHING, related_name='minorcategory')
    name = models.CharField(max_length=15)

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'category': self.category.name

        }
    def __str__(self):
        return (f"{self.category.name} {self.name.title()}")
    
class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, auto_created=True, unique=True, editable=False, null=False)
    category = models.ForeignKey(MinorCategory, on_delete=models.DO_NOTHING, related_name='categoryItem', null=False)
    owner = models.ForeignKey(User, related_name='userItems', on_delete=models.DO_NOTHING, null=False)
    description = models.CharField(max_length=64, default='')
    name = models.CharField(max_length=64, default="Has no name")

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name.title(),
            'category': self.category.name,
            'description': self.description
        }
    
    def __str__(self):
            return self.name