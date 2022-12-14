# Generated by Django 2.2.12 on 2022-11-19 14:29

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_auto_20221119_1521'),
    ]

    operations = [
        migrations.CreateModel(
            name='Costumer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=100)),
                ('namabrg', models.CharField(max_length=100)),
                ('jumlahbrg', models.CharField(max_length=100)),
                ('harga', models.CharField(max_length=50)),
                ('totalbyr', models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='Sosmed',
        ),
        migrations.RemoveField(
            model_name='transaksi',
            name='tanggal',
        ),
        migrations.AddField(
            model_name='transaksi',
            name='jenis_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dashboard.Jenis'),
        ),
        migrations.AddField(
            model_name='transaksi',
            name='nama',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='transaksi',
            name='phone',
            field=models.CharField(max_length=50),
        ),
    ]
