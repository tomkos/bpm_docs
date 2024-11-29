<!-- image -->

# Preparing to deploy to a server

## Before you begin

## About this task

## Procedure

1. Locate the folder that contains
the components for the module you want to deploy. The
component folder should be named module-name with
a file in it named module.module,
the base module.
2. Verify that all components contained in the module are
in component subfolders beneath the module folder. For
ease of use, name the subfolder similar to module/component.
3. Verify that all files that comprise each component are
contained in the appropriate component subfolder and have a name similar
to component-file-name.component.
The component files contain the definitions for each individual
component within the module.
4. Verify that all other components and artifacts are in the
subfolders of the component that requires them. In this
step you ensure that any references to artifacts required by a component
are available. Names for components should not conflict with the names
the serviceDeploy command uses for staging modules.
See  Naming conventions
for staging modules.
5. Verify that a references file, module.references,
exists in the module folder of step 1. The references file defines the
references and the interfaces within the module.
6. Verify that a wires file, module.wires,
exists in the component folder. The wires file completes
the connections between the references and the interfaces within the
module.
7. Verify that a manifest file, module.manifest,
exists in the component folder. The manifest lists the
module and all the components that comprise the module. It also contains
a class path statement so that the serviceDeploy command
can locate any other modules needed by the module.
8. Create a compressed file or a JAR file of the module as
input to the serviceDeploy command that you will
use to prepare the module for deployment to the production server.

## Example folder structure for MyValue module before
 deployment

The following example illustrates the directory
structure for the module MyValueModule, which is made up of the components
MyValue, CustomerInfo, and StockQuote.

```
MyValueModule
   MyValueModule.manifest
   MyValueModule.references
   MyValueModule.wiring
   MyValueClient.jsp
process/myvalue
   MyValue.component
   MyValue.java
   MyValueImpl.java
service/customerinfo
   CustomerInfo.component
   CustomerInfo.java
   Customer.java
   CustomerInfoImpl.java
service/stockquote
   StockQuote.component
   StockQuote.java
   StockQuoteAsynch.java
   StockQuoteCallback.java
   StockQuoteImpl.java
```

## What to do next