# Generated by Django 5.0.6 on 2024-06-20 07:13
# Generated by Django 5.0.6 on 2024-06-20 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('talent_management_system', '0003_alter_employee_table_alter_goal_table_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='password',
            field=models.CharField(default='password', max_length=15),
        ),
    ]
