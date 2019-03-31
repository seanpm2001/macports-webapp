# Generated by Django 2.1.7 on 2019-03-30 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BuildHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('builder_name', models.CharField(db_index=True, max_length=50)),
                ('build_id', models.IntegerField()),
                ('status', models.CharField(max_length=50)),
                ('port_name', models.CharField(db_index=True, max_length=50)),
                ('time_start', models.CharField(max_length=50)),
                ('time_elapsed', models.CharField(max_length=50)),
                ('build_url', models.URLField(default='')),
                ('watcher_id', models.IntegerField()),
                ('watcher_url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('name', models.TextField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Port',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('portdir', models.CharField(max_length=100)),
                ('variants', models.TextField(default='')),
                ('description', models.TextField(default='')),
                ('homepage', models.URLField(default='')),
                ('epoch', models.TextField(default='')),
                ('platforms', models.TextField(default='')),
                ('long_description', models.TextField(default='')),
                ('depends_extract', models.TextField(default='')),
                ('version', models.CharField(max_length=100)),
                ('revision', models.TextField(default='')),
                ('maintainers', models.TextField(default='')),
                ('name', models.CharField(db_index=True, max_length=100)),
                ('license', models.CharField(max_length=100)),
                ('depends_lib', models.TextField(default='')),
                ('depends_build', models.TextField(default='')),
                ('installs_libs', models.TextField(default='')),
                ('depends_fetch', models.TextField(default='')),
                ('depends_run', models.TextField(default='')),
                ('conflicts', models.TextField(default='')),
                ('replaced_by', models.TextField(default='')),
                ('depends_test', models.TextField(default='')),
                ('depends_patch', models.TextField(default='')),
                ('subports', models.TextField(default='')),
                ('categories', models.ManyToManyField(db_index=True, related_name='category', to='ports.Category')),
            ],
        ),
    ]
