# Generated by Django 5.0.7 on 2024-08-02 19:00

import django.db.models.deletion
import mptt.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField(blank=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='category_images/')),
                ('lft', models.PositiveIntegerField(default=0)),
                ('rght', models.PositiveIntegerField(default=0)),
                ('tree_id', models.PositiveIntegerField(default=0)),
                ('level', models.PositiveIntegerField(default=0)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='categories.category')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CategorySimilarity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_a', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='similar_to', to='categories.category')),
                ('category_b', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='similar_from', to='categories.category')),
            ],
            options={
                'unique_together': {('category_a', 'category_b')},
            },
        ),
    ]
