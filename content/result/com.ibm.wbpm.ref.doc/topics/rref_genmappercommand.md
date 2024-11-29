# genMapper command-line utility

The genMapper command generates a component that bridges an SCA reference to a
Java™
interface creating files that you import into IBM® Integration
Designer. After importing to IBM Integration
Designer, you wire the Web Services Description
reference and the Java interface to the generated component.

The input can contain a Java class, a stateless session bean, or a Java interface.

If the input is a Java class, the class can contain only one interface and the interface cannot
extend other interfaces.

## Syntax

```
genMapper
-javaOutput java\_output\_dir
-scdlOutput sca\_output\_dir
-name java\_class\_file
```

## Parameters

## Examples

```
genMapper -javaOutput c:\customer\src -scdlOutput c:\customer -name com.ibm.mj.Customer
```

```
Customermapper.component
Customermapper.wsdl
```

```
Customermapper.java
```

Copy the files from
both generated directories to the directory of any module that requires the bridge component. You
can then either import that bridge component into IBM Integration
Designer and wire the reference and interface to the
bridge component or use the serviceDeploy command to create an enterprise archive
(EAR) file to deploy to the server.