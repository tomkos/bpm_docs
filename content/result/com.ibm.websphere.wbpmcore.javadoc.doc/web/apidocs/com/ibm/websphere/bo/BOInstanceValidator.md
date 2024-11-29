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

## Interface BOInstanceValidator

- public interface BOInstanceValidator
The interface for BO Instance Validator service. This service provides apis to validate
 a BO instance.

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
COPYRIGHT
    - Method Summary

Methods 

Modifier and Type
Method and Description

boolean
validate(commonj.sdo.DataObject businessObject,
        java.util.List diagnostics)
Do a deep validation for a BO instance.

boolean
validate(commonj.sdo.DataObject businessObject,
        java.util.List diagnostics,
        java.util.Locale locale)
Do a deep validation for a BO instance.

boolean
validate(commonj.sdo.DataObject businessObject,
        java.util.List diagnostics,
        java.util.Locale locale,
        java.util.logging.Level logLevel)
Do a deep validation for a BO instance.

boolean
validateProperty(commonj.sdo.DataObject businessObject,
                java.lang.String propertyPath,
                java.util.List diagnostics)
Do a deep validation for a BO instance's property.

boolean
validateProperty(commonj.sdo.DataObject businessObject,
                java.lang.String propertyPath,
                java.util.List diagnostics,
                java.util.Locale locale)
Do a deep validation for a BO instance's property.

boolean
validatePropertyShallow(commonj.sdo.DataObject businessObject,
                       java.lang.String propertyPath,
                       java.util.List diagnostics)
Do a shallow validation for a BO instance's property.

boolean
validatePropertyShallow(commonj.sdo.DataObject businessObject,
                       java.lang.String propertyPath,
                       java.util.List diagnostics,
                       java.util.Locale locale)
Do a shallow validation for a BO instance's property.

boolean
validateShallow(commonj.sdo.DataObject businessObject,
               java.util.List diagnostics)
Do a shallow validation for a BO instance.

boolean
validateShallow(commonj.sdo.DataObject businessObject,
               java.util.List diagnostics,
               java.util.Locale locale)
Do a shallow validation for a BO instance.

- ============ FIELD DETAIL =========== ============ METHOD DETAIL ==========
    - Field Detail

### Field Detail

- COPYRIGHT
static final java.lang.String COPYRIGHT
See Also:Constant Field Values

- Method Detail

### Method Detail

    - validate
boolean validate(commonj.sdo.DataObject businessObject,
               java.util.List diagnostics,
               java.util.Locale locale)
Do a deep validation for a BO instance. If a BO had children BOs, this method would validate the whole BO tree.
 
 
 For example: there is a BO instance named customer. 

 List diagnostics; 

Parameters:businessObject: - The Business Object to be validateddiagnostics: - diagnostics a place to accumulate diagnostics; if it's null, no diagnostics should be producedlocale: - The locale in which to report the diagnostics
Returns:whether the business object is valid.
    - validate
boolean validate(commonj.sdo.DataObject businessObject,
               java.util.List diagnostics,
               java.util.Locale locale,
               java.util.logging.Level logLevel)
Do a deep validation for a BO instance. If a BO had children BOs, this method would validate the whole BO tree.
 It will also log any errors to the console log at the requrested logging level.
 
 
 For example: there is a BO instance named customer. 

 List diagnostics; 

Parameters:businessObject: - The Business Object to be validateddiagnostics: - diagnostics a place to accumulate diagnostics; if it's null, no diagnostics should be producedlocale: - The locale in which to report the diagnosticslogLevel: - The logging level at which to log the errors
Returns:whether the business object is valid.
    - validate
boolean validate(commonj.sdo.DataObject businessObject,
               java.util.List diagnostics)
Do a deep validation for a BO instance. If a BO had children BOs, this method would validate the whole BO tree.
 
 
 For example: there is a BO instance named customer. 

 List diagnostics; 

Parameters:businessObject: - The Business Object to be validateddiagnostics: - diagnostics a place to accumulate diagnostics; if it's null, no diagnostics should be produced
Returns:whether the business object is valid.
    - validateShallow
boolean validateShallow(commonj.sdo.DataObject businessObject,
                      java.util.List diagnostics,
                      java.util.Locale locale)
Do a shallow validation for a BO instance. Even if a BO had children BOs, this method would only validate the first level of the BO tree.
 
 
 For example: there is a BO instance named customer. 

 List diagnostics;

Parameters:businessObject: - The Business Object to be validateddiagnostics: - diagnostics a place to accumulate diagnostics; if it's null, no diagnostics should be producedlocale: - The locale in which to report the diagnostics
Returns:whether the business object is valid.
    - validateShallow
boolean validateShallow(commonj.sdo.DataObject businessObject,
                      java.util.List diagnostics)
Do a shallow validation for a BO instance. Even if a BO had children BOs, this method would only validate the first level of the BO tree.
 
 
 For example: there is a BO instance named customer. 

 List diagnostics;

Parameters:businessObject: - The Business Object to be validateddiagnostics: - diagnostics a place to accumulate diagnostics; if it's null, no diagnostics should be produced
Returns:whether the business object is valid.
    - validateProperty
boolean validateProperty(commonj.sdo.DataObject businessObject,
                       java.lang.String propertyPath,
                       java.util.List diagnostics,
                       java.util.Locale locale)
Do a deep validation for a BO instance's property.

Parameters:businessObject: - The Business Object to be validated.propertyPath: - The property path of the business object.diagnostics: - diagnostics a place to accumulate diagnostics; if it's null, no diagnostics should be producedlocale: - The locale in which to report the diagnostics
Returns:whether the business object is valid.
    - validateProperty
boolean validateProperty(commonj.sdo.DataObject businessObject,
                       java.lang.String propertyPath,
                       java.util.List diagnostics)
Do a deep validation for a BO instance's property.

Parameters:businessObject: - The Business Object to be validated.propertyPath: - The property path of the business object.diagnostics: - diagnostics a place to accumulate diagnostics; if it's null, no diagnostics should be produced
Returns:whether the business object is valid.
    - validatePropertyShallow
boolean validatePropertyShallow(commonj.sdo.DataObject businessObject,
                              java.lang.String propertyPath,
                              java.util.List diagnostics,
                              java.util.Locale locale)
Do a shallow validation for a BO instance's property. 

Parameters:businessObject: - The Business Object to be validated.propertyPath: - The property path of the business object.diagnostics: - diagnostics a place to accumulate diagnostics; if it's null, no diagnostics should be producedlocale: - The locale in which to report the diagnostics
Returns:whether the business object is valid.
    - validatePropertyShallow
boolean validatePropertyShallow(commonj.sdo.DataObject businessObject,
                              java.lang.String propertyPath,
                              java.util.List diagnostics)
Do a shallow validation for a BO instance's property. 

Parameters:businessObject: - The Business Object to be validated.propertyPath: - The property path of the business object.diagnostics: - diagnostics a place to accumulate diagnostics; if it's null, no diagnostics should be produced
Returns:whether the business object is valid.