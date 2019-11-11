# Dino API

## API developed using Django and Django Rest Framework

![Gif](/images/Recording.gif)

### Development Branch

To implement authorization and authentication coming from the backend to this frontend. Sign up and log in users to add new Dinosaurs.

### Endpoints

You can make requests to the following endpoint: http://127.0.0.1:8000/api/dinosaur/

The admin has currently a secret password.

### JSON Object

-It is also possible to make a request to an endpoint based on ID: 

http://127.0.0.1:8000/api/dinosaur/1/

-With the following result for a GET request:

 ```{
        "id": 1,
        "name": "Acanthopholis",
        "description": "Herbivore, Quadrupedal",
        "height": "1.80",
        "weight": 380,
        "image": "https://vignette.wikia.nocookie.net/ppba/images/e/ea/Acanthopholis222_29db.jpg/revision/latest?cb=20181123195027",
        "region": "Europe",
        "geological_era": "CRETACEOUS"
    }```

### Hackathon

To track all the progress until the end of the Hackathon, check the branch 'Hackathon'.

Developed during 2.5 days for a Hackathon at Codaisseur in Amsterdam in November, 2019. 