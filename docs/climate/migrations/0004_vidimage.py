# Generated by Django 3.1.2 on 2022-04-27 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('climate', '0003_auto_20220427_0039'),
    ]

    operations = [
        migrations.CreateModel(
            name='vidimage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='vidimage')),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
