# Create new activity resource

- GET method for the create new activity resource

The GET method returns the launch step information for the specified activity type that is required to add a user-created activity to the case. The launch step information is passed to the POST method to start the user-created activity.
- POST method for the create new activity resource

The POST method adds a new user-created activity to a case by passing in the workflow launch step information that was returned by the preceding GET method.