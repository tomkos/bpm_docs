# Securing the User Management Service

The User Management Service web
application is secure by default, and it employs standard protections
against threats such as Cross Site Request Forgery, Cross Frame Scripting,
and Cross Site Scripting, however the following additional security
actions are necessary:

1. For maximum security, users must only connect to a web server
that is in a demilitarized zone (DMZ) and never connect to the IBM®
WebSphere® Application Server Liberty server
directly. This topology provides great flexibility in terms of hostnames,
HTTPS, HTTP header, request filtering and other protections. For example,
configuring HTTPS strict transport security for Liberty recommends
adding an HTTP response header in your web server configuration as
described in Securing Liberty by using HTTP Strict Transport Security
(HSTS).
2. A secure environment requires you to stay up-to-date with security
patches. Because the User Management Service is built on
Liberty which in turn builds on Java and WebSphere Application
Server, you must
subscribe to security bulletins for all three of them. For more information,
see My Notifications
3. Install security fixes for your Liberty runtime.
4. Ensure that all passwords for local users, keystores, and the
SSO database that are stored in User Management Service configuration
files are obfuscated by using the securityUtility command .

Next, perform Configuring single sign-on.