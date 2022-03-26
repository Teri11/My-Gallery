from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=200 , unique=True)


    def __str__(self):
        return self.name

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()


class Picture(models.Model):
    image = models.ImageField(upload_to ='gallery',blank =False)
    
    description = models.TextField()
   
    date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
 
    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    @classmethod
    def search_by_category(cls, category):
        images = cls.objects.filter(category__name__icontains=category)
        return images
        
    def __str__(self):
        return self.description