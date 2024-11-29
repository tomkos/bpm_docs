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

## Class CaseRelationship

- java.lang.Object
    - com.ibm.casemgmt.api.CaseRelationship

- public final class CaseRelationship
extends java.lang.Object
Represents a relationship between two cases. Instances of CaseRelationship
 are obtained by calling the fetchRelatedCases() method
 on a Case instance.

ID status:
ID review by David Newhall

- ========== METHOD SUMMARY ===========
    - Method Summary All Methods Instance Methods Concrete Methods Modifier and Type Method and Description java.lang.String getCategoryName () Returns the relationship category name of this relationship. java.lang.String getDescription () Returns a textual description of the case relationship. Case getHeadCase () Returns an instance of Case that represents the head of the relationship. com.filenet.api.util.Id getRelationshipId () Returns the ID of this relationship. RelationshipType getRelationshipType () Returns the relationship type of this relationship. Case getTailCase () Returns an instance of Case that represents the tail of the relationship.

### Method Summary

| Modifier and Type       | Method and Description                                                                  |
|-------------------------|-----------------------------------------------------------------------------------------|
| java.lang.String        | getCategoryName() Returns the relationship category name of this relationship.          |
| java.lang.String        | getDescription() Returns a textual description of the case relationship.                |
| Case                    | getHeadCase() Returns an instance of Case that represents the head of the relationship. |
| com.filenet.api.util.Id | getRelationshipId() Returns the ID of this relationship.                                |
| RelationshipType        | getRelationshipType() Returns the relationship type of this relationship.               |
| Case                    | getTailCase() Returns an instance of Case that represents the tail of the relationship. |

- Methods inherited from class java.lang.Object
equals, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait