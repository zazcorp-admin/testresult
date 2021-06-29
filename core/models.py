from django.db import models
from ckeditor.fields import RichTextField


class TestResult(models.Model):
    title = models.CharField(max_length=1000)
    fat = models.CharField(max_length=1000,default='(Non-Adulterated)')
    snf = models.CharField(max_length=1000,default='(Non-Adulterated)')
    urea = models.CharField(max_length=1000,default='(Non-Adulterated)')
    starch = models.CharField(max_length=1000,default='(Non-Adulterated)')
    detergent = models.CharField(max_length=1000,default='(Non-Adulterated)')
    antibiotic = models.CharField(max_length=1000,default='(Non-Adulterated)')
    acidity = models.CharField(max_length=1000,default='(Non-Adulterated)')
    caustic_soda = models.CharField(max_length=1000,default='(Non-Adulterated)')
    desc = models.TextField()
    test_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return str(self.title) + '-->' + str(self.test_date)



class TermsAndCondition(models.Model):
    terms = RichTextField()