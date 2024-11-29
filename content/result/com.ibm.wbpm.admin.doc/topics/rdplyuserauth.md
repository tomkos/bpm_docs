<!-- image -->

# User authentication

- J2C authentication alias: Using a J2C authentication data entry, or authentication alias,
created with the Java Authentication and Authorization Service (JAAS) feature of Java EE security is
a secure way to deploy applications. An administrator creates the authentication alias that is used
by one or more applications that need to access a system. The user name and password must be known
only to that administrator, who can change the password in a single place, when a change is
required.
- Adapter properties: Saving the user name and password in adapter properties is a direct way to
provide this information at run time. You provide this user name and password when you use the
external service wizard to configure your module. Although directly specifying the user name and
password seems the most straightforward method, it has important limitations. Adapter properties are
not encrypted; the password is stored as clear text in fields that are accessible to others on the
server. Also, when the password changes, you must update the password in all instances of the
adapter that access that server. This update includes the adapters that are embedded in application
EAR files and adapters that are separately installed on the server.