# Trello endpoints
---

## Index

#### Environment variables

`{url}`: `{host}`/api/v1/trello

*Example: `{url}`/trello/boards/ == www.example.com/api/v1/trello/boards/*

#### URLs List

| Resource                       | POST         | GET          |
| :----                          |     :-----:  | :---:        |
| [`{url}`/boards/][1]           |              | List boards. |


`*` Only Admin users have access.

`#` No authentication required.

---

## boards/

### GET

Before creating a task, you need to consume this endpoint in order to get the `idList` of the List where you want to save your cards.
The access token is the only parameter this endpoint will need.

**Request Example**

```shell
curl --header "Authorization: Bearer {your-access-token}" \
    --request GET \
    http://localhost:8000/api/v1/trello/boards/
```

**Response Example**

```json
[
    {
        "id": "3klj2435kj2n4lk5j24n3lkj",
        "name": "Reportes",
        "url": "https://trello.com/b/lk23jk4/reportes",
        "lists": [
            {
                "id": "3klj2435kj2n4lk5j24n3lkj",
                "name": "Documentos Anexos"
            },
            {
                "id": "3klj2435kj2n4lk5j24n3lkj",
                "name": "Reportes de backoffice"
            }
        ]
    },
    {
        "id": "3klj2435kj2n4lk5j24n3lkj",
        "name": "Tareas",
        "url": "https://trello.com/b/lk23jk4/tareas",
        "lists": [
            {
                "id": "3klj2435kj2n4lk5j24n3lkj",
                "name": "Lista de tareas"
            },
            {
                "id": "3klj2435kj2n4lk5j24n3lkj",
                "name": "En proceso"
            },
            {
                "id": "3klj2435kj2n4lk5j24n3lkj",
                "name": "Hecho"
            }
        ]
    }
]
```

---

[1]: #boards