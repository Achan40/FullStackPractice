from django.db import models

# Create your models here.
# Models are classes that are a derived class froim Django models class
class Topic(models.Model):
    top_name = models.CharField(max_length=264, unique=True)

    # String representation of the model
    def __str__(self):
        return self.top_name

class Webpage(models.Model):
    topic = models.ForeignKey(Topic, on_delete = models.CASCADE)
    name = models.CharField(max_length=264,unique=True)
    url = models.URLField(unique=True)

    def __str__(self):
        return self.name
    
class AccessRecord(models.Model):
    name = models.ForeignKey(Webpage, on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return str(self.date)

# To make sql data base: manage.py migrate
# manage.py makemigration nameofapp
# manage.py migrate

# See the data using manage.py shell