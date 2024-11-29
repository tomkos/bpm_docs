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

## Class DocumentType

- java.lang.Object
    - com.ibm.casemgmt.api.DocumentType

- public final class DocumentType
extends java.lang.Object
Represents a document type deployed as part of a deployed solution in the
 Case Management system. An instance of DocumentType can be obtained
 only in the list returned from the getDocumentTypes method on
 DeployedSolution.
 
 A DocumentType represents a document class in the Content Engine object
 store or an item type in a CM8 system.

ID status:
ID review by David Newhall

- ========== METHOD SUMMARY ===========
    - Method Summary All Methods Instance Methods Concrete Methods Modifier and Type Method and Description java.lang.String getDescription () Returns the descriptive text of the document type or item type. java.lang.String getDisplayName () Returns the display name of the document type or item type. java.lang.String getItemTypeId () Returns the item type ID if this DocumentType represents an item type, and returns null otherwise. java.lang.String getSymbolicName () Returns the symbolic name of the document type. boolean hasInstanceCreationRights () Indicates if the current authenticated user has the rights to create documents that are of this document type. boolean isHidden () Returns the hidden flag set on the document type or item type.

### Method Summary

| Modifier and Type   | Method and Description                                                                                                                      |
|---------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| java.lang.String    | getDescription() Returns the descriptive text of the document type or item type.                                                            |
| java.lang.String    | getDisplayName() Returns the display name of the document type or item type.                                                                |
| java.lang.String    | getItemTypeId() Returns the item type ID if this DocumentType represents an item type,  and returns null otherwise.                         |
| java.lang.String    | getSymbolicName() Returns the symbolic name of the document type.                                                                           |
| boolean             | hasInstanceCreationRights() Indicates if the current authenticated user has the rights to create  documents that are of this document type. |
| boolean             | isHidden() Returns the hidden flag set on the document type or item type.                                                                   |

- Methods inherited from class java.lang.Object
equals, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait