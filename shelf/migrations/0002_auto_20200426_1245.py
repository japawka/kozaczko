# Generated by Django 3.0.5 on 2020-04-26 10:45

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('shelf', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='BookEdition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isbn', models.CharField(max_length=17)),
                ('date', models.DateField()),
            ],
        ),
        migrations.RemoveField(
            model_name='book',
            name='author',
        ),
        migrations.RemoveField(
            model_name='book',
            name='isbn',
        ),
        migrations.RemoveField(
            model_name='book',
            name='publisher',
        ),
        migrations.AddField(
            model_name='book',
            name='authors',
            field=models.ManyToManyField(to='shelf.Author'),
        ),
        migrations.CreateModel(
            name='BookItem',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('cat_number', models.CharField(max_length=30)),
                ('cover_type', models.CharField(choices=[('soft', 'Soft'), ('hard', 'Hard')], max_length=4)),
                ('edition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shelf.BookEdition')),
            ],
        ),
        migrations.AddField(
            model_name='bookedition',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shelf.Book'),
        ),
        migrations.AddField(
            model_name='bookedition',
            name='publisher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shelf.Publisher'),
        ),
        migrations.AddField(
            model_name='book',
            name='categories',
            field=models.ManyToManyField(to='shelf.BookCategory'),
        ),
    ]
