<!-- image -->

# Customizing an escalation email notification

## About this task

Before you can customize the email notification, it is necessary to configure the
IBM® Workflow
Server as described in Sending emails for escalations.

## Procedure

1. Create an escalation for your human task.
2. In the Details page of the properties
area select email as the Notification
type. The email message field
becomes active with the default message selected automatically.
3. To create a new email message, select New from
the email message drop down list.
4 To make changes to an email message, first select it fromthe email message drop down list, and click Edit . The email editor will launch with the emailDefinition window where you can edit the email that getssent as a notification.To configure the email message, proceedas follows:

To configure the email message, proceed
as follows:

    1. Give the email message a name and a subject. To
insert a human task variable into the text of the subject, click Add
Variable and select an appropriate variable from the list.
In the editor, the variable will appear between "%" characters, but
will be replaced when it is evaluated in the runtime environment when
the email is sent.
    2. Compose your message in the email window
in HTML language. When you enter a "<" symbol, a list
of possible HTML code tags will appear along with a description of
what that tag would be used for. Click the tag you want to use, and
hit enter. As before, you can insert a human task variable by clicking Add
Variable.Tip: If you are composing a brand
new email message, and are unsure of how to proceed, take a look at
the existing default message for ideas.
    3. To see what your email message will look like when it
is delivered, click the Preview tab.