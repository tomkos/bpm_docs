<!-- image -->

# Troubleshooting escalation emails

## About this task

## Procedure

- Check the SystemOut.log file for error
messages relating to people assignments or email addresses.
- If the SystemOut.log file does not
contain any relevant messages, enable the debug mode for the mail
session server. In the administrative console, click Resources > Mail > Mail sessions then HTMMailSession\_server,
and select the Enable debug mode check box.

When an escalation email is sent, debug information is
written to the SystemOut.log file.
- If you are using virtual member manager as the people directoryprovider and you are having problems with email addresses, enablethe Staff.Diagnosis custom property. When an escalation email is sent, additional informationabout the people assignment is written to the SystemOut.log file.
    1. In the administrative console, click Servers > Clusters > WebSphere application server clusters > cluster\_name,
then on the Configuration tab, in the Business Process Manager section, expand Business Process Choreographer, and click Human Task Manager.
    2. On the Configuration tab, under Additional
Properties, click Custom Properties > Staff.Diagnosis, and type on in
the Value field.
- Check if the Human Task Manager hold queue contains messages. If the hold queue contains messages, check the First FailureData Capture (FFDC) directory of your server for more informationabout the error.

1. In the administrative console, click Servers > Clusters > WebSphere application server clusters > cluster\_name,
then on the Configuration tab, in the Business Process Manager section, expand Business Process Choreographer, and click Human Task Manager.
2. In the Runtime tab, click Replay
Hold Queue. The messages in the hold
queue are shown in the Hold queue messages field.

If the hold queue contains messages, check the First Failure
Data Capture (FFDC) directory of your server for more information
about the error.

- Check the values of the custom properties for the numberof times an email is resent and the timeout for sending an email.

1. In the administrative console, click Servers > Clusters > WebSphere application server clusters > cluster\_name,
then on the Configuration tab, in the Business Process Manager section, expand Business Process Choreographer, and click Human Task Manager.
2. On the Configuration tab, in
the Additional Propertiessection, click Custom
Properties.
3. Check the values of the EscalationEmail.RetryTimeout and
the EscalationEmail.MaxRetries fields.

EscalationEmail.RetryTimeout
Specifies how long Human Task Manager waits until it resends an
email notification that failed. The default value for this field is 3600 s.
(one hour) If the retry fails, then the retry timeout is doubled dynamically
for every time the retry fails. By default, if the first retry fails,
another retry is made after two hours.
EscalationEmail.MaxRetries
Specifies the number of times Human Task Manager tries to resend
an email notification that failed. The default value for this field
is 4 retries. If the value of this field is set to 0,
a failed email notification is not resent. If all of the retries fail,
then a message is put into the hold queue. You can see the messages
in the hold queue in the administrative console in the Runtime tab
for Human Task Manager. If you replay the messages, this is equivalent
to sending the email for the first time.