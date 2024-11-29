# Configuring Business Automation Workflow for GDPR
readiness

## Secure configuration

Many features are
provided for ensuring that your runtime environment and applications
are secure. For more information about securing your configuration,
see Creating a secure environment.

## Encrypt data in motion

By default, all communications
in all layers are encrypted, for example, using HTTPS, JDBC over TLS,
SMTP over SSL, and LDAP over TLS. Although it might be acceptable
to use unencrypted connections on a test system that does not process
user information, to comply with GDPR you must ensure that all communications
by production systems are encrypted. For more information about Secure
Sockets Layer and web service security, see Data integrity and privacy.

For information about configuring secure communications in IBM® Business Automation
Workflow, see Configuring security for case management solutions.

For information about configuring secure communications in IBM
FileNet® P8, including your Content Platform Engine object store is secure, see the topics in the Security section.

For information about configuring secure communications in a Db2® database, see  TLS configuration of Db2.

For information about configuring secure communications in WebSphere® Application
Server, see Securing applications and their environment.

## Encrypt data at rest

- To ensure that all data in the database is encrypted, you can
host the database on an encrypted file system, such as Linux Unified
Key Setup (LUKS) disk encryption.
- To ensure that all other data, such as log files, configuration
files or full text search indexes, is encrypted, you can host the
product installation directory on an encrypted file system, such as
LUKS.

For more information about LUKS, see LUKS:
Disk Encryption.

## Changeable BPM logon user IDs

Allowing users
to log on using a personal identifying attribute, such as an email
address, is convenient for your users. But for privacy reasons, or
when they change their name or change their email address, users should
be able to change their logon ID. BPM associates user preferences
and task assignments with user names, this means that changing the
user name effectively creates a new account in the database, without
any relation to existing user preferences and task assignments.

A
best practice is to decouple the logon ID (the value that users enter
on the logon page) from the internal user identifier (the value that
is stored in the product database) by configuring multiple logon properties.
The first login property should be a stable non-personal identifier,
whereas the second property can be any unique attribute. For more
information about configuring an LDAP, see Configuring the user registry.

## User attributes

User attributes that are
stored in the BPM database can be used to store sensitive personal
information such as job titles, phone numbers and email addresses.
User attributes that are defined as public can be
read by any other users. For information about retrieving and deleting
this information, see Configuring the user registry.

## Prevent recording of sensitive information in audit logs and case history

You can configure IBM Business Automation
Workflow to record any
solution property in the case history and audit logs. However, you cannot remove the values from
these locations. Therefore, it is recommended that you do not configure IBM Business Automation
Workflow to record any property that stores personal data
in the case history or audit logs.

Case history also contains personal data, such as the case creator, that is a permanent part of
the historical case data. This information cannot be removed.

## Prevent logging and tracing of sensitive information

If you encounter a problem with Business Automation Workflow, you might
need to provide trace logs to IBM support. These logs can
contain personal data. Before you send a log file to IBM support, edit the file to mask any personal
data.

## Malware protection

Business Automation Workflow allows end users and administrators to
upload files, for example, when deploying applications or associating a document with a process
instance. In some scenarios, these files might exist briefly on the server's file system. To
mitigate the risk that such files might contain malware, you can install an antivirus utility to run
on each server and configure it to protect all product and temporary directories.