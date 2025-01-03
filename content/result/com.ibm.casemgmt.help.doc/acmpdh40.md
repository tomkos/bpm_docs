# addCommentToCurrentDocument operation

The document title that is used on the comment is the short name of the released version of the
document.

If a case type is configured so that users can attach documents from repositories other than the
case management target object store, you can use this operation to add a comment to a document from
an external repository. To add a comment to an attachment from an external repository, an external
document reference object must be filed in the case along with the information that is used to
reference the external document.

| Parameter    | Type       | Description                                                                                                                                                  |
|--------------|------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| caseId       | String     | The identifier of the case. You must set the expression for the caseID parameter to the F\_CaseFolder business object field in the Expression Builder window. |
| doc          | Attachment | The document where you want to add a comment.                                                                                                                |
| comment      | String     | The comment that you want to add.                                                                                                                            |
| return\_value | String     | The GUID of the new comment.                                                                                                                                 |