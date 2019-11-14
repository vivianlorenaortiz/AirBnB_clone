# AirBnB clone - The console
----------

<img src =
"https://camo.githubusercontent.com/a0c52a69dc410e983b8c63fa4aa57e83cb4157cd/68747470733a2f2f73332e616d617a6f6e6177732e636f6d2f696e7472616e65742d70726f6a656374732d66696c65732f686f6c626572746f6e7363686f6f6c2d6869676865722d6c6576656c5f70726f6772616d6d696e672b2f3236332f4842544e2d68626e622d46696e616c2e706e67">
----------


Table of Contents
----------

*Description<br>
*Purpose<br>
*Requirements<br>
*File Structure<br>
*Usage Examples<br>
*Bugs<br>
*Authors<br>
*License<br>

-----------
Description
----------
----------

This proyect hbnb is a full-stack clone of the web application AirBnB. Thos clone was built in several parts:<br>
*create a command interpreter using the cmd module<br>
*serialize and deserialize a Class<br>
*Write an read JSON file<br>
*manege datetime<br>
*Use *arg and **kwargs<br>
*handle named arguments in a function<br>

------------

Requirements
------------

General
*How to create a Python package<br>
*How to create a command interpreter in Python using the cmd module<br>
*What is Unit testing and how to implement it in a large project<br>
*How to serialize and deserialize a Class<br>
*How to write and read a JSON file<br>
*How to manage datetime<br>
*What is an UUID<br>
*What is *args and how to use it<br>
*What is **kwargs and how to use it<br>
*How to handle named arguments in a function<br>

-----------
## Commands and how to use it                                                                                     
the command interpreter allow us to handle our data requirements with the following commands
                                                                                                                      
| Command | Function |                                                                                                
| ------- | ------------------------------------ |
| create | create a new instace of a class |
| show | show the info of an instance of a class |
| destroy | destroy a instance of a class |
| update | update the info of the objects in an instance |
| all | update the info of the objects in an instance |
| quit | exit the console |
| help | show the help of the commands |

## Objects
this is the objects that you can pass to the command console

| Object | Function |                                                                                                
| ------- | -------- |
| city | city of the reservation |
| state | country state of the reservation |
| place | Name of the place of reservation |
| user | Name of the user who reserves|
| amenity | Benefits of the place |
| review | review of the room and the guest |

-----------
File Structure
------------

*AUTHORS-list of contributors<br>
*-
----------
----------------
Usage
---------------
Enter the executable in your terminal after compiling.
```
(hbnb) all 
["[Place] (473a69fe-c236-417e-ba95-3990852a32da) {'id': '473a69fe-c236-417e-ba95-3990852a32da', 'created_at': datetime.datetime(2019, 11, 14, 1, 22, 32, 925878), 'updated_at': datetime.datetime(2019, 11, 14, 1, 22, 32, 925904), '__class__': 'Place'}", "[Amenity] (1335b3b9-f8fe-414e-8987-ee9cac78d0dc) {'id': '1335b3b9-f8fe-414e-8987-ee9cac78d0dc', 'created_at': datetime.datetime(2019, 11, 14, 1, 22, 39, 729393), 'updated_at': datetime.datetime(2019, 11, 14, 1, 22, 39, 729418), '__class__': 'Amenity'}"]
(hbnb) all User
[]
(hbnb) all BaseModel
[]
(hbnb) 

```
----------


----------
Authors
---------

* **Vivian Ortiz** - [vivianlorenaortiz](https://github.com/vivianlorenaortiz)
* **Camilo Maldonado** - [alt3ralus](https://github.com/alt3ralus)
----------
Licencia
----------

AirBnB Clone is open source and free to download and use
