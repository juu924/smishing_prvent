# Generated by Django 3.2.7 on 2021-10-12 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smishing', '0004_alter_member_member_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='member_id',
            field=models.AutoField(db_column='UserID', primary_key=True, serialize=False),
        ),
    ]
