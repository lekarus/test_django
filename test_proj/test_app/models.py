from django.db import models


class TestTable(models.Model):
    description = models.CharField(max_length=80)
