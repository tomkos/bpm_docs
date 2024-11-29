<!-- image -->

# Sending emails for escalations

## Before you begin

- Your people directory provider must support the specification
of email addresses, such as Lightweight Directory Access Protocol
(LDAP) or virtual member manager.
- The Everybody, Nobody, Group and Users
by user ID people assignment criteria are not supported.
For example, use User records by user ID instead.

## Procedure

1 In Integration Designer ,perform the following actions for the task in the Human Task editor.
    1 Under the task settings in the Details tabof the properties area, edit the value of the People directory(JNDI name) field. Set this field to oneof the following values:
        - bpe/staff/samplevmmconfiguration
        - bpe/staff/samplevmmconfiguration
        - The people directory configuration name (JNDI name) of your choice.
2. Under the escalation settings in the Details tab
of the properties area, set the value of the Notification
type field to E-mail.
3. Optional: Specify text for the body of the
email that is sent for the escalation. To insert a variable
to include task specific information into the text, click Add
Variable and select an appropriate variable from the list.
In the editor, the variable will appear between "%" characters, but
will be replaced when it is evaluated during execution in the runtime
environment when the email is sent.
If
you do not specify any text, the default message text is used.
2 In the administrative console for Workflow Server , performthe following actions.

1. Ensure that the simple mail transfer protocol (SMTP)
host is set. If authentication is enabled, set the User ID and password
for the SMTP host. In the administrative console, click Resources > Mail  > Mail
Sessions > HTMMailSession\_nodeName\_serverName to check this setting, or Resources > Mail  > Mail Sessions > HTMMailSession\_clusterName if Business Process Choreographer is configured on
a cluster. The SMTP host is defined on the cell level.
2. Ensure that the sender email address (Sender
e-mail address) that you specify when you configure the
human task manager is a valid email address. In the
administrative console, click Servers > Clusters > cluster\_name.
On the Configuration tab, in the Business
Process Manager section, click Business
Process Choreographer > Human Task Manager.

## What to do next