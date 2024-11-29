<!-- image -->

# Registering an XPath function JAR file with IBM Integration
Designer

## Before you begin

## Procedure

1. In Integration Designer,
go to Window > Preferences > Business Integration > BPEL Process
Editor.
2 Under Custom XPath extension functions, enter one or morepaths where your XPath extension function files are located. Thepaths that you enter are then included in the classpath environmentvariable of your operating system.If a path contains white space,you must enclose the path in double quotation marks (""). If Integration Designer cannotfind your XPath extension functions at run time, verify that the pathsthat you entered are correct. The following examplesshow the format for entering multiple paths:

If a path contains white space,
you must enclose the path in double quotation marks (""). If Integration Designer cannot
find your XPath extension functions at run time, verify that the paths
that you entered are correct.

    - D:\xpath;"C:\new xpath"
    - etc/home/xpath:"etc/home/new
xpath"
3. Click OK.

## Results

## What to do next