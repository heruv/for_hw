from django.db import models

# Create your models here.

#create table-class

class OnlineShop(models.Model, ): #nasledyem class Moodel
    #create header
    title = models.CharField('header', max_length=128, ) #CharFiekd class simvolnoe pole 
    #about sell
    description = models.TextField('description') #string field
    #cost - ?
    prise = models.DecimalField('prise', max_digits=10, decimal_places=2) #<-- llike a float in Python
    #scidka/scibidi
    auction = models.BooleanField('auction?', help_text="mark can you auction pr or?")
    created_time = models.DateTimeField("create time", auto_now_add=True)
    update_time = models.DateTimeField("update time", auto_now=True)
    
    
    def __str__(self):
        return '%s %s %s' % (f"ID={self.id}" ,self.title, self.prise)
    
    
    class Meta:
        db_table = 'advertisements'
