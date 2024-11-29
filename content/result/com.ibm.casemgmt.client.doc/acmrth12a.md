# Configuring email notifications for quick tasks assignments

## About this task

You can configure your target object store so that email notifications to alert case workers when
quick tasks are assigned to them. In addition, you can customize the email templates that are used
for these notifications. To configure email notifications for quick tasks assignments:

## Procedure

1. Ensure that the LDAP user definitions include the email addresses for any case workers to
whom quick tasks are assigned.
2. Log in to the Administration Console for Content Platform
Engine.
3 Configure the SMTP server in the IBM®FileNet® P8 domain: For more information, see Configuring email notifications for the FileNet P8domain
    1. In the Domain Navigation panel, select the Server
Hierarchy object. For example, if you want to access the subsystem properties at the
site level, expand the Sites folder and select a site.
    2. In the detail panel, click the SMTP Subsystem
tab.
    3. Select the Enable email notifications checkbox.
    4. Enter the host name and port values for your SMTP server.
    5. In the Default email reply-to ID, Email login ID,
and Email login password fields, enter the email information for the sender
of the quick task assignment email notifications.
4 Ensure that the email services add-on extension is installed. For more information, see Installing an add-on feature to an object store

1. In the domain navigation panel, expand Object stores and
right-click your target object store. Click Install Add-on
Features.
2. Ensure that Email Services Extensions is listed in the
Installed add-on features table.

## What to do next

Case management provides a default email template, called
QuickTaskAssignedEmailTemplate, for assignment notifications. This template uses
HTML code, which you can easily customize. By default, emails that are created with this template
have the following subject line: You have been assigned the quick task
quick\_task\_name. To customize the email template:

1. Log in to the Administration Console for Content Platform
Engine.
2. In the domain navigation panel, expand Object stores and open your target
object store.
3. Expand Email template and open the email template that you want to
customize.
4. Modify the Subject and Body fields as needed.
You enter parameters in these fields as ${PARAM}. These parameters are replaced
with actual values at run time. For example, the USER\_NAME parameter in the
following line of code is replaced with the name of the case worker who is assigned the quick
task:<p class="p1"><span class="s1">Hello ${USER\_NAME}</span></p>The
following parameters are supported:

Parameter
Runtime value

CASE\_LINK
The URL link to the case that contains the quick task.

CASE\_NAME
The name of the case.

DUE\_DATE
The date that the quick task is due, if any. The date is formatted by using the locale of the
originating user.

DUE\_DATE\_DISPLAY
Returns "show" if a due date is specified for the quick task or "none" if no due date is
specified.You can use this parameter to show or hide the HTML element that displays the due date.
You must specify this parameter by using the "display" setting of a style
attribute:
<div style="display: ${DUE\_DATE\_DISPLAY};">

HTML\_DIR
Returns the direction of the language of the email as either ltr (left to right) or rtl
(right to left).Case management recognizes languages such as Arabic (ar) and Hebrew (he) as right
to left.

HTML\_LANG
The language code that appears in the HTML header.

ORIGINATOR\_NAME
The name of the user who assigned the quick task to the case worker.

SOLUTION\_NAME
The name of the solution, which contains this case.

TASK\_NAME
The name of the quick task.

USER\_NAME
The display name of the user, as configured in the LDAP, to whom the quick task is
assigned.