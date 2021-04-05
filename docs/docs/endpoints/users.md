# Sign up endpoint
---

With this endpoint you can create your own user account.

`POST http://localhost:8000/api/v1/users/sign-up/`

| Parameter             | Type   | Required | Description                           |
| :---                  | :---:  | :---:    | :---:                                 |
| email                 | string | True     | User email.                           |
| password              | string | True     | Password in string. It'll be hashed.  |
| trello_key            | string | True     | User trello key.                      |
| trello_token          | string | True     | User trello token.                    |

---

#### Request

```json
{
    "email": "johndoe@example.com",
    "password": "example1234",
    "trello_key": "<your-trello-key>",
    "trello_token": "<your-trello-token>"
}
```

Once you meke the request, your Trello credentials will be validated. If one or both of them are incorrect, an error message will appear.

## Error response

*Status = 422 Unprocessable Entity*
```json
{
    "detail": [
        "Your trello key or token are incorrect."
    ],
    "status_code": 422
}
```

If the credentials are valid, they are going to be saved in the user db instance. Also, a board called **Space-X tasks** will be automatically created in Trello.

#### Successful response

*Status = 201 Created*
```json
{
    "email": "johndoe@example.com",
    "trello_board_id": "<your-new-trello-board-id>",
}
```
---