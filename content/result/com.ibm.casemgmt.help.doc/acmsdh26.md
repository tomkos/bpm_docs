# Adding attachments to an activity

## About this task

In Case Builder,
an attachment is the designated location where users who work in Case Client can attach documents.

For example, for the case worker to view the claim application document, a policy document, and
damage photographs, each of these document types must be added to the activity as an attachment. The
claim application document attachment and the damage photographs documents might be set to read and
write so that the case worker can update them, while the policy document attachment is set to read
only.

If you define a
precondition to start the activity when a new document is added to the repository, you can designate
that document as the Initiating Attachment as described in the following
steps. If an initiating document is specified, then the activity starts when that document is
received and the corresponding attachment field is automatically set to that document. If no
initiating attachment is specified, then the precondition will still start the activity, but the
precondition document value will not be set in the attachment field.

## Procedure

To add an attachment to an activity:

1. Click the Attachments button.
2. Click Add Attachment.
3. Enter a name and prompt for the attachment.
The
prompt is displayed in the Case Client to
provide a brief hint to the case worker about the document.
4. Click OK.
5. Optional: 
If a document precondition
is set, select the attachment from the Initiating Attachment dropdown
menu.
6. Click OK and then click Close.