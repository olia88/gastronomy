from django.db import models

# Create your models here.
class Recipe(models.Model):
    class Meta():
        db_table='recipe'
    recipe_title=models.CharField(max_length=200)
    # recipe_image, vk, facebook
    recipe_ingredients=models.TextField()
    recipe_text=models.TextField()
    recipe_date=models.DateField()
    recipe_likes=models.IntegerField(default=0)

class Comments(models.Model):
    class  Meta():
        db_table='comments'
    comments_text=models.TextField()
    comments_recipe=models.ForeignKey(Recipe)
    comments_date=models.DateField()
