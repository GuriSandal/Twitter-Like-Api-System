# Generated by Django 3.0.6 on 2020-05-30 17:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Tweet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=128)),
                ('is_public', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('type', models.IntegerField(default=0, editable=False)),
                ('likes_count', models.IntegerField(default=0, editable=False)),
                ('comments_count', models.IntegerField(default=0, editable=False)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tweets', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author', to=settings.AUTH_USER_MODEL)),
                ('tweet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='like', to='social_app.Tweet')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('tweet_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='social_app.Tweet')),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='social_app.Tweet')),
            ],
            bases=('social_app.tweet',),
        ),
    ]
