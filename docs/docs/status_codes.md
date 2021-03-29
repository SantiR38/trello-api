# Status codes
---

**Space-x** uses some status codes by default.


## 2xx - Successful

This class of status code indicates that the client's request was successfully received, understood, and accepted.

```plain_text
HTTP_200_OK
HTTP_201_CREATED
HTTP_204_NO_CONTENT
```

## 4xx - Client Error

The 4xx class of status code is intended for cases in which the client seems to have erred. Except when responding to a HEAD request, the server SHOULD include an entity containing an explanation of the error situation, and whether it is a temporary or permanent condition.

```plain_text
HTTP_404_NOT_FOUND
HTTP_422_UNPROCESSABLE_ENTITY
```

## 5xx - Server Error

Response status codes beginning with the digit "5" indicate cases in which the server is aware that it has erred or is incapable of performing the request. Except when responding to a HEAD request, the server SHOULD include an entity containing an explanation of the error situation, and whether it is a temporary or permanent condition.

```plain_text
HTTP_500_INTERNAL_SERVER_ERROR
```