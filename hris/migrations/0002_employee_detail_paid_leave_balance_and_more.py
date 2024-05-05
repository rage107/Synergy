# Generated by Django 4.2.6 on 2024-04-03 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hris', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee_detail',
            name='paid_leave_balance',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='employee_detail',
            name='sick_leave_balance',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='employee_detail',
            name='unpaid_leave_balance',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='leave',
            name='leave_type',
            field=models.CharField(choices=[('sick_leave', 'Sick Leave'), ('paid_leave', 'Paid Leave'), ('unpaid_leave', 'Unpaid Leave'), ('maternity', 'Maternity')], default='unpaid_leave', max_length=20),
        ),
    ]
