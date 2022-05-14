# Generated by Django 2.2.16 on 2022-05-14 06:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0003_auto_20220512_2357'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='review',
        ),
        migrations.RemoveField(
            model_name='genre_title',
            name='genre_id',
        ),
        migrations.RemoveField(
            model_name='genre_title',
            name='title_id',
        ),
        migrations.AddField(
            model_name='genre_title',
            name='genre',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='reviews.Genre'),
        ),
        migrations.AddField(
            model_name='genre_title',
            name='title',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='reviews.Title'),
        ),
        migrations.AddField(
            model_name='title',
            name='rating',
            field=models.IntegerField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='pub_date',
            field=models.DateTimeField(verbose_name='Дата публикации'),
        ),
        migrations.AlterField(
            model_name='title',
            name='genre',
            field=models.ManyToManyField(default=None, related_name='titles', through='reviews.Genre_title', to='reviews.Genre'),
        ),
    ]