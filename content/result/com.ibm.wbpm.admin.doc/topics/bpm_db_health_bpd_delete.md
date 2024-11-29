# Deleting process instances

If you want to specify particular
process instance states, the states running, finished,
and stopped correspond to the states active, completed,
and failed in wsadmin and Process Inspector.

## Using the Process Admin Console and REST API call

1. Login to the Process Admin Console at
https://<BAW\_hostname:port>/ProcessAdmin.
2. Select the menu icon and select Process
Admin > Health Management.IBM Business Automation
Workflow Operations REST Interface
Swagger UI opens in a new browser tab.
3. Load the IBM Business Automation
Workflow
Operations REST Interface Swagger UI:
https://host:port/bpm/explorer/?url=https://host:port/ops/docs?tags=Health%20Management#/Health%20Management
4. Expand the System section, then expand the POST/system/login
section.
5. Click Try it
out > Execute.If the login is not successful, HTTP
error code is shown in the Server response section. Fix the error and repeat the
login.
If the login is successful, the HTTP response code is 201 and the
csrf\_token element is found at the Response body
section.{ "csrf\_token": "eyJhbGciOiJIUzI1NiJ9.eyJleHAiOjE....o0PoTvKdQxokI5XaZRMw", "expiration": 7200 }
6. Copy the csrf\_token and locate/expand DELETE
/std/bpm/processes API call in the Health Management section.
7. Click Try it out.
8. Copy the csrf\_token to the BPMCSRFToken parameter.
9. Specify values for the parameters. Required parameters are marked with a *.Important: To delete process instances that are in states other than finished and terminated,
you must specify the option force=true.
10. Click Execute.

## Using a wsadmin command

To delete process instances from the IBM Business Automation
Workflow database, see BPMProcessInstancesPurge command.

- Counting process instances

You can use the Process Admin Console or a REST API call to count the number of process instances that match specified criteria before you decide whether to delete them.