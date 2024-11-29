<!-- image -->

# Creating a data format transformation resource configuration

## Before you begin

```
MyDataHandler.bcfg
cfg:bindingConfiguration xmlns:cfg="http://www.ibm.com/xmlns/prod/websphere/bindingconfiguration/6.1.0" name="MyDataHandler" ...

NewDataHandler.bcfg
cfg:bindingConfiguration xmlns:cfg="http://www.ibm.com/xmlns/prod/websphere/bindingconfiguration/6.1.0" name="NewDataHandler" ...
```

## About this task

## Procedure

1. Right-click the module and from the menu select
New > Configure Binding
Resource. The Binding Resource Configuration window
opens. On the Select a Configuration Type page, select Data
transformation. Click Next.
2 By default, the existing data format transformations, thatis, the existing data format handlers, in the binding registry areshown. These prepackaged data handlers are described in Prepackaged data format handlers . You may alsoselect a custom data format transformation from your workspace onthe class path. Note that only classes on the class path with a namefollowing this pattern <class name>Properties areselectable. Selecting Show the deprecated data formattransformations adds previous transformations that havebeen deprecated. In this example, we chose the Delimited dataformat. Click Next . Notethat if you chose another popular format, the SOAP dataformat, and clicked Next you would have thefollowing selections on the next page.

You may also
select a custom data format transformation from your workspace on
the class path. Note that only classes on the class path with a name
following this pattern <class name>Properties are
selectable.

Selecting Show the deprecated data format
transformations adds previous transformations that have
been deprecated.

In this example, we chose the Delimited data
format. Click Next.

    - Propagate SOAP headers: Selecting this
option propagates the SOAP header information at run time
    - Construct the faultcode of SOAP Fault as QName format:
Selecting this option means your faults will use the qualified name
(QName) for a namespace; that is you intend to use the SOAP with Attachments
API for Java (SAAJ) 1.3 standard. If you do not select this option,
which is the default, then your faults will contain the unqualified
name of a namespace; that is, you intend to use the SOAP with Attachments
API for Java (SAAJ) 1.2 standard.
3. Once you have selected your data format transformation,
the wizard allows you to proceed to the Data Transformation
Properties page where you can add or modify properties
such as, in this case, the delimiter for the data. The
delimited format property fields are discussed in Delimited format properties. Other
format property fields are discussed in Data handler formats.
4. In the New Data Transformation Configuration page,
you can change or create a new module for the data format transformation,
add a folder to contain the generated files and name and describe
your configuration. Click Finish and the data
format transformation resource configuration is completed and shown
in the editor.
5. The data format handler configuration is completed and
shown in the editor along with the bindings it can be used with. It
also is listed in the navigation under Binding Resources. 
If you had chosen a SOAP data format then you will see the
options discussed earlier in the Properties view.

## What to do next