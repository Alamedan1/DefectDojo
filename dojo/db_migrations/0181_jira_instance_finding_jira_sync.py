# Generated by Django 4.1.7 on 2023-03-02 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dojo', '0180_announcement_userannouncement'),
    ]

    operations = [
        migrations.AddField(
            model_name='jira_instance',
            name='finding_jira_sync',
            field=models.BooleanField(default=False, help_text='If enabled, this will sync changes to a Finding automatically to JIRA', verbose_name='Automatically sync Findings with JIRA?'),
        ),
    ]
