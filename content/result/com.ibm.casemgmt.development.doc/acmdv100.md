# Authentication for external data services

If Content Platform Engine and
the external data service do not use the same WebSphere® Application
Server profile, you must set up
Lightweight Third Party Authentication (LTPA) security between the
applications in WebSphere Application
Server.
Begin by exporting the LTPA key from the Content Platform Engine server.

If the request contains either of these authentication values, WebSphere Application
Server first authenticates with
the LDAP server, if one is configured. WebSphere Application
Server then sets up a JAAS subject
in the calling context of the external data service. To retrieve this
JAAS subject, you can use one of the WebSphere Application
Server Java™ APIs. Alternatively, you can use the helper
method javax.security.auth.Subject getAmbientSubject( ) that
is defined for the UserContext class in the Content Platform Engine Java API.