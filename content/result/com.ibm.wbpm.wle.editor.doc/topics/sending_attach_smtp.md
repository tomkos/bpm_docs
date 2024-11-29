# Sending attachments using an SMTP server (deprecated)

## Before you begin

To perform
this task, you must be in the IBM® Process
Designer desktop
editor, which is deprecated.

Check
that your system administrator set up the SMTP server. You must know
its URL address when you complete the following procedure.

## Procedure

1. Open the desktop Process Designer (deprecated).
2. Create an integration service.
3. In the Integration service, add a Java Integration component.
4. In the Variables tab, add an input
variable with a Boolean value set to true.
The input variable instructs the SMTP server to use file names
to identify attachments instead of a full path name. For example,
use a name like useFileName.
5. Create all the other variables to pass values to the SMTP
server. Use them later in the Data Mapping section.
6. On the Definition tab, select the teamworks.Mail class
and the sendMessage method that includes the
Boolean parameter.
7. In the Data Mapping section, add the variables that are
expected by the SMTP server, including a variable for your attachments.
In the Replace Full Paths By File Names field,
add the variable that you created earlier to indicate that you are
specifying the names of the files that are being transferred and that
you are not using the full path name for them.