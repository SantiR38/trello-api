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
| first_name            | string | True     | User first name.                      |
| last_name             | string | True     | User last name.                       |
| email                 | string | True     | User email.                           |
| password              | string | True     | Password in string. It'll be hashed.  |

---

#### Request example

```json
{
    "first_name": "John",
    "last_name": "Doe",
    "email": "johndoe@example.com",
    "password": "example1234"
}
```

#### Response example

*Status = 201 Created*
```json
{
    "first_name": "John",
    "last_name": "Doe",
    "email": "johndoe@example.com"
}
```
---


[1]: #sign-up
