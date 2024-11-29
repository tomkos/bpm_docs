# Starting a process by calling an Business Automation Workflow REST
API

## Before you begin

- You know the model name and container acronym of the process that
you want to start.
- Users of the application must be authenticated users and authorized
to start an instance of the process.

## Procedure

1. Call the processes REST API and include
the model name and container acronym in the call. For
example, if you want to start an instance of the Order Management
process that belongs to the process app with the acronym ORDMAN1,
you can use the following REST API call:POST /bpm/processes?model=OrderManagement&container=ORDMAN1
2. Optional: Pass the business data that the process
requires to start as input parameters in a JSON object in the request
body of the call. For example, if the Order Management
process requires an order number and customer name to start, you can
pass the following JSON object: ...
{
   "input":[
      {
         "name":"orderNumber",
         "data":"5"
       },
       {
          "name":"customerName",
          "data":{
             "firstName":"John",
             "lastName":"Doe"
          }
       }
   ]
}
3. If you want additional information about the new process
instance to be returned by the call, include the optional\_parts parameter
in the query.  You can return data, valid actions for the
new instance, or both.For example, if you want
to return both data and valid actions for the new instance of the
Order Management process, you can use the following call:POST /bpm/processes?model=OrderManagement&container=ORDMAN1&optional\_parts=data,actions

## Results

- A new instance of the process is started. Depending on the parametersthat you include in the REST call, a version of the instance is started:
    - If you include the version and branch\_name parameters or only
the version parameter, an instance of the specified version is started.
    - If you include neither the version nor branch\_name parameters or only a branch\_name parameter,
an instance of the tip snapshot of the specified or default branch is started on the playback
server, or an instance of the default snapshot is started on a workflow server.
- A new process instance object is returned. If you include the optional\_parts parameter
in the query, this information is also included in the returned process
instance object.