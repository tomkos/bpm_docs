- Overview
- Package
- Class
- Tree
- Deprecated
- Index
- Help

- Prev Class
- Next Class

- Frames
- No Frames

- All Classes

- Summary:
- Nested |
- Field |
- Constr |
- Method

- Detail:
- Field |
- Constr |
- Method

## Class Comment

- java.lang.Object
    - com.ibm.casemgmt.api.Comment

- public final class Comment
extends java.lang.Object
Represents a comment applied to a case. Instances of Comment
 are obtained by calling methods on a Case instance. For example, 
 the addCaseComment method creates a new comment that applies to 
 a case in general, and returns a new Comment instance. The method
 fetchCaseComments returns a list of Comment instances
 representing the current comments on a case.
 
 Comments in a case management system are stored in the Content Engine
 repository as annotation objects.

ID status:
ID review by David Newhall

- ========== METHOD SUMMARY ===========
    - Method Summary All Methods Instance Methods Concrete Methods Modifier and Type Method and Description CommentContext getContext () Returns the context of the comment. java.lang.String getCreator () Returns the creator of the comment, which is stored in the Creator property of the annotation object. java.util.Date getDateCreated () Returns the date that the comment was created, which is stored in the DateCreated property of the annotation object. java.lang.String getDocumentTitle () Returns the document title at the time the comment was created if this comment represents a comment for a document object, and returns null otherwise. com.filenet.api.util.Id getId () Returns the ID of the comment, which is stored in the Id property of the annotation object. com.filenet.api.util.Id getItemId () Returns the ID of the associated object if this comment is associated with a document, task or work item. java.lang.String getText () Returns the text of the comment, which is stored in the CmAcmCommentText property of the annotation object. java.lang.String getWorkClassName () Returns the work class name if this comment is associated with a work item. java.lang.String getWorkResponse () Returns the work response if this comment is associated with a work item. java.lang.String getWorkStepName () Returns the work step name if this comment is associated with a work item. java.lang.String getWorkWorkflowNumber () Returns the workflow number if this comment is associated with a work item.

### Method Summary

| Modifier and Type       | Method and Description                                                                                                                                                       |
|-------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CommentContext          | getContext() Returns the context of the comment.                                                                                                                             |
| java.lang.String        | getCreator() Returns the creator of the comment, which is stored in the Creator property  of the annotation object.                                                          |
| java.util.Date          | getDateCreated() Returns the date that the comment was created, which is stored in the DateCreated property of the   annotation object.                                      |
| java.lang.String        | getDocumentTitle() Returns the document title at the time the comment was created if   this comment represents a comment for a document object, and returns  null otherwise. |
| com.filenet.api.util.Id | getId() Returns the ID of the comment, which is stored in the Id property of the annotation  object.                                                                         |
| com.filenet.api.util.Id | getItemId() Returns the ID of the associated object if this comment is associated with  a document, task or work item.                                                       |
| java.lang.String        | getText() Returns the text of the comment, which is stored in the CmAcmCommentText  property of the annotation object.                                                       |
| java.lang.String        | getWorkClassName() Returns the work class name if this comment is associated with a work item.                                                                               |
| java.lang.String        | getWorkResponse() Returns the work response if this comment is associated with a work item.                                                                                  |
| java.lang.String        | getWorkStepName() Returns the work step name if this comment is associated with a work item.                                                                                 |
| java.lang.String        | getWorkWorkflowNumber() Returns the workflow number if this comment is associated with a work item.                                                                          |

- Methods inherited from class java.lang.Object
equals, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait