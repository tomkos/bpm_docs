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

## Class HealthAlert

- java.lang.Object
    - com.ibm.casemgmt.api.HealthAlert

- public class HealthAlert
extends java.lang.Object
Represents a JSON object that is stored in the CmAcmHealthDetails property of the Health Condition object. Instances of HealthAlert
 are obtained by calling the getHealthDetails method on a HealthCondition instance, 
 which returns a list of HealthAlert objects.
 
 The HealthAlert object is used for message localization purpose.

- ========== METHOD SUMMARY ===========
    - Method Summary All Methods Instance Methods Concrete Methods Modifier and Type Method and Description void clearParameters () Clears the memory that was allocated for the parameters. java.lang.String getDefaultMessage () Returns the default message. java.lang.String getLocalizedMessage (java.util.Locale inputLocale) Returns the localized message based on an input locale java.util.List<java.lang.String> getParameters () Returns a list of the String parameters for this alert. java.lang.String getResourceKey () Returns the resource key.

### Method Summary

| Modifier and Type                | Method and Description                                                                                   |
|----------------------------------|----------------------------------------------------------------------------------------------------------|
| void                             | clearParameters() Clears the memory that was allocated for the parameters.                               |
| java.lang.String                 | getDefaultMessage() Returns the default message.                                                         |
| java.lang.String                 | getLocalizedMessage(java.util.Locale inputLocale) Returns the localized message based on an input locale |
| java.util.List<java.lang.String> | getParameters() Returns a list of the String parameters for this alert.                                  |
| java.lang.String                 | getResourceKey() Returns the resource key.                                                               |

- Methods inherited from class java.lang.Object
equals, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait