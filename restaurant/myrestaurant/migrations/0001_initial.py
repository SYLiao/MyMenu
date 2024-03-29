# Generated by Django 2.2.7 on 2019-11-14 19:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=50, verbose_name='Restaurant Name')),
                ('address', models.TextField(blank=True, default='', max_length=200, verbose_name='Address')),
                ('telephone', models.TextField(blank=True, default='', max_length=20, verbose_name='Telephone number')),
                ('url', models.URLField(blank=True, default='', verbose_name='Offical Website')),
                ('date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Create Time')),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='RestaurantReview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Rating', models.SmallIntegerField(choices=[(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four'), (5, 'five')], default=5, verbose_name='Rating (stars)')),
                ('date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Create time')),
                ('comment', models.TextField(blank=True, max_length=200, null=True, verbose_name='Comment')),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='myrestaurant.Restaurant')),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(verbose_name='Dish name')),
                ('description', models.TextField(blank=True, default='', verbose_name='Dish description')),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='Dish price')),
                ('date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Create time')),
                ('restaurant', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='myrestaurant.Restaurant')),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
