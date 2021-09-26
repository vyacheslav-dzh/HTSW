from django.db import models


class Routes(models.Model):
    r_name = models.CharField(max_length=255)
    r_stops = models.TextField()
    r_count_stowaways = models.IntegerField()
    r_region = models.IntegerField()

    def __str__(self):
        return f'Маршрут {self.r_name}'


