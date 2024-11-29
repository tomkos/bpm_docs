# Installing workflow projects to an offline server by calling REST APIs

Containers: 
You can call REST APIs to export versions of workflow projects and then install
them to any workflow server. It does not require an online connection.

## Before you begin

## Procedure

Complete the following steps:

1. Construct a BPMCSRFToken parameter for the Business Automation Studio server and offline workflow
server by using POST/system/login to obtain it. Each subsequent API call requires
this header, for example: 
curl -X POST -H "${ACCESS\_TOKEN\_HEADER}" -H 'Content-Type: application/json' -H 'Accept: 
application/json' -d '{"refresh\_groups": true, "requested\_lifetime": 7200}'
'https://zen-front-door-hostname/instance\_prefix/ops/system/login'

The URL might be, for
example:https://cpd-cp4ba.apps.cp4ba-ca.55baw.p1.openshiftapps.com/baw-bawins1/ops/system/login
You
get a response such as
this:
{"expiration":7200,"csrf\_token":"eyJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2NDI2MTA2NjcsInN1YiI6ImNwNGFkbWluIn0.8742sRV3CTHN\_fY45W-29\_CrqeuOqRlFWPFItCKnodI"}The
response has a csrf\_token value that you can set as the parameter value. For
example,the variable $CSRF\_TOKEN\_HEADER is set to BPMCSRFToken:
<csrf\_token\_value> for the respective server.
2. On the Business Automation Studio
server, create the installation package by using POST
/std/bpm/containers/{container}/versions/{version}/offline\_package. Ensure that you are
using the ACCESS\_TOKEN\_HEADER and CSRF\_TOKEN\_HEADER for the Business Automation Studio server, for example: 
curl -X POST -H "$ACCESS\_TOKEN\_HEADER" -H "$CSRF\_TOKEN\_HEADER" -H 'Content-Type: 
application/json' -H 'Accept: application/json' 
'https://zen-front-door-hostname/instance\_prefix/ops/std/bpm/containers/PA1/versions/1/offline\_package?server=OffLn1'

You get a response such as this:
{"description":"Your request to create and
install an offline package from the specified snapshot on the specified server was submitted. You
can check the progress of the operation by calling the returned
url.","url":"https://zen-front-door-hostname/instance\_prefix/ops/system/queue/7?key=8b09658ae4fdb42ccfe33a20122265f4"}
3. Check the status by using the URL that was returned in the previous step with
GET /system/queue/{id}, for example: 
curl -X GET -H "$ACCESS\_TOKEN\_HEADER" -H "$CSRF\_TOKEN\_HEADER" -H 'Accept: 
application/json' 
'https://zen-front-door-hostname/instance\_prefix/ops/system/queue/7?key=8b09658ae4fdb42ccfe33a20122265f4'

You get a response such as
this:
{"state":"success","result":{"container":"PA1","server":"OffLn1","version":"SN03"},"last\_modified":"2022-01-18T22:11:25.367Z"}
4. Export the installation package by using GET
/std/bpm/containers/{container}/versions/{version}/install\_package, for example: 

curl -X GET -H "$ACCESS\_TOKEN\_HEADER" -H "$CSRF\_TOKEN\_HEADER" -H 'Accept: 
application/octet-stream' 
'https://zen-front-door-hostname/instance\_prefix/ops/std/bpm/containers/PA1/versions/1/install\_package?server=OffLn1' 
-o /c/MyExportPkg.zip

Note the location and name of the file that you exported.
5. On the offline workflow server, install the application version that you exported by
using POST /std/bpm/containers/install. Ensure that you are using the
ACCESS\_TOKEN\_HEADER and CSRF\_TOKEN\_HEADER for the offline server, for example: 
curl -X POST -H "$ACCESS\_TOKEN\_HEADER" -H "$CSRF\_TOKEN\_HEADER" -H 'Content-Type: 
multipart/form-data' -H 'Accept: application/json' -F 'install\_file=@C:\MyFiles\PA1 - 1.zip' 
{"type":"formData"}' 
'https://zen-front-door-hostname/instance\_prefix/ops/std/bpm/containers/install?inactive=false&caseOverwrite=false'

You get a response such as this:
{"description":"Your request to import the
specified file was submitted. You can check the progress of the import in the system log or by
calling the returned
url.","url":"https://zen-front-door-hostname/instance\_prefix/ops/system/queue/9?key=d2772760f7bd30006e877164ba8a6ee9"}
6. As described in step 5, you can check the status by using the URL in the response, for
example: 
curl -X GET -H "$ACCESS\_TOKEN\_HEADER" -H "$CSRF\_TOKEN\_HEADER" -H 'Accept: 
application/json' 
'https://zen-front-door-hostname/instance\_prefix/ops/system/queue/9?key=d2772760f7bd30006e877164ba8a6ee9'

You get a response such as
this:
{"state":"success","result":{"details":""},"last\_modified":"2022-01-19T14:46:16.979Z"}Your
project is now installed on the offline server.