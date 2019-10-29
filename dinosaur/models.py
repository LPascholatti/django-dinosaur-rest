from django.db import models


class Dinosaur(models.Dinosaur):
    TRIASIC = 'TRIASIC'
    JURASSIC = 'JURASSIC'
    CRETACEOUS = 'CRETACEOUS'
    GEOLOGICAL_ERAS = [
        (TRIASIC, 'Triasic'),
        (JURASSIC, 'Jurassic'),
        (CRETACEOUS, 'Cretaceous')
    ]
    name: models.CharField(max_length=250)
    age: models.IntegerField()
    geological_era: models.CharField(
      max_length=300,
      choices=GEOLOGICAL_ERAS
    )
    image: models.URLField()
    region: models.CharField(max_length=100)
