# Tokens and login endpoints
---

## Index

#### Environment variables

`{host}`: Ip or domain.

*Example: `{host}`/api/token/ == www.example.com/api/token/*

#### URLs List

| Resource                                         | POST                                   | GET                            |
| :----                                            |     :-----:                            | :---:                          |
| [`{host}`/api/token/][1]                         | Get Access and refresh tokens (log in) ||
| [`{host}`/api/token/refresh/][2]                 | Get Access tokens from refresh token.  ||
| [`{host}`/api/token/verify/][3]                  | Validate tokens expiration.            ||

`*` Only Admin users have access.

`#` No authentication required.

---

## api/token/

*This endpoint should only be used for login in. For redirections and reloads use the refresh endpoint.*

### POST

| Parameter             | Type   | Required | Description          |
| :---                  | :---:  | :---:    | :---:                |
| email                 | string | True     | User email.          |
| password              | string | True     | Password in string.   |

---

#### Request example

```json
{
    "email": "johndoe@example.com",
    "password": "example1234"
}
```

#### Response example

*Status = 200 OK*
```json
{
    "refresh": "eyJ0eXAiOi.JKV1QiLCJhbGc.iOiJIUzI1N",
    "access": "eyJ0eXAiOi.JKV1QiLCJhbGc.iOiJIUzI1N"
}
```
---

## api/token/refresh/

### POST

| Parameter      | Type   | Required | Description          |
| :---           | :---:  | :---:    | :---:                |
| refresh        | string | True     | User refresh token.  |

---

#### Request example

```json
{
    "refresh": "eyJ0eXAiOi.JKV1QiLCJhbGc.iOiJIUzI1N"
}
```

#### Response example

*Status = 200 OK*
```json
{
    "access": "eyJ0eXAiOi.JKV1QiLCJhbGc.iOiJIUzI1N"
}
```
---


## api/token/verify/

### POST

| Parameter      | Type   | Required | Description       |
| :---           | :---:  | :---:    | :---:             |
| token          | string | True     | User token.       |

---

#### Request example

```json
{
    "token": "eyJ0eXAiOi.JKV1QiLCJhbGc.iOiJIUzI1N"
}
```

#### Response example

*Status = 200 OK*
```json
[]
```
or

*Status = 401 Unauthorized*
```json
{
    "detail": "Token is invalid or expired",
    "code": "token_not_valid"
}
```
---

[1]: #apitoken
[2]: #apitokenrefresh
[3]: #apitokenverify