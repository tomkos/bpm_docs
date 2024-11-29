<!-- image -->

# Overview

- A flat file
- WebSphere® Adapter for Flat Files
- Inbound processing
- File splitting
- Record delimiters
- Splitting by size
- Custom data bindings
- Outbound processing
- Overview of the application in this tutorial.

## What is a flat file?

```
<?xml version="1.0" encoding="UTF-8"?>
<customer>
	<title>Mr</title>
	<name>Smith</name>
	<city>Ottawa</city>
	<state>ON</state>
</customer>
<customer>
	<title>Mrs</title>
	<name>Jones</name>
	<city>Winnipeg</city>
	<state>MB</state>
</customer>
```

```
Mr,Smith,Ottawa,ON
Mrs,Jones,Winnipeg,MB
```

## What is the WebSphere Adapter for Flat
Files?

Suppose you have an external system that outputs sets of files to a directory. An example might
be an order processing system that produces text files containing order information to be processed
in a batch mode during off-peak hours. You would use the WebSphere Adapter for Flat Files along with IBM Integration
Designer to help you create and manage these files.

Your application can use the adapter for flat files to create and manage files or to monitor a
directory and read files from this directory. You have two options when creating a service
associated with adapter for flat files, both of which are documented in the documentation of the
product:

- Simple external service wizard: With this wizard, you create a service by specifying the
directories that the WebSphere Adapter for Flat Files
reads from and writes to and formats of the data in those directories. Then the wizard generates the
service. For many users, this quick and easy way of creating a service is sufficient. We will use
this approach in this tutorial.
- Advanced service wizard: With this wizard, you create a service by a longer, more comprehensive
process. Some users may find this more detailed approach more suitable. You begin by specifying the
type of adapter you will require and then specify the directories that the WebSphere Adapter for Flat Files reads from and writes to, and the format
of the data in those directories. Then you continue using further pages with fields in an advanced
section to add more control over the generated service.

Inbound processing is the mode of operation in which the WebSphere Adapter for Flat Files monitors the file system, reads new
files, and sends the data to an operation in an application.

Outbound processing is the mode of operation in which the WebSphere Adapter for Flat Files receives requests (from a component of
an application) to perform a file operation and, when applicable, returns the results to the caller.
Example operations include creating a file, writing to a file, or checking if a specific file
exists.

During inbound processing, the adapter for flat files listens for events that are produced by an
event directory (for example, a file is placed in the event directory). An event is a record
of what changes have occurred in the event directory. The directory that the adapter for flat files
monitors for new files is called the event directory.

The following diagram shows the four steps that occur during inbound processing:

<!-- image -->

1. An external system outputs its files to the event directory.
2. The adapter for flat files polls for files from the event directory and converts the data from
those files into events. The adapter can be configured to poll for only certain types of files, or
for files created during a certain time period.
3. Events are temporarily placed in an event store. This is either a database or an in-memory
representation of the event table. If you use a database, events will not be lost before your
application can process them if the server goes down after an event is created, for example. This is
referred to as assured delivery. Using in-memory tables, the event processing will be faster
but you lose the event recovery capability.
4. The adapter for flat files retrieves the events from the event store and passes each event in
the form of a business object through an exported inbound interface, which the external service
wizard created.

This method of retrieving data, that is, passing data in the form of a business object, is called
non-pass-through or Data Transformation Framework (DTF), and it operates on structured data.

If the application does not know the format of the data files, you can configure the adapter for
flat files to run in pass-through mode, operating on unstructured data. In that case, it
would not transform an event into a business object.

## File splitting

You use file splitting when the files you want to retrieve are large or they each contain more
than one record. You can split files into smaller chunks based on a delimiter or on a fixed-size
value, which allows parts of the file to be processed in parallel. Each chunk is considered a
separate event and is individually sent to an operation in an application through the exported
inbound interface.

## Record delimiter

Typically, input is stored as a single record per file. However, when the input file contains
more than one record, you often separate the records in the file with a delimiter, which can be any
text string and is usually a combination of characters followed by \r\n (platform dependent new line
character). The adapter can both read and write files that contain a delimiter.

Using our XML format and CSV format examples discussed earlier, we have the string #### followed
by a new line as the delimiter in the XML file shown in the following example. We have a new line as
the delimiter in the CSV file.

```
<?xml version="1.0" encoding="UTF-8"?>
<customer>
	<title>Mr</title>
	<name>Smith</name>
	<city>Ottawa</city>
	<state>ON</state>
</customer>
####
<customer>
	<title>Mrs</title>
	<name>Jones</name>
	<city>Winnipeg</city>
	<state>MB</state>
</customer>
####
```

```
Mr,Smith,Ottawa,ON
Mrs,Jones,Winnipeg,MB
```

## Split by size

The split-by-size feature is similar to splitting by delimiter, because you use it to divide a
file into smaller chunks and transfer them, one by one, to the operation in the application. Use
this feature with unstructured data in a pass-through scenario because the unstructured data is not
going to be put into business objects. You specify the split criterion in the adapter as a number of
bytes. The adapter reads the file as chunks (events) of that byte size. Each chunk will be the size
defined by split criteria, except the last one, which might be smaller.

## Custom data binding

Data in flat files can come in many different formats, such as the previously discussed XML and
CSV formats. Others formats include name and value pairs, tab-separated, and fixed-width formats. A
data handler maps from the format in the data files to the attributes of a business
object.

Using the adapter for flat files default data binding, you can convert files to and from XML
format. In other formats, you have to use custom data handlers that define the mapping between the
file format and a business object. To implement a custom data handler, create a Java™ class that converts the data for the specific format and enter this class
in the external service wizard when you configure the adapter.

For more information about creating a custom data handler, refer to the IBM Integration
Designer documentation.

## Outbound processing

To write or modify files, the application uses the operations defined in the outbound interface,
which you create using the external service wizard. You can create both unstructured data (in
pass-through mode) and structured data (in non-pass-through mode) using the different operation
types:

- Create - Stores data to a new file or creates an empty file.
- Append - Appends data to an existing file. A new file is created if one did not already
exist.
- Overwrite - Overwrites an existing file with a new data.
- Delete - Deletes an existing file.
- Exists - Checks if a specific file exists.
- List - Lists files in a directory.
- Retrieve - Reads content from a file.

Only the create and append operations are used with the simple external service wizard.

## Overview of the application in this tutorial

Imagine that you want to create an application that monitors a certain directory in a file system
so that you can collect customer record information. When a file is created, the adapter uses the
specified file splitter delimiter to split the content of the file into business objects. The export
is called for each business object. The export is wired to a mediation flow which invokes the
adapter to write the records into their own file in an output directory.

This scenario is shown in the following diagram:

<!-- image -->

When files that contain customer records are in the inbound events directory, the resource
adapter retrieves them, creates a customer business object, and calls an export in the module, which
initiates the mediation flow. The mediation flow invokes a file service which generates a new file
name with its name based on the number of existing files.

## Related information

- Build it Yourself
- Run the sample
- Import