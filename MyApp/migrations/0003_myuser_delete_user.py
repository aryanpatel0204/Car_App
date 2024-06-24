# Generated by Django 5.0.4 on 2024-05-28 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0002_alter_user_address'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=100)),
                ('lname', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('cpassword', models.CharField(max_length=100)),
                ('mobile', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('address', models.TextField()),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('zipCode', models.CharField(max_length=100)),
                ('genderType', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
