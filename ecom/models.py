from django.db import models

class Categories(models.Model):
    title = models.CharField(max_length=255, blank=True, default="")
    is_active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.id

    class Meta:
        db_table = "categories"

class Products(models.Model):
    title = models.CharField(max_length=255, blank=True, default="")
    description = models.CharField(max_length=255, blank=True, default="")
    price  = models.CharField(max_length=255, blank=True, default="")
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.id

    class Meta:
        db_table = "products"
        
        
class Review(models.Model):
    products = models.ForeignKey(Products, on_delete = models.CASCADE)
    rating = models.IntegerField(default = 0)
    pros = models.CharField(max_length=522, blank=True, default="")
    corns = models.CharField(max_length=522, blank=True, default="")
    review = models.CharField(max_length=522, blank=True, default="")
    def __unicode__(self):
        return self.id

    class Meta:
        db_table = "review"