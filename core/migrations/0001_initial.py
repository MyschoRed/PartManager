# Generated by Django 4.2.1 on 2023-06-06 18:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Customer",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "boost_id",
                    models.CharField(
                        blank=True, editable=False, max_length=5, null=True, unique=True
                    ),
                ),
                ("name", models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name="Part",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "part_id",
                    models.CharField(
                        blank=True, editable=False, max_length=6, null=True, unique=True
                    ),
                ),
                ("description", models.CharField(max_length=512)),
                ("customer_part", models.CharField(max_length=128)),
                ("revision", models.CharField(blank=True, max_length=5, null=True)),
                (
                    "customer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="part_customer",
                        to="core.customer",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Order",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "order_id",
                    models.CharField(
                        blank=True, editable=False, max_length=4, null=True, unique=True
                    ),
                ),
                ("pcs", models.IntegerField(default=1)),
                (
                    "customer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="order_customer",
                        to="core.customer",
                    ),
                ),
                (
                    "part",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="order_part",
                        to="core.part",
                    ),
                ),
            ],
        ),
    ]
