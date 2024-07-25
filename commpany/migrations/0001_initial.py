# Generated by Django 5.0.7 on 2024-07-25 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_title', models.CharField(max_length=60)),
                ('post_content', models.TextField()),
                ('published_date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
