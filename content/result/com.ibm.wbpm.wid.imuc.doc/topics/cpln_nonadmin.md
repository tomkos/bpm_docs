# Considerations for installing Db2 with IBM Integration
Designer

Before you install Integration Designer with Db2, review the
information in this topic.

For information about required user accounts for installing Db2 on Windows, refer
to Required user accounts for installation of Db2 server products
(Windows).

If you have an instance of Db2 already installed, it must be using port 50000 for a typical
installation of IBM Integration
Designer with a test environment to succeed. If your existing Db2 instance is not using port 50000, either
change it to 50000, or use a silent installation method (command line or response file) and use the
BPMConfig command to configure the test environment with a custom Db2 port
number.

- Before installing the product, install a Db2 server separately.
- Log on as an administrator and use the product installer to install the Db2 server alone. Grant
special permission to the non-administrative user. The non-administrative user
must be part of the DB2USERS group. This will allow the user to read and write to the database.
Then log on as the non-administrative user and install the product using the installed Db2
server.

- Setting up Windows elevated privileges before installing a Db2 product
(Windows)
- Required user accounts for installation of Db2 server products (Windows)
- Non-root installation overview (Linux and UNIX)