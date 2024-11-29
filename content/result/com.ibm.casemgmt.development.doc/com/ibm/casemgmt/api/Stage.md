- Overview
- Package
- Class
- Tree
- Deprecated
- Index
- Help

- Prev Class
- Next Class

- Frames
- No Frames

- All Classes

- Summary:
- Nested |
- Field |
- Constr |
- Method

- Detail:
- Field |
- Constr |
- Method

## Class Stage

- java.lang.Object
    - com.ibm.casemgmt.api.Stage

- public final class Stage
extends java.lang.Object
Represents a case stage in IBM Case Manager. To obtain an instance of a Stage object, use the method fetchStages 
 from the Case object.
 
 New stages are first created by the IBM Case Manager event handler during case creation. If there is more than one stage,
 the stages are linked through a P8 task relationship object. Once created, the first stage is automatically started
 and its due date is calculated if the expected duration is given.
 
 After a Case instance is obtained, call other methods, such as the method completeCurrentStage that completes a stage, 
 or the method placeCurrentStageOnHold to place a stage on-hold. 
 
 A stage is started automatically by the IBM Case Manager event handler when either it is the first stage or the previous stage has completed.

- ========== METHOD SUMMARY ===========
    - Method Summary All Methods Instance Methods Concrete Methods Modifier and Type Method and Description java.util.Date getCompletedDate () Returns the completed date and time for a stage that is completed. java.lang.String getDescription () Returns the textual description of the stage. java.util.Date getDueDate () Returns the stage due date. int getDuration () Returns the stage duration. int getDurationTimeInHours (Stage stage) StageDurationType getDurationType () Returns the stage duration type. java.lang.String getName () Returns the display name of the stage. float getOverDueTime () Calculates the overdue on this stage if the stage is currently working or complete. int getRestartCount () Returns restart count for the stage. java.util.Date getStageEstimatedCompleteDate () Returns the estimated complete date and time for a stage that is not started yet. java.util.Date getStageEstimatedStartDate () Returns the estimated start date and time for a stage that is not started yet. java.util.Date getStartedDate () Returns start date and time for a stage that is currently working or on hold. StageStatus getStatus () Returns the status of the stage, for example whether it is working, completed, on hold, or waiting for a previous stage. java.lang.String getSymbolicName () Returns the stage symbolic name. float getTimeSpent () Calculates the total time spent on this stage if the stage is currently working or on hold.

### Method Summary

| Modifier and Type   | Method and Description                                                                                                               |
|---------------------|--------------------------------------------------------------------------------------------------------------------------------------|
| java.util.Date      | getCompletedDate() Returns the completed date and time for a stage that is completed.                                                |
| java.lang.String    | getDescription() Returns the textual description of the stage.                                                                       |
| java.util.Date      | getDueDate() Returns the stage due date.                                                                                             |
| int                 | getDuration() Returns the stage duration.                                                                                            |
| int                 | getDurationTimeInHours(Stage stage)                                                                                                  |
| StageDurationType   | getDurationType() Returns the stage duration type.                                                                                   |
| java.lang.String    | getName() Returns the display name of the stage.                                                                                     |
| float               | getOverDueTime() Calculates the overdue on this stage if the stage is currently working or complete.                                 |
| int                 | getRestartCount() Returns restart count for the stage.                                                                               |
| java.util.Date      | getStageEstimatedCompleteDate() Returns the estimated complete date and time for a stage that is not started yet.                    |
| java.util.Date      | getStageEstimatedStartDate() Returns the estimated start date and time for a stage that is not started yet.                          |
| java.util.Date      | getStartedDate() Returns start date and time for a stage that is currently working or on hold.                                       |
| StageStatus         | getStatus() Returns the status of the stage, for example whether it is working, completed, on hold, or waiting for a previous stage. |
| java.lang.String    | getSymbolicName() Returns the stage symbolic name.                                                                                   |
| float               | getTimeSpent() Calculates the total time spent on this stage if the stage is currently working or on hold.                           |

- Methods inherited from class java.lang.Object
equals, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait