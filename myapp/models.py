from django.db import models

class Cafe(models.Model):

    product_name = models.CharField(max_length=25) #수업에서는 20
    product_price = models.IntegerField() 
    
    # 여기서 추가로 생각해볼만한 점은, 품절이 된다면? integerfield로 쓰면 안되지 않을까라는 생각!


    


    
