# Generated by Django 5.0.2 on 2024-02-14 16:35

import storages.backends.s3

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("posts", "0003_post_body_post_name"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="image",
            field=models.ImageField(
                blank=True,
                db_index=True,
                storage=storages.backends.s3.S3Storage(),
                upload_to="images/",
                verbose_name="image",
            ),
        ),
        migrations.AddField(
            model_name="post",
            name="likes",
            field=models.PositiveIntegerField(
                blank=True, db_index=True, default=0, verbose_name="like"
            ),
        ),
        migrations.AlterField(
            model_name="post",
            name="body",
            field=models.CharField(
                blank=True,
                db_index=True,
                max_length=140,
                null=True,
                verbose_name="body",
            ),
        ),
        migrations.AlterField(
            model_name="post",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True, verbose_name="Created DateTime"
            ),
        ),
    ]
