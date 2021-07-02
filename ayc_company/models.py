from django.db import models
from django.db.models.deletion import CASCADE

class Jean(models.Model): # models 모듈 안에 있는 Model 클래스 상속
    name=models.CharField(max_length=100)
    price=models.CharField(max_length=100)
    material=models.TextField()
    detail=models.TextField()
    image=models.ImageField(upload_to = "anc_company/", blank=True, null=True)
    
    def __str__(self):
        return self.name