# Error occurs when importing process applications

```
ERROR [org.apache.catalina.core.ContainerBase] Servlet.service() for servlet ImportSnapshotServlet threw exception
java.io.IOException: The system cannot find the path specified
```

This
error occurs when you do not have permission to write to the temporary
directory that the operating system uses during the import process.

- DB2 engine SQL error, SQLCODE
= -913
- SQLSTATE = 57033

To resolve this issue, increase the value of the DB2 for z/OS system parameter for resource timeouts
(IRLMRWT). This value is measured in seconds. For more information,
see RESOURCE TIMEOUT field (IRLMRWT subsystem parameter) in
the DB2 for z/OS documentation.

- Granting permission to write to the temp directory

If an import process fails because the system cannot find the path specified, modify permission settings for the temporary directory that the operating system uses during the import process.