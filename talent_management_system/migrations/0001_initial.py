
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('employee_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(default='<PASSWORD>', max_length=15)),
                ('phone_number', models.CharField(max_length=15)),
                ('position', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'staff',
            },
        ),
        migrations.CreateModel(
            name='Training',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('location', models.CharField(max_length=255)),
                ('manager_email', models.EmailField(default='no email', max_length=254)),
            ],
            options={
                'db_table': 'trainings',
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('staff_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='talent_management_system.staff')),
            ],
            options={
                'db_table': 'employees',
            },
            bases=('talent_management_system.staff',),
        ),
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('staff_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='talent_management_system.staff')),
                ('department_managed', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'managers',
            },
            bases=('talent_management_system.staff',),
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('proficiency', models.CharField(choices=[('B', 'BEGINNER'), ('I', 'INTERMEDIATE'), ('A', 'ADVANCED')], default='B', max_length=15)),
                ('employee_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='talent_management_system.employee')),
            ],
            options={
                'db_table': 'skills',
            },
        ),
        migrations.CreateModel(
            name='Promotion',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('old_position', models.CharField(max_length=255)),
                ('new_position', models.CharField(max_length=255)),
                ('promotion_date', models.DateField()),
                ('employee_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='talent_management_system.employee')),
            ],
            options={
                'db_table': 'promotions',
            },
        ),
        migrations.CreateModel(
            name='Goal',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=255)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('status', models.CharField(choices=[('PEN', 'PENDING'), ('IN_PRO', 'IN PROGRESS'), ('COMP', 'COMPLETED')], default='PEN', max_length=15)),
                ('employee_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='talent_management_system.employee')),
            ],
            options={
                'db_table': 'goals',
            },
        ),
        migrations.CreateModel(
            name='PerformanceReview',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('review_date', models.DateField()),
                ('comment', models.TextField()),
                ('employee_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='talent_management_system.employee')),
                ('reviewer_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='talent_management_system.manager')),
            ],
            options={
                'db_table': 'performanceReviews',
            },
        ),
        migrations.AddField(
            model_name='employee',
            name='manager_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='talent_management_system.manager'),
        ),
    ]
