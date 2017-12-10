"""
database structure for food orders.
"""


from django.db import models

#one table for each food outlet
class hungercycle(models.Model):
    name = models.CharField(max_length=100)   #column heading= name
    order = models.CharField(max_length=300)
    status = models.CharField(max_length=100)

    def __str__(self):    #describes what to do if print statement is used with item of this class
        return(self.name + "---:  " + self.order)

class hungercycle_menu(models.Model):
    foodItem = models.CharField(max_length = 300) #Item name
    foodPrice = models.IntegerField() #Cost of the item
    def __str__(self):
        return self.foodItem + str("------")+ str(self.foodPrice)

class foodjunction(models.Model):
    name= models.CharField(max_length=5000)
    order= models.CharField(max_length=300)
    status= models.CharField(max_length=100)
    def __str__(self):
        return(self.name+"---:  "+ self.order)

class foodjunction_menu(models.Model):
    foodItem = models.CharField(max_length = 300) #Item name
    foodPrice = models.IntegerField() #Cost of the item

    def __str__(self):
        return self.foodItem + str("------")+ str(self.foodPrice)