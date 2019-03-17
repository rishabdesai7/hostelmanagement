# Generated by Django 2.1 on 2019-03-15 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='applications',
            fields=[
                ('app_id', models.AutoField(primary_key=True, serialize=False)),
                ('student_id', models.SmallIntegerField()),
                ('hostel_id', models.SmallIntegerField()),
                ('room_id', models.SmallIntegerField()),
                ('status', models.CharField(default=None, max_length=10)),
            ],
            options={
                'db_table': 'applications',
            },
        ),
        migrations.CreateModel(
            name='complaints',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_id', models.SmallIntegerField()),
                ('sender', models.CharField(max_length=10)),
                ('receiver', models.CharField(max_length=10)),
                ('text', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'complaints',
            },
        ),
        migrations.CreateModel(
            name='hostel',
            fields=[
                ('hostel_id', models.SmallIntegerField(primary_key=True, serialize=False)),
                ('hostel_name', models.CharField(max_length=30)),
                ('totalrooms', models.PositiveIntegerField()),
                ('availablerooms', models.PositiveIntegerField()),
            ],
            options={
                'db_table': 'hostel',
            },
        ),
        migrations.CreateModel(
            name='rooms',
            fields=[
                ('room_id', models.SmallIntegerField(primary_key=True, serialize=False)),
                ('hostel_no', models.SmallIntegerField()),
                ('status', models.CharField(default='free', max_length=10)),
                ('student_id', models.SmallIntegerField(default=None)),
            ],
            options={
                'db_table': 'rooms',
            },
        ),
        migrations.CreateModel(
            name='users',
            fields=[
                ('id', models.SmallIntegerField(primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=20)),
                ('user_type', models.CharField(max_length=10)),
                ('hostel_no', models.IntegerField(null=True)),
                ('room_no', models.IntegerField(null=True)),
                ('phone_no', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'users',
            },
        ),
    ]