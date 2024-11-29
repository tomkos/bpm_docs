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

## Class CloseCase

- java.lang.Object
    - com.ibm.casemgmt.api.deletecase.CloseCase

- public class CloseCase
extends java.lang.Object
Represents the CloseCase class. This class has the methods to delete the case artifacts.
     To instantiate the class, use the constructor CloseCase by passing the parameters in JSON.

After instantiating the class, call the  method validateParams to validate the parameters.

After getting a successful string result from the validateParams method, 
         call the deleteCase method to delete the case artifacts

ID status:
ID review by Bibhudatta Mohapatra

- ======== CONSTRUCTOR SUMMARY ======== ========== METHOD SUMMARY ===========
    - Constructor Summary

Constructors 

Constructor and Description

CloseCase(org.apache.commons.json.JSONObject jobj)
Constructor CloseCase to create instance of the class CloseCase
    - Method Summary All Methods Instance Methods Concrete Methods Modifier and Type Method and Description java.lang.String deleteCase () Method to delete the case artifacts. java.lang.String validateParams () Method to validate the parameters inside the JSON that returns a string that indicates if the validation was successful or not.

### Method Summary

| Modifier and Type   | Method and Description                                                                                                                            |
|---------------------|---------------------------------------------------------------------------------------------------------------------------------------------------|
| java.lang.String    | deleteCase() Method to delete the case artifacts.                                                                                                 |
| java.lang.String    | validateParams() Method to validate the parameters inside the JSON that  returns a string that indicates if the validation was successful or not. |

- Methods inherited from class java.lang.Object
equals, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait