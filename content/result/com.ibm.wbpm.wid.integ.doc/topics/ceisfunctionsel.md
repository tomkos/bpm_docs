<!-- image -->

# Pre-packaged Email, FTP and Flat File function selectors

The following function selectors are available for the Email,
FTP and Flat File adapters.

| Function selector            | Description                                                                                                                                                                                                          |
|------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| EmailFunctionSelector        | This function selector maps to the emitEmail method. It cannot be configured by a data handler.                                                                                                                      |
| EmbeddedNameFunctionSelector | This function selector is used by the FTP and Flat Files adapters. It must be configured by a data handler. The function selector serializes and deserializes the data to and from the object that maps to a method. |
| FilenameFunctionSelector     | This function selector is used by the FTP and Flat Files adapters. By default, it maps to the emitFTP or emitFlatFile methods. It can be configured by a data handler.                                               |