# Generated by Django 4.0.3 on 2022-03-15 02:41

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Devices',
            fields=[
                ('id_device', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('create_at', models.DateField(auto_now_add=True)),
                ('state', models.BooleanField(default=True)),
            ],
        ),
    ]