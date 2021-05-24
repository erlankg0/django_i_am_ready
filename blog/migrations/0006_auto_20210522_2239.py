# Generated by Django 3.2.3 on 2021-05-22 19:39

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_person'),
    ]

    operations = [
        migrations.CreateModel(
            name='OpinionPoll',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterModelManagers(
            name='person',
            managers=[
                ('people', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Response',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('poll', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.opinionpoll')),
            ],
        ),
    ]