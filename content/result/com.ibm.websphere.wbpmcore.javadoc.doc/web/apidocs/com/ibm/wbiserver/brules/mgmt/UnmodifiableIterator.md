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

## Class UnmodifiableIterator<E>

- java.lang.Object
    - com.ibm.wbiserver.brules.mgmt.UnmodifiableIterator<E>

- Type Parameters:E - The type of object returned by the iterator.

All Implemented Interfaces:
java.util.Iterator<E>

public class UnmodifiableIterator<E>
extends java.lang.Object
implements java.util.Iterator<E>
This class implements an unmodifiable iterator based on another iterator.  The 
 remove method from the Iterator interface is not supported and
 will throw an UnsupportedOperationException if called.

- =========== FIELD SUMMARY =========== ======== CONSTRUCTOR SUMMARY ======== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
COPYRIGHT
    - Constructor Summary

Constructors 

Constructor and Description

UnmodifiableIterator(java.util.Iterator<E> iter)
Constructor for UnmodifiableIterator class.
    - Method Summary Methods Modifier and Type Method and Description boolean hasNext () Returns true if the iteration has more elements. E next () Returns the next element in the iteration. void remove () Unsupported method.

### Method Summary

| Modifier and Type   | Method and Description                                     |
|---------------------|------------------------------------------------------------|
| boolean             | hasNext() Returns true if the iteration has more elements. |
| E                   | next() Returns the next element in the iteration.          |
| void                | remove() Unsupported method.                               |

- Methods inherited from class java.lang.Object
clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait