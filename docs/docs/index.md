# SPACE-X PROJECT
---

By **Space-x**.

In this site you will find all the needed documentation to undestand all the functions of the API.


## Documentation

If you want to **see the docs in web format**, you'll have to do some steps.

1. Execute in terminal `docker-compose -f local.yml up docs`. This will create the `_build` directory with all the web structure for the docs.

2. Download and install `ritwickdey.liveserver` extension for VS code. If you have another editor, search for another live server.

3. Open the `docs/_build/index.html` file in VS Code. Press "Go Live", and automatically the browser will open the docs in web format.

## GETTING STARTED

Once you have your documentation running in your localhost, let's start with the configuration. These steps are optimized for linux, that is the OS that you will use in production right?

### Sign up

First of all, you have to register your user in the url `http://localhost:8000/api/v1/users/sign-up/` with the following data:
```json
{
    "email": "johndoe@example.com",
    "password": "example1234",
    "trello_key": "<your-trello-key>",
    "trello_token": "<your-trello-token>",
    "trello_username": "johndoe1"
}
```

**Request Example**

```shell
curl --header "Content-Type: application/json" \
    --request POST \
    --data '{ "email": "johndoe@example.com", "password": "example1234", "trello_key": "d13dfb06s56s2d31f9dfca2", "trello_token": "45sd45f5s60f9967c035565sfd65465dfs4gsd654d25e95e8e163df5g4603e5", "trello_username": "johndoe1"}' \
    http://localhost:8000/api/v1/users/sign-up/
```

**Response Example**

*Status 201 Created*
```json
{"trello_key":"d13dfb06s56s2d31f9dfca2","trello_token":"45sd45f5s60f9967c035565sfd65465dfs4gsd654d25e95e8e163df5g4603e5","trello_username":"johndoe1","email":"johndoe@example.com"}
```

You can get the Trello credentials by accesing the https://trello.com/app-key.

### Get access token

This site uses JWT for authentication. So if you will need the access token in order to use the funcionality of this application.

URL: http://localhost:8000/api/token/

**Data:**
```json
{
    "email": "johndoe@example.com",
    "password": "example1234"
}
```

**Request Example**

```shell
curl --header "Content-Type: application/json" \
    --request POST \
    --data '{ "email": "johndoe@example.com", "password": "example1234"}' \
    http://localhost:8000/api/token/
```

**Response Example**

*Status 200 OK*
```json
{"refresh":"bvvbncvncGciOiJIUzI1NiJ9.eyJdghdgfl90eXBlIjoicmVmcmVzaCIsvbcnety4NjUwMSwianRpIjoiNTA3NjY1MmFmMGQxNGQ1MWE5ZTI0MjIxNGvbndfhdtrjoyfQ.vk8QIye42umH__PQ7asdfxzcvetrDOY3t0aCzoI","access":"eyJ0eXAiadsf6487qiLCJhbGciOiJIUzI1NiJ9.eyJ0b26a5s65adf8q9eXBlIjoiYWNiwiZXhwIjoxNjE3MTAwNDAxLCJqdGkiOiI2MDE3MTc0Y2EzMWI0MTg4Ym65hjgkj645ZmVlNSIsInVzZXJfaWQiOjJ9.dPb6asd5f498M39f2Q60_0y8woQUWPPAVnGVaojAM"}
```

Now you have to use the **access token** for the following views.

