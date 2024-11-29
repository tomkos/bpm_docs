# REST API groups and counters

| Property   | Description                                                            |
|------------|------------------------------------------------------------------------|
| GET        | REST API that requests a representation of the specified resource.     |
| DELETE     | REST API that deletes a specified resource.                            |
| POST       | REST API that submits data to be processed to the identified resource. |
| PUT        | REST API that uploads a representation of the specified resource.      |

| Property                 | Counter Type   | Description                                                                |
|--------------------------|----------------|----------------------------------------------------------------------------|
| Cases                    | Event          | Manually create a case instance of a case type.                            |
| Cases                    | Duration       | Manually create a case instance of a case type.                            |
| Case Instance            | Event          | Retrieve, update, or split a case instance.                                |
| Case Instance            | Duration       | Retrieve, update, or split a case instance.                                |
| Case Type                | Event          | Get the information about a case type.                                     |
| Case Type                | Duration       | Get the information about a case type.                                     |
| Case Comments            | Event          | Return or create comments of a specific type for a case instance.          |
| Case Comments            | Duration       | Return or create comments of a specific type for a case instance.          |
| Case History             | Event          | Return a filtered case history of a case instance.                         |
| Case History             | Duration       | Return a filtered case history of a case instance.                         |
| Case Tasks               | Event          | Lists activity instances of a case instance.                               |
| Case Tasks               | Duration       | Lists activity instances of a case instance.                               |
| Case Task Type           | Event          | Get the information about a case type.                                     |
| Case Task Type           | Duration       | Get the information about a case type.                                     |
| Case Status              | Event          | Return the status of a case instance.                                      |
| Case Status              | Duration       | Return the status of a case instance.                                      |
| Related Cases            | Event          | Return all of the related cases (of any type) of a case instance.          |
| Related Cases            | Duration       | Return all of the related cases (of any type) of a case instance.          |
| Solution Deployment      | Event          | Starts asynchronous solution deployment or retrieves solution information. |
| Solution Deployment      | Duration       | Starts asynchronous solution deployment or retrieves solution information. |
| Solution                 | Event          | Copy a solution in the design object store.                                |
| Solution                 | Duration       | Copy a solution in the design object store.                                |
| Discretionary Task Types | Event          | Return a list of the discretionary activities for a case worker.           |
| Discretionary Task Types | Duration       | Return a list of the discretionary activities for a case worker.           |
| Document Class           | Event          | Return the information of a document class.                                |
| Document Class           | Duration       | Return the information of a document class.                                |
| Document Classes         | Event          | Return the list of document classes in the target object store.            |
| Document Classes         | Duration       | Return the list of document classes in the target object store.            |
| Task Instance            | Event          | Change the state of an instance of an activity.                            |
| Task Instance            | Duration       | Change the state of an instance of an activity.                            |