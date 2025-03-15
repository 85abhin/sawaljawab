from django.db import models
# Create your models here.

class Current_Affairs(models.Model):
    question=models.CharField(max_length=500)
    answer=models.CharField(max_length=500)
    opt_A=models.CharField(max_length=500)
    opt_B=models.CharField(max_length=500)
    opt_C=models.CharField(max_length=500)
    opt_D=models.CharField(max_length=500)
    ans_description=models.TextField(max_length=1000)
    category=models.CharField(max_length=300)
    question_topic=models.CharField(max_length=300)
    

class Maths_and_Reasoning(models.Model):
    question=models.CharField(max_length=500)
    answer=models.CharField(max_length=500)
    opt_A=models.CharField(max_length=500)
    opt_B=models.CharField(max_length=500)
    opt_C=models.CharField(max_length=500)
    opt_D=models.CharField(max_length=500)
    ans_description=models.TextField(max_length=1000)
    category=models.CharField(max_length=300)
    question_topic=models.CharField(max_length=300)
    


class Gujarati_and_literature(models.Model):
    question=models.CharField(max_length=500)
    answer=models.CharField(max_length=500)
    opt_A=models.CharField(max_length=500)
    opt_B=models.CharField(max_length=500)
    opt_C=models.CharField(max_length=500)
    opt_D=models.CharField(max_length=500)
    ans_description=models.TextField(max_length=1000)
    category=models.CharField(max_length=300)
    question_topic=models.CharField(max_length=300)
    

class English_and_literature(models.Model):
    question=models.CharField(max_length=500)
    answer=models.CharField(max_length=500)
    opt_A=models.CharField(max_length=500)
    opt_B=models.CharField(max_length=500)
    opt_C=models.CharField(max_length=500)
    opt_D=models.CharField(max_length=500)
    ans_description=models.TextField(max_length=1000)
    category=models.CharField(max_length=300)
    question_topic=models.CharField(max_length=300)
    
class history_questions(Current_Affairs):
    pass

class geograpphy_questions(Current_Affairs):
    pass

class Computer_Operator(Current_Affairs):
    pass

class General_knowledge(Current_Affairs):
    pass

class Current_Affairs2(Current_Affairs):
    pass

class Question_Paper(Current_Affairs):
    pass