# Generated by Django 2.0.7 on 2019-10-20 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0002_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeleteTweet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status_id', models.TextField()),
            ],
        ),
        migrations.RenameModel(
            old_name='Tweet',
            new_name='CreateTweet',
        ),
    ]