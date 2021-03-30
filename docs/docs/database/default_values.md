# Default Values
---

Some tables have default values that are going to help you to integrate the endpoints without creating testing values.
Most of this values will persevere in producción.

## User

You don't need to create a superuser account after installing the project, but if you need to create a client account, it will be avaliable an endpoint for that.

**Alert:** This account must be deleted in production after testing.

| id    | username | email           | password  |
| :---: | :---:    | :---:           | :---:     |
|   1   | admin    | admin@admin.com | admin1234 |

---

## Category

There are three default values for `Category` model. 

| id    | name             |
| :---: | :---:            |
|   1   | Mantenimiento    |
|   2   | Investigación    |
|   3   | Prueba           |

---

## Status

There are three default values for `Status` model. 

| id    | name   |
| :---: | :---:  |
|   1   | Issue  |
|   2   | Bug    |
|   3   | Task   |

---