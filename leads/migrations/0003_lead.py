# Generated by Django 4.1.1 on 2022-09-08 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0002_agent_created_at_agent_updated_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lead',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name of the lead', max_length=200, verbose_name='Name')),
                ('phone', models.CharField(help_text='Number of phone of the agent', max_length=11, unique=True, verbose_name='Phone')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
            ],
            options={
                'verbose_name': 'Lead',
                'verbose_name_plural': 'Leads',
            },
        ),
    ]
