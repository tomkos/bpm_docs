# Getting and changing case information

## Cases and case folders

A case is represented as a case folder within the folder hierarchy in the target object store for
a deployed solution. A case is filed in folder hierarchy under the Cases folder
for its case type. A case folder contains the activities, history, and comments that are associated
with the case.

- yyyy: The four-digit year
- mm: The two-digit month
- dd: The two-digit day
- pppp: The four-digit parent folder number

```
/IBM Case Manager
  /Solution Deployments
    /<solution name 1>
      /Case Types        /<Case Type 1a folder>
          /Cases
            /yyyy
              /mm
                /dd
                  /pppp
                    /<case folder. Name = sequence number>
                    ... (more case instance folders)
        /<Case Type 1b folder>
          /Cases
            /yyyy
              /mm
                /dd
                  /pppp
                    /<case folder. Name = sequence number>
                    ... (more case types for solution 1)
    /<solution name 2>
      /Case Types
        /<Case Type 2a folder>
          /Cases
            /yyyy
              /mm
                /dd
                  /pppp
                    /<case folder. Name = sequence number>
                    ... 
        /<Case Type 2b folder>
          /Cases
            /yyyy
              /mm
                /dd
                  /pppp
                    /<case folder. Name = sequence number>
                    ... (more case types for solution 2)
    ... (more solutions)
```

- Cases resource

The cases resource represents the cases that are defined in your case management system. You can use this resource to create a case.
- Particular case instance resource

The particular case instance resource represents a case. You can use this resource to return or update the property values for a case.
- Deleting a particular case resource

You can use this resource and its POST method to delete a particular case resource.
- Status of particular case resource

The status of particular case resource represents status information about a case. You can use this resource to determine whether a case completed successfully.
- Related cases for a particular case resource

The related cases for a particular case resource represent the set of cases that are related to a specific case. You can use this resource to return a list of the related cases. For example, you can return a list of the cases that were created by splitting the current case.
- List of activity instances resource

The list of activity instances resource provides a list of all the activity instances that are running for a particular case instance.
- Create new activity resource

By using the create new activity resource, a case worker can add a user-created activity to a case. You can use the GET method that is defined for this resource to retrieve the launch step information for the selected user-created activity type. You can then use the POST method to add a new user-created activity of that type to the case.
- Particular activity instance resource

The particular activity instance resource represents an instance of an activity. You can use this resource to change the state of an activity, for example, from disabled to started.
- Case comments resource

The case comments resource represents the comments that are associated with a specific case. A case comment can be associated with the case or with a document, activity, or work item in the case. The format of the comment varies depending on the component with which it is associated. You can use this resource to retrieve comments for a case and to add a comment to a case.
- Case history resource

The case history resource represents the history for a specific case. You can use this resource to retrieve the entries that make up the case history. The case history shows information such as creation dates, comments, and such, about the case.
- Case stage

The Case stage API helps to retrieve all stages' information or current stage for a given case instance.
- List of case folder resources

The list of case folder resources provides a list of all the case folder and case documents in a case instance.
- Security manifest

 The saveSolutionSecurityManifest API allows you to save and apply Security manifest.