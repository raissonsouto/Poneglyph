Here you will find all the specification to the Bifrost REST API.

## Authentication related

```
POST: https://host:10373/auth/login

body:
{
    username: steve,
    password: evets
}
```

## Aurhorization related

```
POST: https://host:10373/roles/add

body:
{
    token: 123123,
    user-id: 433,
    role: student
}
```

Return
- 200
- 400