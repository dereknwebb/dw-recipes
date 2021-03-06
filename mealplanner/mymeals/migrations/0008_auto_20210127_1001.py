# Generated by Django 3.1.4 on 2021-01-27 10:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mymeals', '0007_auto_20210126_0539'),
    ]

    operations = [
        migrations.AddField(
            model_name='grocerylist',
            name='recipe_ingredients',
            field=models.ManyToManyField(blank=True, to='mymeals.RecipeIngredient'),
        ),
        migrations.AlterField(
            model_name='grocerylist',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='my_grocery_lists', to=settings.AUTH_USER_MODEL),
        ),
    ]
