
# Ticketing-System-Backend

This is a a backend for ticketing system. This project is made using Django REST Framework.


## Live URL 
URL of the Admin Panel 

https://vishveshticket.herokuapp.com/admin
## API Reference

### Create User 
There can be basically two types of user/role - admin or employee

```http
  POST /users/new
```

| Body|  Description                       |
| :-------- | -------------------------------- |
| `username`      | **Required**. |
| `password`       | **Required**. |
| `role`  | **Required**. Role can be 'admin' or 'employee' only|
                 

It return a Auth Token which will required in all other endpoints.

### Create Tickets
Tickets can only be created by admin.

```http
  POST /tickets/new
```


| Body |  Description                       |
| :-------- |  :-------------------------------- |
| `title`      | **Required** Title of the ticket|
| `description`      |**Required**  Description of ticket |
| `assigned`      |**Required** Username of the user to whom this ticket has to be assigned. |
| `priority` | **Required** low / medium / high |

It returns the id of the ticket created.



### Get all Tickets

```http
  GET /tickets/all
```

### Query Tickets

```http
  GET /tickets/[param]
```

Query Parameters
| Parameter |  Description                       |
| :-------- |  :-------------------------------- |
| `status`      |  open / close |
| `title`      |  search for a ticket with this title |
| `priority`      | low / high / medium  |

### Closing Tickets
Tickets can only be closed by admin or to whom the ticket is assigned.

```http
  POST /tickets/markAsClosed
```

| Body|  Description                       |
| :-------- | -------------------------------- |
| `ticketID`      | **Required**. ID of the ticket that needs to be closed |

### Delete Tickets
Tickets can only be deleted by admin.


```http
  POST /tickets/delete
```

| Body|  Description                       |
| :-------- | -------------------------------- |
| `ticketID`      | **Required**. ID of the ticket that needs to be deleted |






