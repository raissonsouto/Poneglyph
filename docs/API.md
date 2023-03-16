# Authentication and Authorization Server Documentation

This documentation outlines the endpoints and request/response format for the Authentication and Authorization Server.

## Authentication

### Register

```
POST /auth/register
```

#### Request Body

| Parameter | Type   | Description         |
| --------- | ------ | ------------------- |
| username  | string | The user's username. |
| password  | string | The user's password. |

#### Response

| Parameter     | Type   | Description                                      |
| ------------- | ------ | ------------------------------------------------ |
| access_token  | string | The access token for the authenticated user.     |
| token_type    | string | The type of token, typically "Bearer".           |
| expires_in    | number | The number of seconds until the token expires.   |
| refresh_token | string | The refresh token that can be used to get a new access token. |

#### Example

```
POST /auth/login
{
    "username": "user",
    "password": "password"
}

HTTP/1.1 200 OK
{
    "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9",
    "token_type": "Bearer",
    "expires_in": 3600,
    "refresh_token": "CfDJ8"
}
```

### Login

Allows a user to authenticate and receive an access token that can be used for subsequent requests.

```
POST /auth/login
```

#### Request Body

| Parameter | Type   | Description         |
| --------- | ------ | ------------------- |
| username  | string | The user's username. |
| password  | string | The user's password. |

#### Response

On success, returns an access token that can be used for subsequent requests.

| Parameter     | Type   | Description                                      |
| ------------- | ------ | ------------------------------------------------ |
| access_token  | string | The access token for the authenticated user.     |
| token_type    | string | The type of token, typically "Bearer".           |
| expires_in    | number | The number of seconds until the token expires.   |
| refresh_token | string | The refresh token that can be used to get a new access token. |

#### Example

```
POST /auth/login
{
    "username": "user",
    "password": "password"
}

HTTP/1.1 200 OK
{
    "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9",
    "token_type": "Bearer",
    "expires_in": 3600,
    "refresh_token": "CfDJ8"
}
```

### Change Password

```
POST /auth/change-password
```

#### Request Body



#### Example

```

```

#### Lost Password
#### Enable 2FA

## Authorization

### Add a Role
```
POST /authz/add-role
```

#### Request Body

| Parameter | Type   | Description                                                                               |
|-----------| ------ |-------------------------------------------------------------------------------------------|
| role name | string | The role name.                                                                            |
| superior  | string | If there is a role above this one pass the name, if it doesn`t, just pass in empty string |

#### Response

| Parameter     | Type   | Description                                      |
| ------------- | ------ | ------------------------------------------------ |
| access_token  | string | The access token for the authenticated user.     |
| token_type    | string | The type of token, typically "Bearer".           |
| expires_in    | number | The number of seconds until the token expires.   |
| refresh_token | string | The refresh token that can be used to get a new access token. |

#### Example

```
POST /authz/add-role
{
    "token": "h2lkj34h5jkl23h45jkl2"
    "role_name": "tenant",
    "superior": "admin"
}

HTTP/1.1 200 OK
{
    ???
}
```
### Delete a role
### Add a user to a role
### Remove a user from a role


### User non-authentication/authorization related features

#### Update email
#### Update phone
#### Get email
#### Get phone

### Roles non-authentication/authorization related features

#### Update role name
#### Get all users from role