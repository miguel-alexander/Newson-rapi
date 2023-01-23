# Generated by Django 3.2 on 2022-08-20 20:26

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0037_postsequence_employee_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prospect',
            name='engagement',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('Liked Posts', 'Liked Posts'), ('Commented Posts', 'Commented Posts'), ('Shared Posts', 'Shared Posts'), ('Job Applicant', 'Job Applicant')], max_length=54, null=True),
        ),
    ]