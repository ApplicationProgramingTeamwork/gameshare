# Generated by Django 5.1.2 on 2024-11-19 21:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0006_alter_boardgame_options_remove_loan_return_by'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='loan',
            unique_together=set(),
        ),
    ]
