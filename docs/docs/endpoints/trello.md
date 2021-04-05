# Trello endpoints
---

## Create task

`POST http://localhost:8000/api/v1/trello/tasks/`

---

**Request Example**

```shell
curl --header "Authorization: Bearer {your-access-token}" \
    --request POST \
    --data '{"desc": "Lorem ipsum dolor sit ammet", "category": "Bug"}' \
    http://localhost:8000/api/v1/trello/tasks/
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
