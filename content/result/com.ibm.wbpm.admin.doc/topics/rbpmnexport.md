# Exporting process applications to BPMN 2.0

- To export a project so that you can import it into another Workflow Center, use the export
(.twx) file format. This format includes all the details for your process. See
Importing and exporting projects.
- Process names must not include the colon (:) character.
- Process names must not include characters that are not supported in names on the operating
system.

The following table shows the mapping between workflow objects and their equivalent
elements in the BPMN 2.0 file format after export. If an object is not included in the table, the
object is not exported. All the elements include the name and the description text. The description
is included in a Documentation element.

| Workflow object                               | BPMN element                     | Comments                                                                                     |
|-----------------------------------------------|----------------------------------|----------------------------------------------------------------------------------------------|
| Process                                       | Process                          |                                                                                              |
| Activity with a Linked Process implementation | Call Activity                    | Refers to the called process.                                                                |
| Activity with a Decision Task implementation  | Business Rule Task               |                                                                                              |
| Activity with a System Task implementation    | Service Task                     |                                                                                              |
| Activity with a Script implementation         | Script Task                      |                                                                                              |
| Activity with a User Task implementation      | User Task                        |                                                                                              |
| Activity with a Subprocess implementation     | Subprocess                       | Contents are included.                                                                       |
| Activity with an Event Subprocess type        | Subprocess                       | Marked as triggered by an event. Contents are included.                                      |
| Activity with a None implementation           | Task                             |                                                                                              |
| Event Gateway                                 | Event-based Gateway              |                                                                                              |
| Exclusive Gateway                             | Exclusive Gateway                |                                                                                              |
| Inclusive Gateway                             | Inclusive Gateway                |                                                                                              |
| Parallel Gateway                              | Parallel Gateway                 |                                                                                              |
| Start Event                                   | Start Event                      |                                                                                              |
| Message Start Event                           | Message Start Event              |                                                                                              |
| Timer Start Event                             | Timer Start Event                |                                                                                              |
| Error Start Event                             | Error Start Event                | An Error element with an error code is also created if there is an error code for the event. |
| AdHoc Start Event                             | Start Event                      |                                                                                              |
| None End Event                                | End Event                        |                                                                                              |
| Error End Event                               | Error End Event                  | An Error element with an error code is also created if there is an error code for the event. |
| Message End Event                             | Message End Event                |                                                                                              |
| Terminate End Event                           | Terminate End Event              |                                                                                              |
| Message Intermediate Event (Receiving)        | Message Intermediate Catch Event |                                                                                              |
| Message Intermediate Event (Sending)          | Message Intermediate Throw Event |                                                                                              |
| Timer Intermediate Event                      | Timer Intermediate Catch Event   |                                                                                              |
| Tracking Intermediate Event                   | Intermediate Catch Event         |                                                                                              |
| Error Event that is attached to an Activity   | Error Boundary Event             | An Error element with an error code is also created if there is an error code for the event. |
| Message Event attached to an Activity         | Message Boundary Event           |                                                                                              |
| Timer Event that is attached to an Activity   | Timer Boundary Event             |                                                                                              |
| Sequence Flow                                 | Sequence Flow                    |                                                                                              |
| Note                                          | Text Annotation                  |                                                                                              |

## Related tasks

- Next steps after importing BPMN models

## Related reference

- Mapping BPMN 2.0 constructs to workflow objects after import