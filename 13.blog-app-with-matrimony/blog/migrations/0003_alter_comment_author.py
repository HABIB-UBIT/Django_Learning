# Generated by Django 4.2.4 on 2023-09-17 21:49

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0002_alter_comment_author"),
    ]

    operations = [
        migrations.AlterField(
            model_name="comment",
            name="author",
            field=models.CharField(max_length=200),
        ),
    ]