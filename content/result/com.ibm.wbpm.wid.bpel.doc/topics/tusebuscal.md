<!-- image -->

# Working with business calendars

## About this task

The following topics provide conceptual and reference information about, and step-by-step instructions for, working with business calendars in IBM Integration
Designer:

- Business calendars

In IBM Integration Designer, time-based computations are often simplistic and involve a start time and end time. Business calendars are used to model noncontiguous time intervals (intervals that do not proceed in a sequential manner) and allow these intervals to be further composed into a single semantically meaningful interval as opposed to simply using elapsed time for date and time computations. For example, a business calendar defining Regular Working Hours may refer to non-overtime regular working hours of Monday to Friday, 9:00 a.m. to 5:00 p.m. and exclude weekends. Business calendars are created using the New Business Calendar wizard in IBM Integration Designer. Business calendars can also be authored in and imported from IBM WebSphere Business Modeler where they are referred to as timetables (TT).
- Setting the business calendar type

Business calendar types, such as a Gregorian calendar or Hijri (Islamic) calendar, provide an environment for your business calendar functions. Business calendar types are set on the Preferences page.
- Creating business calendars

Business calendars are created using the IBM Integration Designer New Business Calendar wizard.
- Working with timetables (IBM WebSphere Business Modeler)

Business calendars are referred to as timetables (TT) in IBM WebSphere Business Modeler. The business calendar artifacts are exported to a PI (Project Interchange) file which is then imported by IBM Integration Designer.
- Business calendars and human tasks

After a business calendar has been created using the business calendar editor it can be used in a human task.
- Business calendars and BPEL processes

After a business calendar has been created using the business calendar editor it can be used in a BPEL process.
- Business calendar types

The business calendar schema is flexible enough to allow multiple ways of creating calendars.  In the flat model, all of the metadata is in one calendar file. In the hierarchical model, you can build small calendars that are complete on their own and then build a top level calendar that references other calendars. When authoring business calendars in IBM Integration Designer you do not need to explicitly decide whether the calendars must be flat or hierarchical. If all the intervals are in a single calendar, it will be flat and if the calendar includes or excludes other calendars then the calendar will be hierarchical.
- Deploying business calendars to IBM Workflow Server

After a business calendar has been created in IBM Integration Designer, it can be deployed to IBM Workflow Server as part of the deployment of the business module that contains it.
- Considerations when working with business calendars

There are a number of useful tips to consider when working with business calendars in IBM Integration Designer.