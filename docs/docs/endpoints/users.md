# User endpoints
---

## Index

#### Environment variables

`{url}`: `{host}`/api/v1/users

*Example: `{url}`/sign_up/ == www.example.com/api/v1/users/sign-up/*

#### URLs List

| Resource                        | POST                  | GET                   | PUT               | DELETE          |
| :----                           |     :-----:           |      :-----:          |     :-----:       |     :-----:     |
| [`{url}`/sign-up/][1]           | Create User#          ||||

`*` Only Admin users have access.

`#` No authentication required.

---

## sign-up/

### POST

| Parameter             | Type   | Required | Description                           |
| :---                  | :---:  | :---:    | :---:                                 |
| email                 | string | True     | User email.                           |
| password              | string | True     | Password in string. It'll be hashed.  |
| trello_key            | string | True     | User trello key.                      |
| trello_token          | string | True     | User trello token.                    |

---

#### Request example

```json
{
    "email": "johndoe@example.com",
    "password": "example1234",
    "trello_key": "<your-trello-key>",
    "trello_token": "<your-trello-token>"
}
```

#### Response example

*Status = 201 Created*
```json
{
    "email": "johndoe@example.com",
    "trello_key": "<your-trello-key>",
    "trello_token": "<your-trello-token>"
}
```
---


[1]: #sign-up
