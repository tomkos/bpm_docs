- Overview
- Package
- Class
- Tree
- Deprecated
- Index
- Help

- Prev Class
- Next Class

- Frames
- No Frames

- All Classes

- Summary:
- Nested |
- Field |
- Constr |
- Method

- Detail:
- Field |
- Constr |
- Method

## Class ALFactory

- java.lang.Object
    - com.ibm.wsspi.al.ALFactory

- public class ALFactory
extends java.lang.Object
Factory to create/remove AdminAL

- =========== FIELD SUMMARY =========== ======== CONSTRUCTOR SUMMARY ======== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
COPYRIGHT
Copyright
    - Constructor Summary

Constructors 

Constructor and Description

ALFactory()
    - Method Summary Methods Modifier and Type Method and Description static ArtifactLoader create (org.eclipse.jst.j2ee.commonarchivecore.internal.Archive earFile) Create an ArtifactLoader instance. static ArtifactLoader create (org.eclipse.jst.j2ee.commonarchivecore.internal.Archive earFile, com.ibm.websphere.management.application.Scheduler scheduler) Create a ArtifactLoader instance, for use from application install or sync tasks. static ArtifactLoader create (java.lang.String path) Create an ArtifactLoader based on a file directory. static void remove (org.eclipse.jst.j2ee.commonarchivecore.internal.Archive earFile) Remove the instance AL created based on an Archive (ear file). static void remove (java.lang.String path) Remove an ArtifactLoader instance that is created by ALFactory.create(String path);

### Method Summary

| Modifier and Type     | Method and Description                                                                                                                                                                                                        |
|-----------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| static ArtifactLoader | create(org.eclipse.jst.j2ee.commonarchivecore.internal.Archive earFile) Create an ArtifactLoader instance.                                                                                                                    |
| static ArtifactLoader | create(org.eclipse.jst.j2ee.commonarchivecore.internal.Archive earFile,       com.ibm.websphere.management.application.Scheduler scheduler) Create a ArtifactLoader instance, for use from application install or sync tasks. |
| static ArtifactLoader | create(java.lang.String path) Create an ArtifactLoader based on a file directory.                                                                                                                                             |
| static void           | remove(org.eclipse.jst.j2ee.commonarchivecore.internal.Archive earFile) Remove the instance AL created based on an Archive (ear file).                                                                                        |
| static void           | remove(java.lang.String path) Remove an ArtifactLoader instance that is created by ALFactory.create(String path);                                                                                                             |

- Methods inherited from class java.lang.Object
clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait