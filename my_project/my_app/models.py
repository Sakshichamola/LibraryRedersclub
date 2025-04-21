from django.db import models
from datetime import date


class Popular(models.Model):
    image = models.ImageField(upload_to='popular_images/')
    title = models.CharField(max_length=255)  # Changed 'title' to 'name'
    date = models.DateField(default=date.today)  # Stores the created date
    rating = models.DecimalField(max_digits=2, decimal_places=1, default=0.0)  # Example: 4.5 stars
    readers_count = models.PositiveIntegerField(default=0)
    sub_content = models.TextField(max_length=500)
    price1 = models.DecimalField(max_digits=10, decimal_places=2, default=999)
    price2 = models.DecimalField(max_digits=10, decimal_places=2, default=999)
    price3 = models.DecimalField(max_digits=10, decimal_places=2, default=999)
    price4 = models.DecimalField(max_digits=10, decimal_places=2, default=990)

    def str(self):
        return self.name

class New_Arrivals(models.Model):
    image = models.ImageField(upload_to='new_arrivals_images/')
    title= models.CharField(max_length=255)  # Changed 'title' to 'name'
    date = models.DateField(default=date.today)  # Stores the created date
    rating = models.DecimalField(max_digits=2, decimal_places=1, default=0.0)  # Example: 4.5 stars
    readers_count = models.PositiveIntegerField(default=0)  # Number of readers
    sub_content = models.TextField(max_length=500)
    price1 = models.DecimalField(max_digits=10, decimal_places=2, default=999)
    price2 = models.DecimalField(max_digits=10, decimal_places=2, default=999)
    price3 = models.DecimalField(max_digits=10, decimal_places=2, default=999)
    price4 = models.DecimalField(max_digits=10, decimal_places=2, default=990)


class Lifestyles(models.Model):
    image = models.ImageField(upload_to='lifestyles_images/')
    title = models.CharField(max_length=255)  # Changed 'title' to 'name'
    date = models.DateField(default=date.today)  # Stores the created date
    rating = models.DecimalField(max_digits=2, decimal_places=1, default=0.0)  # Example: 4.5 stars
    readers_count = models.PositiveIntegerField(default=0)  # Number of readers
    sub_content = models.TextField(max_length=500)
    price1 = models.DecimalField(max_digits=10, decimal_places=2, default=999)
    price2 = models.DecimalField(max_digits=10, decimal_places=2, default=999)
    price3 = models.DecimalField(max_digits=10, decimal_places=2, default=999)
    price4 = models.DecimalField(max_digits=10, decimal_places=2, default=990)



class Entertainment(models.Model):
    image = models.ImageField(upload_to='entertainment_images/')
    title= models.CharField(max_length=255)  # Changed 'title' to 'name'
    date = models.DateField(default=date.today)  # Stores the created date
    rating = models.DecimalField(max_digits=2, decimal_places=1, default=0.0)  # Example: 4.5 stars
    readers_count = models.PositiveIntegerField(default=0)  # Number of readerssub_content = models.TextField()
    sub_content = models.TextField(max_length=500)
    price1 = models.DecimalField(max_digits=10, decimal_places=2, default=999)
    price2 = models.DecimalField(max_digits=10, decimal_places=2, default=999)
    price3 = models.DecimalField(max_digits=10, decimal_places=2, default=999)
    price4 = models.DecimalField(max_digits=10, decimal_places=2, default=990)



class Newspaper(models.Model):
    image = models.ImageField(upload_to='newspaper_images/')
    title= models.CharField(max_length=255)  # Changed 'title' to 'name'
    date = models.DateField(default=date.today)  # Stores the created date
    rating = models.DecimalField(max_digits=2, decimal_places=1, default=0.0)  # Example: 4.5 stars
    readers_count = models.PositiveIntegerField(default=0)  # Number of readers
    sub_content = models.TextField(max_length=500)
    price1 = models.DecimalField(max_digits=10, decimal_places=2, default=999)
    price2 = models.DecimalField(max_digits=10, decimal_places=2, default=999)
    price3 = models.DecimalField(max_digits=10, decimal_places=2, default=999)
    price4 = models.DecimalField(max_digits=10, decimal_places=2, default=990)


class Magazine(models.Model):
    image = models.ImageField(upload_to='magazine_images/')
    title  = models.CharField(max_length=255)  # Changed 'title' to 'name'
    date = models.DateField(default=date.today)  # Stores the created date
    rating = models.DecimalField(max_digits=2, decimal_places=1, default=0.0)  # Example: 4.5 stars
    readers_count = models.PositiveIntegerField(default=0)  # Number of readers
    sub_content = models.TextField(max_length=500)
    price1 = models.DecimalField(max_digits=10, decimal_places=2, default=999)
    price2 = models.DecimalField(max_digits=10, decimal_places=2, default=999)
    price3 = models.DecimalField(max_digits=10, decimal_places=2, default=999)
    price4 = models.DecimalField(max_digits=10, decimal_places=2, default=990)


class Business(models.Model):
    image = models.ImageField(upload_to='business_images/')
    title = models.CharField(max_length=255)  # Changed 'title' to 'name'
    date = models.DateField(default=date.today) # Stores the created date
    rating = models.DecimalField(max_digits=2, decimal_places=1, default=0.0)  # Example: 4.5 stars
    readers_count = models.PositiveIntegerField(default=0)  # Number of readers
    sub_content = models.TextField(max_length=500)
    price1 = models.DecimalField(max_digits=10, decimal_places=2, default=999)
    price2 = models.DecimalField(max_digits=10, decimal_places=2, default=999)
    price3 = models.DecimalField(max_digits=10, decimal_places=2, default=999)
    price4 = models.DecimalField(max_digits=10, decimal_places=2, default=990)



class Fashion(models.Model):
    image = models.ImageField(upload_to='fashion_images/')
    title = models.CharField(max_length=255)  # Changed 'title' to 'name'
    date = models.DateField(default=date.today)  # Stores the created date
    rating = models.DecimalField(max_digits=2, decimal_places=1, default=0.0)  # Example: 4.5 stars
    readers_count = models.PositiveIntegerField(default=0)  # Number of readers
    sub_content = models.TextField(max_length=500)
    price1 = models.DecimalField(max_digits=10, decimal_places=2, default=999)
    price2 = models.DecimalField(max_digits=10, decimal_places=2, default=999)
    price3 = models.DecimalField(max_digits=10, decimal_places=2, default=999)
    price4 = models.DecimalField(max_digits=10, decimal_places=2, default=990)



class Technology(models.Model):
    image = models.ImageField(upload_to='technology_images/')
    title = models.CharField(max_length=255)  # Changed 'title' to 'name'
    date = models.DateField(default=date.today)  # Stores the created date
    rating = models.DecimalField(max_digits=2, decimal_places=1, default=0.0)  # Example: 4.5 stars
    readers_count = models.PositiveIntegerField(default=0)  # Number of readers
    sub_content = models.TextField(max_length=500)
    price1 = models.DecimalField(max_digits=10, decimal_places=2, default=999)
    price2 = models.DecimalField(max_digits=10, decimal_places=2, default=999)
    price3 = models.DecimalField(max_digits=10, decimal_places=2, default=999)
    price4 = models.DecimalField(max_digits=10, decimal_places=2, default=990)



class Comic(models.Model):
    image = models.ImageField(upload_to='comic_images/')
    title = models.CharField(max_length=255)  # Changed 'title' to 'name'
    date = models.DateField(default=date.today)  # Stores the created date
    rating = models.DecimalField(max_digits=2, decimal_places=1, default=0.0)  # Example: 4.5 stars
    readers_count = models.PositiveIntegerField(default=0)  # Number of readers
    sub_content = models.TextField(max_length=500)
    price1 = models.DecimalField(max_digits=10, decimal_places=2, default=999)
    price2 = models.DecimalField(max_digits=10, decimal_places=2, default=999)
    price3 = models.DecimalField(max_digits=10, decimal_places=2, default=999)
    price4 = models.DecimalField(max_digits=10, decimal_places=2, default=990)



class Autocar(models.Model):
    image = models.ImageField(upload_to='autocar_images/')
    title = models.CharField(max_length=255)  # Changed 'title' to 'name'
    date = models.DateField(default=date.today) # Stores the created date
    rating = models.DecimalField(max_digits=2, decimal_places=1, default=0.0)  # Example: 4.5 stars
    readers_count = models.PositiveIntegerField(default=0)  # Number of readers
    sub_content = models.TextField(max_length=500)
    price1 = models.DecimalField(max_digits=10, decimal_places=2, default=999)
    price2 = models.DecimalField(max_digits=10, decimal_places=2, default=999)
    price3 = models.DecimalField(max_digits=10, decimal_places=2, default=999)
    price4 = models.DecimalField(max_digits=10, decimal_places=2, default=990)


    
class Sport(models.Model):
    image = models.ImageField(upload_to='sport_images/')
    title = models.CharField(max_length=255)  # Changed 'title' to 'name'
    date = models.DateField(default=date.today)  # Stores the created date
    rating = models.DecimalField(max_digits=2, decimal_places=1, default=0.0)  # Example: 4.5 stars
    readers_count = models.PositiveIntegerField(default=0)  # Number of readers
    sub_content = models.TextField(max_length=500)
    price1 = models.DecimalField(max_digits=10, decimal_places=2, default=999)
    price2 = models.DecimalField(max_digits=10, decimal_places=2, default=999)
    price3 = models.DecimalField(max_digits=10, decimal_places=2, default=999)
    price4 = models.DecimalField(max_digits=10, decimal_places=2, default=990)



class Holiday(models.Model):
    image = models.ImageField(upload_to='holiday_images/')
    title = models.CharField(max_length=255)  # Changed 'title' to 'name'
    date = models.DateField(default=date.today)  # Stores the created date
    rating = models.DecimalField(max_digits=2, decimal_places=1, default=0.0)  # Example: 4.5 stars
    readers_count = models.PositiveIntegerField(default=0)  # Number of readers
    sub_content = models.TextField(max_length=500)
    price1 = models.DecimalField(max_digits=10, decimal_places=2, default=999)
    price2 = models.DecimalField(max_digits=10, decimal_places=2, default=999)
    price3 = models.DecimalField(max_digits=10, decimal_places=2, default=999)
    price4 = models.DecimalField(max_digits=10, decimal_places=2, default=990)



class Health(models.Model):
    image = models.ImageField(upload_to='health_images/')
    title = models.CharField(max_length=255)  # Changed 'title' to 'name'
    date = models.DateField(default=date.today)  # Stores the created date
    rating = models.DecimalField(max_digits=2, decimal_places=1, default=0.0)  # Example: 4.5 stars
    readers_count = models.PositiveIntegerField(default=0)  # Number of readers
    sub_content = models.TextField(max_length=500)
    price1 = models.DecimalField(max_digits=10, decimal_places=2, default=999)
    price2 = models.DecimalField(max_digits=10, decimal_places=2, default=999)
    price3 = models.DecimalField(max_digits=10, decimal_places=2, default=999)
    price4 = models.DecimalField(max_digits=10, decimal_places=2, default=990)



class Competitive_Exam(models.Model):
    image = models.ImageField(upload_to='competitive_exam_images/')
    title  = models.CharField(max_length=255)  # Changed 'title' to 'name'
    date = models.DateField(default=date.today)  # Stores the created date
    rating = models.DecimalField(max_digits=2, decimal_places=1, default=0.0)  # Example: 4.5 stars
    readers_count = models.PositiveIntegerField(default=0)  # Number of readers
    sub_content = models.TextField(max_length=500)
    price1 = models.DecimalField(max_digits=10, decimal_places=2, default=999)
    price2 = models.DecimalField(max_digits=10, decimal_places=2, default=999)
    price3 = models.DecimalField(max_digits=10, decimal_places=2, default=999)
    price4 = models.DecimalField(max_digits=10, decimal_places=2, default=990)


class Fitness(models.Model):
    image = models.ImageField(upload_to='fitness_images/')
    title = models.CharField(max_length=255)  # Changed 'title' to 'name'
    date = models.DateField(default=date.today)  # Stores the created date
    rating = models.DecimalField(max_digits=2, decimal_places=1, default=0.0)  # Example: 4.5 stars
    readers_count = models.PositiveIntegerField(default=0)  # Number of readers
    sub_content = models.TextField(max_length=500)
    price1 = models.DecimalField(max_digits=10, decimal_places=2, default=999)
    price2 = models.DecimalField(max_digits=10, decimal_places=2, default=999)
    price3 = models.DecimalField(max_digits=10, decimal_places=2, default=999)
    price4 = models.DecimalField(max_digits=10, decimal_places=2, default=990)


