# Generated by Django 4.2.6 on 2023-10-12 11:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LexiconSentimentAnalysis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_sentiment_score', models.FloatField(null=True)),
                ('normalized_sentiment_score', models.FloatField(null=True)),
                ('sentiment_label', models.CharField(max_length=15, null=True)),
                ('result', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='lexicon_sentiment_analysis', to='account.result')),
            ],
        ),
    ]
