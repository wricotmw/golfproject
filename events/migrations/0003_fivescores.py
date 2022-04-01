# Generated by Django 3.2.9 on 2022-02-16 14:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_rename_golfer_scores_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='FiveScores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score1', models.IntegerField()),
                ('score2', models.IntegerField()),
                ('score3', models.IntegerField()),
                ('score4', models.IntegerField()),
                ('score5', models.IntegerField()),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.golfer')),
            ],
        ),
    ]