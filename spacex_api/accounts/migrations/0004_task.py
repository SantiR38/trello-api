# Generated by Django 3.0.11 on 2021-03-30 11:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0003_create_default_categories'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date time on which the object was created.', verbose_name='created at')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Date time on which the object was last modified.', verbose_name='modified at')),
                ('title', models.CharField(max_length=45)),
                ('description', models.CharField(blank=True, max_length=255)),
                ('trello_list', models.CharField(max_length=140, null=True)),
                ('category_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.Category')),
                ('status_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.Status')),
                ('user_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created', '-modified'],
                'get_latest_by': 'created',
                'abstract': False,
            },
        ),
    ]
