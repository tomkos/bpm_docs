# Configuring a single sign-on database

In order to provide single sign-on capabilities, the User Management Service (UMS) issues and validates security tokens and
registers each client (OpenID Connect Relying Party).

1. Create a database for single sign on according to the documentation for your database.
2. Only for UMS versions before 1.1.0: Perform the database setup to create the database tables as
described in Persisting OAuth services with a database store. Note that for
UMS version 1.1.0 and later, these tables are  created automatically during server start if they
don't exist.
3. Copy the Java Database Connectivity (JDBC) driver for the database to
wlp/usr/shared/resources/db.type/.
4 Ensure that the following properties are specified: For more information about these properties, see Specifying basic User Management Service configuration settings
    - db.type
    - oauth.db.name
    - oauth.db.hostname
    - oauth.db.port
    - oauth.db.user
    - oauth.db.password

Next, perform Securing the User Management Service.