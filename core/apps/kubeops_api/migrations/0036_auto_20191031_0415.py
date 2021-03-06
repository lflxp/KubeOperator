# Generated by Django 2.1.2 on 2019-10-31 04:15

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('kubeops_api', '0035_auto_20191030_0703'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cluster',
            options={'ordering': ('date_created',)},
        ),
        migrations.AddField(
            model_name='cluster',
            name='cluster_doamin_suffix',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='cluster',
            name='status',
            field=models.CharField(
                choices=[('RUNNING', 'running'), ('INSTALLING', 'installing'), ('DELETING', 'deleting'),
                         ('READY', 'ready'), ('ERROR', 'error'), ('WARNING', 'warning'), ('UPGRADING', 'upgrading'),
                         ('SCALING', 'scaling'), ('RESTORING', 'restoring'), ('ADDING', 'adding')], default='READY',
                max_length=128),
        ),
        migrations.AlterField(
            model_name='clusterhealthhistory',
            name='date_type',
            field=models.CharField(choices=[('DAY', 'DAY'), ('HOUR', 'HOUR')], default='HOUR', max_length=255),
        ),
    ]
