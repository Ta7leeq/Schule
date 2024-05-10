from django.db import models

# Create your models here.




class gaps(models.Model):
  gapWord = models.IntegerField()
  sentence = models.TextField()
  category = models.CharField(max_length=100, default='default_value', null=True)
  image = models.CharField(max_length=100, default='default_value', null=True)
  

  def __str__(self):
        return f"{self.sentence} {self.gapWord}"
        #return {f"{self.sentence}",f"{self.gapWord}"}
        #return str((self.sentence))