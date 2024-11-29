<!-- image -->

# Configuring logging properties for business objects

## About this task

To enable logging and set the output properties for a log, use the
following procedure.

## Procedure

1. In the navigation pane of the administrative console, click Servers > Server Types  > WebSphere application servers.
2. Click the name of the server that you want to work with.
3. Under Troubleshooting, click Loging and
tracing.
4. Click Change log detail levels.
5 Specify when you want the change to take effect:
    - For a static change to the configuration, click the Configuration
tab.
    - For a dynamic change to the configuration, click the Runtime
tab.
6 Expand the list, and then click the names of the public packages (described in Table 1 ) whose logging level you want to modify. Table 1. Logging specification descriptions Logging specification Usage BOChangeSummary Enable this log specification in the following circumstances: BOCopy Enable this log specification if you are using the BOCopy API in a businessapplication and you notice that the copied object does not match the original object. BOCore Enable this log specification for any issues related to initialization ofBusiness Object framework, loading of Business Object services, or schema loading . BODataObject Enable this log specification if you use the BODataObject API to access dataobject aspects of a business object (such as the change summary, event summary, and business graph).Also enable this log specification when you are using the BOLAZY parsing mode and youfind issues related to retrieving, modifying, or unsetting the data on the business object. BOEquality Enable this log specification if you find issues when using the BOEquality APIto determine if two business objects are equal. BOFactory Enable this log specification if you find issues when creating businessobjects using the BOFactory API. BOImpl Enable this log specification for issues related to other Business Objectframework implementation classes. BOInstanceValidator Enable this log specification for issues related to business object instancevalidation. BOType Enable this log specification for issues that arise when using the BOType APIto create types. BOTypeMetadata Enable this log specification for issues related to transforming an annotationstring to a data object (or vice-versa) using the BOTypeMetadata API. BOXMLSerializer or BOXMLSerializerXMLTrace Enable these log specifications for any issues related to serialization ordeserialization of business objects. Enabling BOXMLSerializerXMLTrace will print the XML documentbeing read or written in the log file. For any other issues, enable the BOCore log specification. Note: You can enable multiple logdetails for issues spanning multiple areas.

| Logging specification                      | Usage                                                                                                                                                                                                                                                                                                                                                               |
|--------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| BOChangeSummary                            | Enable this log specification in the following circumstances:  When changes are not logged in a business graph even though you have change summary enabled  You are using the BOChangeSummary API                                                                                                                                                                   |
| BOCopy                                     | Enable this log specification if you are using the BOCopy API in a business application and you notice that the copied object does not match the original object.                                                                                                                                                                                                   |
| BOCore                                     | Enable this log specification for any issues related to initialization of Business Object framework, loading of Business Object services, or schema loading.                                                                                                                                                                                                        |
| BODataObject                               | Enable this log specification if you use the BODataObject API to access data object aspects of a business object (such as the change summary, event summary, and business graph). Also enable this log specification when you are using the BOLAZY parsing mode and you find issues related to retrieving, modifying, or unsetting the data on the business object. |
| BOEquality                                 | Enable this log specification if you find issues when using the BOEquality API to determine if two business objects are equal.                                                                                                                                                                                                                                      |
| BOFactory                                  | Enable this log specification if you find issues when creating business objects using the BOFactory API.                                                                                                                                                                                                                                                            |
| BOImpl                                     | Enable this log specification for issues related to other Business Object framework implementation classes.                                                                                                                                                                                                                                                         |
| BOInstanceValidator                        | Enable this log specification for issues related to business object instance validation.                                                                                                                                                                                                                                                                            |
| BOType                                     | Enable this log specification for issues that arise when using the BOType API to create types.                                                                                                                                                                                                                                                                      |
| BOTypeMetadata                             | Enable this log specification for issues related to transforming an annotation string to a data object (or vice-versa) using the BOTypeMetadata API.                                                                                                                                                                                                                |
| BOXMLSerializer or BOXMLSerializerXMLTrace | Enable these log specifications for any issues related to serialization or deserialization of business objects. Enabling BOXMLSerializerXMLTrace will print the XML document being read or written in the log file.                                                                                                                                                 |

7. Expand Message and Trace Levels, and then select the logging level (as
described in Table 2).

Table 2. Logging levels

Logging Level
Description

Fatal 
The task cannot continue or the component cannot function. 

Severe
The task cannot continue, but the component can still function. This logging
level also includes conditions that indicate an impending fatal error (that is, situations that
strongly suggest that resources are on the verge of being depleted). 

Warning
A potential error has occurred or a severe error is impending. This logging
level also includes conditions that indicate a progressive failure (for example, the potential
leaking of resources). 

Audit
A significant event has occurred that affects the server state or resources.

Info
The task is running. This logging level includes general information outlining
the overall progress of a task. 

Config
The status of a configuration is reported or a configuration change has
occurred.

Detail
The subtask is running. This logging level includes general information
detailing the progress of a subtask.

All
Superset of all the logging levels.
8. Click Apply.
9. Click OK.

## Results

- If you selected dynamic configuration, the log files immediately contain information about
business objects that are processed by the server.
- If you chose to static configuration, the log files will begin logging the same information
after you restart your server.

## What to do next

<!-- image -->