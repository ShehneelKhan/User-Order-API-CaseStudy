# User-Order-API-using-DRF 

API Documentation
------------

# Register URL
------------


### Endpoint: api/register/

### Method: POST
### Description: Register a new user with a unique email and username.
### Permissions: This API can be accessed by anyone without authentication.
### Request Parameters:
### username: A string representing the username of the new user.
### email: A string representing the email of the new user.
### password: A string representing the password of the new user.
### confirm_password: A string representing the confirmation of the new user's password.
### Response:
### If the request data is valid and the user is successfully registered, returns the registered user's details including id, username
### If the request data is not valid, returns a validation error message in JSON format.
<br><br>
# login URL
<br><br>
### Endpoint: api/login/
### Method: POST
### Description: Obtain an authentication token for a registered user using their username and password.
### Permissions: This API can be accessed by anyone without authentication.
### Request Parameters:
### username: A string representing the username of the registered user.
### password: A string representing the password of the registered user.
### Response:
### If the request data is valid and the user is successfully authenticated, returns a token in JSON format that can be used for further authenticated requests.
### If the request data is not valid or the user is not authenticated, returns an authentication error message in JSON format.
<br><br>
# logout URL
<br><br>
### Endpoint: api/logout/
### Method: POST
### Description: Log out an authenticated user by deleting their authentication token.
### Permissions: This API can only be accessed by authenticated users.
### Response:
### If the user is successfully logged out, returns a HTTP 200 OK response.
### If there is an error logging out, returns an error message in JSON format.
<br><br>



### Users
<br><br>
### Retrieve a list of all users
<br><br>
### Endpoint: api/users/
### Method: GET
### Allowed Roles: Super Admin
### Description: Retrieve a list of all users.
### Request Parameters: None
### Response:
![image](https://github.com/ShehneelKhan/User-Order-API-CaseStudy/assets/45147081/bd48f243-fff3-4e2b-bd29-5a359e964078)
<br><br>


### Retrieve a user by ID
### Endpoint: api/users/<int:pk>/
### Method: GET
### Allowed Roles: Super Admin
### Description: Retrieve a user by ID.
### Request Parameters: None
### Response:
![image](https://github.com/ShehneelKhan/User-Order-API-using-DRF/assets/45147081/4da9a128-5b3d-4ae8-a340-a4abf392044b)


<br><br>
### Orders
<br><br>
### Retrieve a list of all orders
### Endpoint: api/orders/
### Method: GET
### Allowed Roles: Owner, Super Admin
### Description: Retrieve a list of all orders.
### Request Parameters: None
### Response:
![image](https://github.com/ShehneelKhan/User-Order-API-using-DRF/assets/45147081/9341c3ff-3c97-4be5-a28b-395748ee9435)

<br><br>
### Retrieve an order by ID
<br><br>
### Endpoint: api/orders/<int:pk>/
### Method: GET
### Allowed Roles: Owner, Super Admin
### Description: Retrieve an order by ID.
### Request Parameters: None
### Response:
![image](https://github.com/ShehneelKhan/User-Order-API-using-DRF/assets/45147081/dc5141d4-bd22-43ec-b91a-4b43ebbede50)



<br><br>
### Retrieve orders by user emails
### Endpoint: api/orders/by-emails/
### Method: GET
### Allowed Roles: Super Admin
### Description: Retrieve orders owned by users having email addresses in the provided list.
### Request Parameters:
### email - The email addresses of the users to retrieve orders for.
### Example: /orders/by-emails/?email=john_doe@example.com&jane_doe@example.com
### Response:
![image](https://github.com/ShehneelKhan/User-Order-API-using-DRF/assets/45147081/9bff21fc-8fdc-4957-8072-9d050bb256f8)



















