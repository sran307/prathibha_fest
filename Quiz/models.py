from django.db import models

# Create your models here.
class ClassList(models.Model):
    class_level = models.CharField(max_length=50)
    class_abbr = models.CharField(max_length=20)
    class_range = models.CharField(max_length=5)

    class Meta:
        db_table = 'class_list'

    def __str__(self):
        return f"{self.class_level}-{self.class_range}"