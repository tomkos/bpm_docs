# Controlling usage of advanced properties of Business Objects for inbound Web Services

Traditional:  The
enable-advanced-parameter-properties-for-wsdl only has an effect when the target
environment is Traditional. For backward compatibility, the default value is
false. In any other target environment, advanced parameter properties for WSDL are
always enabled. Unless you have strong backward compatibility requirements for existing web
services, you should change the value of this property to true. If you change the
configuration property to true, you can still achieve backward compatibility by
adjusting the advanced parameter properties of business objects that are used by these web services.
However, caution is required when setting the value to true because it will affect
all inbound web services.

Containers:  Advanced parameter properties for WSDL
are always enabled and the enable-advanced-parameter-properties-for-wsdl
configuration property is ignored.

- Business object advanced properties
- Using web services for inter-process application communication

The advanced properties for business objects let you customize the XML representation of business
objects. Those properties are used to define the XML schemas for business objects in the WSDL of
inbound Web Services.

This configuration property is a server-wide setting that is applied dynamically at run-time for
the generation of inbound Web Service WSDL.

If its value is set to true, all advanced properties of the business objects are
taken into account. This is the recommended value that is to be specified in the
100Custom.xml file. You should only use the value false if you
rely on backward compatibility. Note that changing the value results in WSDL changes of all your
inbound Web Services, and thus the respective clients must be changed.

Currently the default value of this configuration property is set to false only
for backward compatibility. If set to false, not all advanced parameter properties
are considered when a web service interface is generated, for example, lists are wrapped in a
specific wrapper type.

For information about the advanced properties of business objects, see Business object advanced properties.