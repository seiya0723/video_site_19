# Generated by Django 3.2.7 on 2021-09-19 04:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tube', '0002_auto_20210919_1251'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='monthlyrank',
            name='category',
        ),
        migrations.RemoveField(
            model_name='monthlyrank',
            name='target',
        ),
        migrations.RemoveField(
            model_name='weeklyrank',
            name='category',
        ),
        migrations.RemoveField(
            model_name='weeklyrank',
            name='target',
        ),
        migrations.DeleteModel(
            name='DailyRank',
        ),
        migrations.DeleteModel(
            name='MonthlyRank',
        ),
        migrations.DeleteModel(
            name='WeeklyRank',
        ),
    ]
