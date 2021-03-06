from django.db import models

class Dinosaur(models.Model):
    TRIASSIC = 'TRIASSIC'
    JURASSIC = 'JURASSIC'
    CRETACEOUS = 'CRETACEOUS'
    GEOLOGICAL_ERAS = [
        (TRIASSIC, 'Triasic'),
        (JURASSIC, 'Jurassic'),
        (CRETACEOUS, 'Cretaceous')
    ]
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=600)
    height = models.DecimalField(blank=True, max_digits=5, decimal_places=2)
    weight = models.IntegerField(blank=True)
    image = models.URLField(blank=True)
    region = models.CharField(max_length=100)
    geological_era = models.CharField(
        max_length=300,
        choices=GEOLOGICAL_ERAS,
        blank=True
    )
    owner = models.ForeignKey('auth.User', related_name='dinosaurs', on_delete=models.CASCADE)
