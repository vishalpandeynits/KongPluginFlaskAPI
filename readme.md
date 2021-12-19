# Kong Plugin For QoS (Quality Of Service) - Github Externship

## Project Goal
To integrate a simple Kong Plugin with Flask API. 

## Technologies used
1. Flask
2. Kong
3. PostgreSQL(Database)

## How to run this project ?

* Clone the repository using

```bash
    https://github.com/vishalpandeyvip/KongPluginFlaskAPI.git
```

* Install requirements using pip. Please make sure that you are in project's root directory.

```bash
pip3 install -r requirements.txt
```

* Create a postgresql database, an user and set password using following command.
```
CREATE USER kong; 
CREATE DATABASE kong OWNER kong;
ALTER USER kong WITH PASSWORD 'password';
```

* change the credentials in kong.config accordingly.

* Runserver of flask API
```bash
python3 app.py
```
* Run Kong
```
sudo kong start -c path/to/kong.config
```

* Stop kong
```
sudo kong stop
```

## Routes
[GET] `/`:
Sample Response
```
{
    "data": "Welcome to dictionary"
}
```
[GET] `/<word>`: It returns a json response which has meaning and details about the word provided.
```
[
    {
        "meanings": [
            {
                "definitions": [
                    {
                        "antonyms": [],
                        "definition": "used as a greeting or to begin a phone conversation.",
                        "example": "hello there, Katie!",
                        "synonyms": []
                    }
                ],
                "partOfSpeech": "exclamation"
            },
        ]
    }
}
```

## Step by step procedure image

1. Added Flask API services to the kong API gateway, by sending service name and url to kong system’s URL which is running at localhost:8001
![Alt text](https://github.com/vishalpandeyvip/KongPluginFlaskAPI/blob/main/screenshots/1.png)

2. Now added the route which will redirect users to our Flask service.
![Alt text](https://github.com/vishalpandeyvip/KongPluginFlaskAPI/blob/main/screenshots/2.png)

3. Authentication key plugin api-key added, It must be supplied in the header of the request by the users for a successful redirection.
![Alt text](https://github.com/vishalpandeyvip/KongPluginFlaskAPI/blob/main/screenshots/3.png)

4. In case the authentication key is not supplied in the request and if these APIs are called then they will raise errors.
![Alt text](https://github.com/vishalpandeyvip/KongPluginFlaskAPI/blob/main/screenshots/5.png)

5. If wrong authentication key is provided , then this error will be raised.
![Alt text](https://github.com/vishalpandeyvip/KongPluginFlaskAPI/blob/main/screenshots/6.png)

6. Created a consumer who will use our Flask API through the kong API gateway. 
![Alt text](https://github.com/vishalpandeyvip/KongPluginFlaskAPI/blob/main/screenshots/8.png)

7. The user has been created and its api key is retrieved and passed into the header. It will call our flask API through the endpoints exposed by Kong. And now we can use our APIs successfully.
![Alt text](https://github.com/vishalpandeyvip/KongPluginFlaskAPI/blob/main/screenshots/9.png)
![Alt text](https://github.com/vishalpandeyvip/KongPluginFlaskAPI/blob/main/screenshots/10.png)

## License
[MIT](https://choosealicense.com/licenses/mit/)