# Generated by Django 2.2.3 on 2019-07-16 10:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Channels',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telegram_id', models.CharField(max_length=15, unique=True)),
                ('title', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Groups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telegram_id', models.CharField(max_length=15, unique=True)),
                ('title', models.CharField(max_length=255)),
                ('linked_channel', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='stats.Channels')),
            ],
        ),
        migrations.AlterField(
            model_name='userstatus',
            name='group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='stats.Groups'),
        ),
        migrations.DeleteModel(
            name='GroupsAndChannels',
        ),
        migrations.AddField(
            model_name='groups',
            name='users',
            field=models.ManyToManyField(null=True, through='stats.UserStatus', to='stats.User'),
        ),
        migrations.AddField(
            model_name='channels',
            name='users',
            field=models.ManyToManyField(null=True, through='stats.UserStatus', to='stats.User'),
        ),
        migrations.AddField(
            model_name='userstatus',
            name='channel',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='stats.Channels'),
        ),
    ]