# Generated by Django 4.1.3 on 2022-11-16 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Nivel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('dni', models.CharField(max_length=10)),
                ('release_date', models.DateField()),
                ('category', models.CharField(choices=[('junior', 'Junior'), ('semijunior', 'Semijunior'), ('senior', 'Senior')], max_length=10)),
                ('category_perfil', models.CharField(choices=[('frontend', 'Frontend'), ('backend', 'Backend')], max_length=10)),
            ],
        ),
    ]