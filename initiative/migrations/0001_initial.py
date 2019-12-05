# Generated by Django 2.2.7 on 2019-12-03 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Initiative',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.TextField()),
                ('team', models.TextField()),
                ('team_leader', models.TextField()),
                ('started_at', models.DateTimeField(auto_now=True)),
                ('goal_date', models.DateField()),
                ('timeline', models.TextField()),
                ('retired', models.BooleanField(default=False)),
            ],
        ),
    ]
