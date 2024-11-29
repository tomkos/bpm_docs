<!-- image -->

# Creating a business object from a source file

## Before you begin

## About this task

The external data wizard lets you create business objects
for your services based on applications available locally. Though
similar in use to the external service wizard, the external data wizard
does not require you to go through the steps of connecting to an EIS
system.

The external data wizard also lets you create a wrapper
business object from an existing business object. Creating a wrapper
business object is discussed at the end of this set of steps.

## Procedure

1 Right-click your module and from the menu, select New> External Data . The External Data windowopens. For the EMail, FTP or Flat File adapters, you can create awrapper business object from a business object. For the purpose ofthis example, under Languages , select COBOL(CICS Channel) . At the end or this set of steps, the otherchoice, creating a wrapper business object, is discussed. Notethat each language (C, COBOL or PL/I) has three choices: Click Next .

Note
that each language (C, COBOL or PL/I) has three choices:

    - A language which will have one output value at run time
    - A language with CICS® channel
support. Traditionally, CICS programs
have used communication areas (COMMAREAs) to exchange data. Channels
and containers provide an improved method for transferring data between
programs, in amounts that exceed the 32KB limit that applies to COMMAREAs.
A container is a named block of data that is used to pass information
between programs (it can be thought of as a named COMMAREA). Any number
of containers can be passed between programs through the use of a
channel.
    - A language with multiple outputs, which means at run time one
of the outputs will be selected to return a value.

Click Next.

2. The Business Object Mapping Details page
opens. Select New beside the Containers pane.
In the following page, browse to a COBOL file on your computer. Click Next.
3. The Select Data Structures page opens.
Platform and code page are already completed for you, but you can
change them. The platform and properties specified here must be those
of the target platform where the CICS transaction
is running (z/OS®, Windows, and so on). The defaults shown are
taken from the preferences set for the COBOL importer in the preferences
page. To see these preferences, from the menu select Window
> Preferences > Importer > COBOL.  Clicking Advanced reveals
other fields you can change such as the floating-point format. Click Find beside
the Data structures pane. The wizard returns the data structures in
the COBOL file. Select the one you want. Click Finish.
4. You are returned to the Business Object Mapping
Details page. Your selection is in the Containers pane.
You could continue adding more containers. Click Next.
5. The Generate Business Objects page
opens. You can choose to change or create a new module at this point.
The name of the generated business object will be the data structure
name if you do not change it. Specifying a folder is recommended since
otherwise all generated files will be in the root module folder, which
will make them difficult to manage. Generation style, which in this
case you will see if you select the container name, lets you choose
several options that can shorten the length of the generated file
names. A CICS channel name
and container name must be specified. Click Finish to
complete the generation of your business objects.

## What to do next

You would follow a similar path to create
a wrapper business object from an existing object.  A wrapper business
object provides more fields for information related to the particular
adapter you selected. Suppose we had created a business object called
DeptPersonnelInfo similar to the one described previously and then
selected FTP beneath the Adapters folder
to create a wrapper business object for a service using the FTP adapter.
Following a similar process, we would create the following DeptPersonnelInfoWrapper
business object. Notice the additional fields for FTP adapter-specific
information.

## Related concepts

- Pattern of accessing external services with adapters
- Developing services with adapters
- Simple adapter wizard
- Migrating applications using previous adapter levels

## Related tasks

- Configuring and using adapters

## Related reference

- J2C data bindings
- A closer look at business objects from data structures
- J2C imports and exports at run time
- Trade-offs when developing adapter imports and exports
- Considerations when using adapters
- Considerations when refactoring
- Contributing your own external service or data wizard plug-in
- Limitations for adapter imports and exports