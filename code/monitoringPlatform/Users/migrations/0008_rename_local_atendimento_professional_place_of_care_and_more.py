# Generated by Django 4.0.3 on 2022-12-26 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0007_user_phone_number_alter_user_email'),
    ]

    operations = [
        migrations.RenameField(
            model_name='professional',
            old_name='local_atendimento',
            new_name='place_of_care',
        ),
        migrations.RemoveField(
            model_name='professional',
            name='codigo_verificador',
        ),
        migrations.AddField(
            model_name='professional',
            name='professional_type',
            field=models.CharField(choices=[('N', 'NUTRITIONIST'), ('PE', 'PHYSICAL EDUCATOR')], default='N', max_length=2),
        ),
        migrations.AddField(
            model_name='professional',
            name='validator_code',
            field=models.CharField(default=1, max_length=250),
            preserve_default=False,
        ),
    ]
