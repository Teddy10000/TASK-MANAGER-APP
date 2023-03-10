# Generated by Django 4.1.5 on 2023-01-27 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0002_remove_notes_attachments_remove_notes_completed_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='notes',
            name='attachments',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='notes',
            name='completed',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='notes',
            name='description',
            field=models.TextField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='notes',
            name='details',
            field=models.CharField(default=None, max_length=255),
        ),
        migrations.AddField(
            model_name='notes',
            name='time_to_complete',
            field=models.DateTimeField(blank=True, default=None),
        ),
        migrations.AddField(
            model_name='notes',
            name='title',
            field=models.CharField(default=None, max_length=30, null=True),
        ),
        migrations.DeleteModel(
            name='NoteItems',
        ),
    ]
