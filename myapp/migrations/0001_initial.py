# Generated by Django 5.0 on 2024-01-16 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Current_Affairs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=500)),
                ('answer', models.CharField(max_length=500)),
                ('opt_A', models.CharField(max_length=500)),
                ('opt_B', models.CharField(max_length=500)),
                ('opt_C', models.CharField(max_length=500)),
                ('opt_D', models.CharField(max_length=500)),
                ('ans_description', models.CharField(max_length=1000)),
                ('category', models.CharField(max_length=300)),
                ('question_topic', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='English_and_literature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=500)),
                ('answer', models.CharField(max_length=500)),
                ('opt_A', models.CharField(max_length=500)),
                ('opt_B', models.CharField(max_length=500)),
                ('opt_C', models.CharField(max_length=500)),
                ('opt_D', models.CharField(max_length=500)),
                ('ans_description', models.CharField(max_length=1000)),
                ('category', models.CharField(max_length=300)),
                ('question_topic', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Gujarati_and_literature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=500)),
                ('answer', models.CharField(max_length=500)),
                ('opt_A', models.CharField(max_length=500)),
                ('opt_B', models.CharField(max_length=500)),
                ('opt_C', models.CharField(max_length=500)),
                ('opt_D', models.CharField(max_length=500)),
                ('ans_description', models.CharField(max_length=1000)),
                ('category', models.CharField(max_length=300)),
                ('question_topic', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Maths_and_Reasoning',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=500)),
                ('answer', models.CharField(max_length=500)),
                ('opt_A', models.CharField(max_length=500)),
                ('opt_B', models.CharField(max_length=500)),
                ('opt_C', models.CharField(max_length=500)),
                ('opt_D', models.CharField(max_length=500)),
                ('ans_description', models.CharField(max_length=1000)),
                ('category', models.CharField(max_length=300)),
                ('question_topic', models.CharField(max_length=300)),
            ],
        ),
    ]