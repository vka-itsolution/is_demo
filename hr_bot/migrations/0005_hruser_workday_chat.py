# Generated by Django 3.0.7 on 2021-03-12 08:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hr_bot', '0004_hruser_checkpoint'),
    ]

    operations = [
        migrations.AddField(
            model_name='hruser',
            name='workday_chat',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='hr_bot.HrChat'),
        ),
    ]
