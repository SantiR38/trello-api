# Trello endpoints
---

## Create task

`POST http://localhost:8000/api/v1/trello/tasks/`

---

For this request you need to authorize with a bearer token that you get in [the login endpoints](/docs/_build/endpoints/tokens_and_login/).
After sending the request, your card will be created in Trello.

| Parameter    | Type   | Required | Description         |
| :---         | :---:  | :---:    | :---:               |
| name         | string | False    | Task name.          |
| desc         | string | False    | Task description.   |
| category     | string | True     | Task category.      |

---

**Request Example**

```json
{
    "desc": "Lorem ipsum sit ammet",
    "category": "Bug"
}
```

**Response Example**

```json
{
    "name": "Bug-worryingly-35914",
    "desc": "Lorem ipsum sit ammet"
}
```

---