# Generated by Django 2.0.3 on 2018-05-03 07:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('boats', '0008_crew_recruited'),
    ]

    operations = [
        migrations.CreateModel(
            name='Elling',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=20)),
                ('phone_number', models.IntegerField()),
                ('elling_photo', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='RepairContract',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_begin', models.DateField()),
                ('date_end', models.DateField()),
                ('repair_price', models.IntegerField(default=0)),
                ('repair_cause', models.CharField(default='', max_length=30)),
            ],
        ),
        migrations.AlterField(
            model_name='boat',
            name='bay_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='boats.Bay'),
        ),
        migrations.AddField(
            model_name='repaircontract',
            name='boat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='boats.Boat'),
        ),
        migrations.AddField(
            model_name='repaircontract',
            name='elling',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='boats.Elling'),
        ),
    ]