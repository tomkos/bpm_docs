<!-- image -->

# Store-and-forward runtime validator

The runtime validator checks the following items. Validation rules verify that the values
supplied in the qualifier make sense in the context of the application, or that there are no
syntactic errors.

- A non-SCA export has a store-and-forward qualifier
- Exceptions are not unique in their hierarchy. For example, if two neighboring interfaces have
identical exception specifications, that is acceptable. However, if an interface has an exception
specified, and an operation under that interface specifies an identical exception, a warning is
logged.

- If the exception name is:
    - not found in the module classpath
    - not a subclass of java.lang.RuntimeException
    - a subclass of com.ibm.websphere.sca.ServiceBusinessException
- If the value for exceptionChain is not set to one of these four valid options:

- startFromTop
- startFromBottom
- OnlyTopLevelException
- OnlyLowestLevelException
- If the configuration name for each qualifier:

- is not defined. This value is required.
- is not named using alphanumeric characters or an underscore. Alphanumeric characters and
underscores are the only supported characters.
- is not unique across the module
- If the validator detects that the XML document does not conform to the XML schema
- If extraneous tags are found in the XML

If you encounter a runtime validation error related to the store-and-forward function, follow the
suggestions in the error message to resolve the error.