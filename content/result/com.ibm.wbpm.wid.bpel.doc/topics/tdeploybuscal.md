<!-- image -->

# Deploying business calendars to IBM Workflow
Server

## About this task

The business calendar service is a runtime service that does date/time
calculations on behalf of components that are clients of this service. For
example if a component needs to determine that a particular time falls into
an interval covered by a calendar, it would simply invoke the service with
the calendar name and the time stamp.

Business modules are deployed either from IBM Integration
Designer using the Unit Test Environment (UTE) or from the administrative console (using an ear exported by IBM Integration
Designer or created by serviceDeploy). For information regarding these processes, refer to the related link below.