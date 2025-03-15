from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Current_Affairs)
class Current_AffairsAdmin(admin.ModelAdmin):
    list_display=['question','answer','opt_A','opt_B','opt_C','opt_D','ans_description','category','question_topic']

@admin.register(Maths_and_Reasoning)
class Current_AffairsAdmin(admin.ModelAdmin):
    list_display=['question','answer','opt_A','opt_B','opt_C','opt_D','ans_description','category','question_topic']

@admin.register(English_and_literature)
class Current_AffairsAdmin(admin.ModelAdmin):
    list_display=['question','answer','opt_A','opt_B','opt_C','opt_D','ans_description','category','question_topic']

@admin.register(Gujarati_and_literature)
class Current_AffairsAdmin(admin.ModelAdmin):
    list_display=['question','answer','opt_A','opt_B','opt_C','opt_D','ans_description','category','question_topic']


@admin.register(history_questions)
class history_questionsAdmin(admin.ModelAdmin):
    list_display=['question','answer','opt_A','opt_B','opt_C','opt_D','ans_description','category','question_topic']

@admin.register(geograpphy_questions)
class geograpphy_questionsAdmin(admin.ModelAdmin):
    list_display=['question','answer','opt_A','opt_B','opt_C','opt_D','ans_description','category','question_topic']

@admin.register(Computer_Operator)
class Computer_questionsAdmin(admin.ModelAdmin):
    list_display=['question','answer','opt_A','opt_B','opt_C','opt_D','ans_description','category','question_topic']


@admin.register(General_knowledge)
class General_KnowledgeAdmin(admin.ModelAdmin):
    list_display=['question','answer','opt_A','opt_B','opt_C','opt_D','ans_description','category','question_topic']

@admin.register(Current_Affairs2)
class Current_Affairs2Admin(admin.ModelAdmin):
    list_display=['question','answer','opt_A','opt_B','opt_C','opt_D','ans_description','category','question_topic']


@admin.register(Question_Paper)
class Question_PaperAdmin(admin.ModelAdmin):
    list_display=['question','answer','opt_A','opt_B','opt_C','opt_D','ans_description','category','question_topic']

