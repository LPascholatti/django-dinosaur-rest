# Dino API

## API developed using Django and Django Rest Framework

Deployed in Heroku: https://agile-wave-15412.herokuapp.com

![Gif](/images/Recording.gif)

### Endpoints

If you are an authenticated user, you can make POST requests to the following endpoint: http://127.0.0.1:8000/api/dinosaur/

Otherwise, only GET requests are allowed.

Alternatively, for authenticated users, you can make CRUD requests to the same 'dinosaur' endpoint using an 'id'. For example: 
```http -a admin:password123 POST http://127.0.0.1:8000/api/dinosaur/22/```

The admin has currently a secret password. Only the admin can create new users at this moment. To access the 'admin' endpoint use: http://127.0.0.1:8000/admin/

The 'user' endpoint can be accessed by the following 'urls':
users/
users/id

#### Login/Logout

To login and logout please use the following endpoints:

http://127.0.0.1:8000/api-auth/login/
http://127.0.0.1:8000/api-auth/logout/

### JSON Object

-It is also possible to make a request to an endpoint based on ID:

http://127.0.0.1:8000/api/dinosaur/1/

-With the following result for a GET request:

```
  {
        "id": 1,
        "name": "Acanthopholis",
        "description": "Herbivore, Quadrupedal",
        "height": "1.80",
        "weight": 380,
        "image": "https://vignette.wikia.nocookie.net/ppba/images/e/ea/Acanthopholis222_29db.jpg/revision/latest?cb=20181123195027",
        "region": "Europe",
        "geological_era": "CRETACEOUS",
        "owner": 1
    }
```

### Hackathon

To track all the progress until the end of the Hackathon, check the branch 'Hackathon'.

Developed during 2.5 days for a Hackathon at Codaisseur in Amsterdam in November, 2019.
