# Processing a user task by calling Business Automation Workflow REST
APIs

## Before you begin

## Procedure

1. Display a list of unclaimed tasks that the current user
is allowed to see.  Unclaimed tasks are those tasks in
the ready state:GET /bpm/user-tasks?states=readyTo
filter the tasks list to show only tasks for a specific process, include
the model name, for example, OrderManagement, in the query: GET /bpm/user-tasks?model=OrderManagement&states=ready 
Alternatively, you can display the tasks for a specific
process instance by including the process ID, for example 2072.3,
in the query:GET /bpm/user-tasks?process\_id=2072.3&states=ready
2. The user opens a task in the list to review the business
data. To display the business data, include the optional\_parts=data parameter
in the query. To ensure that the user is authorized to view and claim
the task, include the actions property in the optional\_parts parameter.
For example, if the user opens task 2078.3, you can use
the following REST API call to show the task details and return the
actions that the user can perform:GET /bpm/user-tasks/2078.3?optional\_parts=data,actions
3. The user claims the task. For example, if
the user claims task 2078.3, you can use the following REST API call:POST /bpm/user-tasks/2078.3/claim?optional\_parts=data 
The task is put into the claimed
state. The returned user-task instance object includes the user ID
of the task owner and the variables that are currently set.
4. The task owner provides the required information and completes
the task. The required data output variables for
the task are passed in a JSON object in the request body of the /complete call.
For example, the order processor might need to provide a confirmation
that the stock is available at a warehouse and the total cost of the
order. POST /bpm/user-tasks/2078.3/complete
...
{
   "output":[
      {
         "name":"inStock",
         "data":"Yes"
       }
       {
          "name":"Price",
          "data":"1000",
       }
       {
          "name":"warehouseAddress",
          "data":{
             "street":"Mystreet", 
             "houseNo":"12", 
             "postCode":"1234", 
             "city":"Mycity" 
            }
        }]
}

## Results

## What to do next

```
POST /user-tasks/{task\_id}/fail
```

An End error
event must be modeled in the service with a matching error code for the API to be invoked
successfully. The error data is a JSON representation of an object that can represent the error
itself or any other object. For example, to pass an instance of a BO object with a single variable
of String type in JSON format, you should use the following
format:

```
{
"code" : "CustomErrorCode",
"data" : "{\"errorString\":\"String for custom error code\"}"
}
```