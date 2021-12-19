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

1. Adding word-meaning service which is a flask app deployed at posrt 5000.
![Alt text](https://github.com/vishalpandeyvip/KongPluginFlaskAPI/blob/main/screenshots/1.png)

2. Adding routes to the service created previously ar path `meaning`
![Alt text](https://github.com/vishalpandeyvip/KongPluginFlaskAPI/blob/main/screenshots/2.png)

3. Adding Authentication key plugin `api-key` which must be suppplied in header of the request by the users.
![Alt text](https://github.com/vishalpandeyvip/KongPluginFlaskAPI/blob/main/screenshots/3.png)

4. If Authentication key is not suppplied, these types of error will be raised.
![Alt text](https://github.com/vishalpandeyvip/KongPluginFlaskAPI/blob/main/screenshots/4.png)
![Alt text](https://github.com/vishalpandeyvip/KongPluginFlaskAPI/blob/main/screenshots/5.png)

5. If wrong authentication key is provided , then this error will be raised.
![Alt text](https://github.com/vishalpandeyvip/KongPluginFlaskAPI/blob/main/screenshots/6.png)

6. Creating a consumer who can utilise API keys to send request to our server.
![Alt text](https://github.com/vishalpandeyvip/KongPluginFlaskAPI/blob/main/screenshots/8.png)

7. And at last our API system is running through the Kong API Gateway management.
![Alt text](https://github.com/vishalpandeyvip/KongPluginFlaskAPI/blob/main/screenshots/9.png)
![Alt text](https://github.com/vishalpandeyvip/KongPluginFlaskAPI/blob/main/screenshots/10.png)

## License
[MIT](https://choosealicense.com/licenses/mit/)