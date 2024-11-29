<!-- image -->

# Pre-packaged Email, FTP and Flat File data bindings

The following data bindings are available for the Email, FTP and
Flat Files adapters.

| Data binding                   | Description                                                                                                                                                                                                                                                                                     |
|--------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| EmailSimpleDataBinding         | This data binding serializes the business object to a simple email data type. It cannot be used with a data handler. It is used for simple email alerts.                                                                                                                                        |
| EmailFixedStructureDataBinding | This data binding serializes the business object to an Email adapter user defined type. It can be used with a data handler. This data binding corresponds to a business object structure that you define. Email attachments must be in the same order as the attributes in the business object. |
| EmailWrapperDataBinding        | This data binding serializes the business object to a generic email data type or generic email with business graph data type. It can optionally be used with a data handler. It is used with generic email and generic email with business graph data types.                                    |
| FlatFileBaseDataBinding        | This data binding serializes the business object to the format expected by the Flat Files adapter. It is configurable with a data handler. It does not need to be configured for some uses such as a passthrough scenario.                                                                      |
| FTPFileBaseDataBinding         | This data binding serializes the business object to the format expected by the FTP adapter. It is configurable with a data handler. It does not need to be configured for some uses such as a passthrough scenario.                                                                             |
| WTX data binding               | This data binding lets you use WebSphere® Transformation Extender (WTX), a universal validation and transformation engine, to convert business objects to many data formats and vice versa.                                                                                                     |