from django.db import models
from django.contrib.auth.models import User




  
class userProfile(models.Model):
    
    level=(('دیپلم','دیپلم'),('کاردانی','کاردانی'),('کارشناسی','کارشناسی'),
           ('فوق لیسانس','فوق لیسانس'),('دکتری','دکتری'),('سایر','سایر'))
    
    user=models.OneToOneField(User,on_delete=models.CASCADE,blank=True,null=True)
    phone_number=models.CharField(max_length=11,null=True,blank=True)
    education_level=models.CharField(max_length=50,choices=level,null=True,blank=True)
    address=models.CharField(max_length=500,blank=True,null=True)
    created=models.DateField(auto_now_add=True)
    image=models.ImageField(blank=True,null=True,upload_to="user_app/images/",
                            default="user_app/images/default.jpg")
    def __str__(self):
        return f'{self.user.username}'
