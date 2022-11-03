# Generated by Django 4.1.1 on 2022-09-25 13:21

from django.db import migrations, models
import django.db.models.deletion
import stdimage.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateField(auto_now_add=True, verbose_name='Criado em')),
                ('modified', models.DateField(auto_now=True, verbose_name='Modificado em')),
                ('active', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('role_name', models.CharField(max_length=100, verbose_name='role')),
            ],
            options={
                'verbose_name': 'Role',
                'verbose_name_plural': 'Roles',
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateField(auto_now_add=True, verbose_name='Criado em')),
                ('modified', models.DateField(auto_now=True, verbose_name='Modificado em')),
                ('active', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('title', models.CharField(max_length=100, verbose_name='Service')),
                ('description', models.TextField(max_length=250, verbose_name='Description')),
                ('icon', models.CharField(choices=[('lni-cog', 'cog'), ('lni-stats-up', 'graph'), ('lni-users', 'users'), ('lni-layers', 'design'), ('lni-mobile', 'mobile'), ('lni-rocket', 'rocket')], max_length=50, verbose_name='Icon')),
            ],
            options={
                'verbose_name': 'Service',
                'verbose_name_plural': 'Services',
            },
        ),
        migrations.CreateModel(
            name='TeamMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateField(auto_now_add=True, verbose_name='Criado em')),
                ('modified', models.DateField(auto_now=True, verbose_name='Modificado em')),
                ('active', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('bio', models.CharField(max_length=250, verbose_name='Bio')),
                ('picture', stdimage.models.StdImageField(force_min_size=False, upload_to='team_pictures', variations={'thumb': {'crop': True, 'height': 480, 'width': 480}}, verbose_name='Image')),
                ('facebook', models.CharField(default='#', max_length=100, verbose_name='Facebook')),
                ('twitter', models.CharField(default='#', max_length=100, verbose_name='Twitter')),
                ('instagram', models.CharField(default='#', max_length=100, verbose_name='Instagram')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.role', verbose_name='Role')),
            ],
            options={
                'verbose_name': 'Team member',
                'verbose_name_plural': 'Team members',
            },
        ),
    ]