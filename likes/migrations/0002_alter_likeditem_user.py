# Generated by Django 4.0 on 2022-01-02 11:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
        ('likes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='likeditem',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.user'),
        ),
    ]