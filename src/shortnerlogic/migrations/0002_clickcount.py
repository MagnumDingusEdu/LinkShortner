# Generated by Django 3.0.6 on 2020-05-28 02:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shortnerlogic', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClickCount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clickcount', models.PositiveIntegerField(default=0)),
                ('link', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='shortnerlogic.Link')),
            ],
        ),
    ]
