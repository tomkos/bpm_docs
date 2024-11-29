# Creating business objects

## About this task

You can create a custom business object in the designer by using a base business object or by
defining a new complex structure.

When you create a business object in a process application, that object is available for all business processes and
services in the process application. If you want to share a custom business object acrossprocess
application, create or store the custom object
in a toolkit. Then, create a dependency on that toolkit from the process
application that requires the variable.

## Procedure

1. Open the designer.
2. In the library, beside Data click + and
select Business Object to create a business object. Alternately, you can
create a business object by clicking New when you create a
variable. The New Business Object window
opens.
3. In the Name field, type a name for the custom business object and
click Finish.

Remember: Names of business objects are case-sensitive.
4. Under Behavior, you see definition types.  

Simple type
Creates a new simple business object that is derived from one of Boolean, Date, Decimal,
Integer, Selection, String or Time. A simple type that is created with the business object editor
cannot be initialized before use with a business process or service unlike a complex type. If you do
initialize a simple type that uses the new keyword, then you receive a runtime error.

Complex type
Creates a new complex business object by specifying the parameters for the structure. Complex
structure types that contain primitive types must initialize the primitive types before use.

An example of initializing a primitive type before use is
tw.local.myListOfComplexTypes[0].name = "";.
5 Select a type from the Definition type list.
    - If you selected Simple type, select the type of your business object
and specify a validation if you want. For example, you might want to limit the number of characters
for a String type.Ad hoc activity runtime behavior affects some string properties. None
(unlimited in length) defaults to a maximum of 64 characters. You see a warning that states this
limit when you select this property. If your application requires a large string, use the Range
property and set a large maximum length. Fixed (always same length) becomes a maximum
length.
    - If you selected Complex type, add the parameters and a description of
each one, if you want. You can also order the parameters.
6. If the business object and its values must be accessible to other instances at run time,
select Shared Object.
7. To perform validation checks, calculations, or access checks on the shared business
object during save handling, select Save service and specify the heritage
service or service flow to use as a save service. 
For more information about save services, see Save services for shared business objects.
8. Click Save or Finish Editing.

- Shared business objects

You can ensure the integrity of data that is passed between process components at run time by using shared business objects. The data in a shared business object is always current because it is refreshed from the data store before it is used. If you use shared business objects, you can also control how data is passed and how changes are handled in running processes and services.
- Save services for shared business objects

Updates to shared business objects are saved either automatically when automatic synchronization is enabled for the process or service instance, or explicitly when the save method is called. Use save services to perform validation checks, calculations, or access checks on the shared business object during save handling. You can include error handling in a process or service to detect and process errors that occur during data validation.
- Business objects, attributes, and variables that are renamed (deprecated)

With time, applications change and business objects, their attributes, and variables might be renamed. However, many parts of a business process might reference or have a dependency on a business object, an attribute, or a variable. Renaming, therefore, can produce unexpected results. To rename a business object, an attribute or a variable and see the impact that renaming causes, use the rename function.
- Business object advanced properties

The advanced properties for business objects lets you customize the serialized XML representation of the business object. This XML representation is used by external systems when a business object is part of an exposed web service.