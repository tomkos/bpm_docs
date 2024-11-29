# Integrating with Box

## About this task

If you enable Box
collaboration, case workers can associate a case with a Box
folder so that internal and external users can exchange content. For example, a customer service
representative at an automobile insurance company receives a new claim request. The customer service
representative creates a Box collaboration folder for the
case, and invites the claimant to be a collaborator on the folder. The customer service
representative copies a claims form to the Box folder and then
assigns a task to the claimant to complete and return the claims form. The claimant receives an
email notification about the task, and clicks a link in the email to open the Box folder. The claimant downloads the form, completes the relevant
information, and uploads the completed form and the police report about the accident. The customer
service representative can then copy the completed form and the police report from the Box folder to the case folder.

If you configure Box as an external repository, case
workers can add Box documents as case documents and task
attachments. Case workers can also add local documents to a case or work item and save the documents
in Box.

By default, when case workers add Box documents to a case,
a reference to the latest version of the document in Box is
added to the case. If the document is deleted from Box, the
reference from the case becomes invalid. You can allow case workers to add a copy of the current
version of a document to the case management repository instead of referencing the document in
Box. The copy remains in the case even if the document is
deleted from Box. However, any changes that are made to the
document in Box are not reflected in the case. To allow case
workers to add a copy of a Box document to the current case,
enable the Box copy feature for the case management repository
in IBM Content
Navigator.

IBM Business Automation
Workflow uses the Box
share feature of IBM Content
Navigator to enable case workers to share case
documents and task attachments that are in an IBM
FileNet Content Manager or
IBM Content
Manager repository. When a case worker selects a document to
share, IBM Content
Navigator saves the document to Box and creates a link to the specific version of the document. If the
case worker later deletes the share, the document is removed from Box.

- Setting up Box collaboration

You can integrate with Box so case workers and external users can use Box to exchange documents.
- Setting up Box as an external repository and for sharing

You can set up Box as an external repository for IBM Business Automation Workflow. You can also use Box to share case documents or attachments with other users.