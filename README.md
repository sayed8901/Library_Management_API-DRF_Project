# Library Management System API Documentation

## Overview

The **Library Management System API** provides endpoints for managing books, authors, members, and borrowing activities in a library. Built using Django and Django REST Framework, this API offers robust features for efficient library operations.


### Admin Panel Access

The Django Rest Framework Admin Panel can be accessed using the following credentials:

- **Username**: `sayed`  
- **Password**: `sayed8901`  



## API Endpoints

### Base URL
`https://library-management-api-bix8.onrender.com`

### Authentication

- **Admin Login**:  
  `POST` - `/admin/login/`  
  Allows the admin to log in.

- **User Register**:  
  `POST` - `/accounts/register/`  
  Allows the a new user to register.

- **User Login**:  
  `POST` - `/accounts/login/`  
  Authenticates any user and generates a session token.

- **User Logout**:  
  `GET` - `/accounts/logout/`  
  Logs out the currently authenticated user.

### Library Book Management - Only by **Admin user**

- **Add New Category**:  
  `POST` - `library/categories/`  
  Allows adding a new category to the library.

- **List All Categories**:  
  `GET` - `library/categories/`  
  Retrieves a list of all categories in the library.

- **Modify a Category**:  
  `GET`, `PUT`, `PATCH`, `DELETE` - `library/categories/<id>/`  
  Modify a category data by category ID.


- **Add New Book**:  
  `POST` - `library/books/`  
  Allows adding a new book to the library.

- **List All Books**:  
  `GET` - `library/books/`  
  Retrieves a list of all books in the library.

- **Modify a Book**:  
  `GET`, `PUT`, `PATCH`, `DELETE` - `library/books/<id>/`  
  Modify a book data by book ID.

- **Get All the Available Books**:  
  `GET` - `library/available_books/`  
  Get all the available books list


### Member Management

### Borrowing Management

- **Borrow a Book**:  
  `POST` - `activity/borrow/<id>/`  
  Allows a member to borrow a book by book ID.

- **List Borrowed Books**:  
  `GET` - `activity/borrowed_books/`  
  Retrieves a list of all borrowed books for a particular member.

- **Return a Book**:  
  `POST` - `activity/return/<id>/`  
  Allows a member to return a book by book ID.


<br>

## Sample requests for model schemas:

### To register a new user		- POST

```bash
{
    "username": "sohel",
    "first_name": "Md. Sohel",
    "last_name": "Rana",
    "email": "sdssayed24@gmail.com",
    "password": "sayed8901",
    "confirm_password": "sayed8901",
    "user_type": "member"
}
```



### To login		- POST

```bash
{
    "username" : "sohel",
    "password" : "sayed8901"
}
```


### To add category		- POST

```bash
{
    "name": "Short Story"
}
```



### To add book		- POST

```bash
{
    "title": "The Call of the Wild",
    "author": "Jack London",
    "description": "Set in the Yukon",
    "quantity": 10,
    "category": 1
}
```
