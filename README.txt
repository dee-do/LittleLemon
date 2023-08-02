API paths to test:

skeleton index page:                            /restaurant/ 
get all menu items, create a menu item:         /restaurant/menu/
get, update, delete single menu item:           /restaurant/menu/id/

get all bookings, create a booking:             /restaurant/bookings/
get,update,delete single booking:               /restaurant/bookings/id/

The project uses djoser for token auth, so all the urls provided by djoser can be used. For example:
retrieve all users, create a user:              /auth/users
enter username and password to obtain token:    /auth/token/login/
logout:                                         /auth/token/logout