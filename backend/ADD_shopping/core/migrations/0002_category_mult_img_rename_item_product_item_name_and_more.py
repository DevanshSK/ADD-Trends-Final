# Generated by Django 4.1 on 2022-10-19 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
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
                ("category1", models.CharField(max_length=100, null=True)),
                ("category2", models.CharField(max_length=100, null=True)),
                ("category3", models.CharField(max_length=100, null=True)),
                ("category4", models.CharField(max_length=100, null=True)),
                ("category5", models.CharField(max_length=100, null=True)),
                ("category6", models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="mult_img",
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
                ("brand", models.CharField(max_length=50, null=True)),
                ("image1", models.ImageField(blank=True, upload_to="items/")),
                ("image2", models.ImageField(blank=True, upload_to="items/")),
                ("image3", models.ImageField(blank=True, upload_to="items/")),
                ("image4", models.ImageField(blank=True, upload_to="items/")),
                ("image5", models.ImageField(blank=True, upload_to="items/")),
            ],
        ),
        migrations.RenameField(
            model_name="product", old_name="item", new_name="item_name",
        ),
        migrations.RemoveField(model_name="product", name="discount",),
        migrations.RemoveField(model_name="product", name="mrp",),
        migrations.RemoveField(model_name="product", name="slug",),
        migrations.RemoveField(model_name="product", name="style_note",),
        migrations.AddField(
            model_name="product",
            name="category",
            field=models.CharField(
                choices=[
                    ("Winter Wear", "Winter Wear"),
                    ("Summer Wear", "Summer Wear"),
                    ("Top wear", "Top wear"),
                    ("Bottom Wear", "Bottom Wear"),
                    ("Foot wear", "Foot wear"),
                    ("Null", "Null"),
                ],
                max_length=200,
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="product",
            name="discounted_percent",
            field=models.DecimalField(
                decimal_places=2, max_digits=7, null=True, verbose_name="discount  %"
            ),
        ),
        migrations.AddField(
            model_name="product",
            name="original_mrp",
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name="product", name="rating", field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name="product", name="stock", field=models.IntegerField(null=True),
        ),
    ]
