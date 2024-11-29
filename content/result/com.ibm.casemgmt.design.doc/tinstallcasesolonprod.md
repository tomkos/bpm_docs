# Installing a case solution by using REST APIs

## Before you begin

1. In Workflow Center, click Case Solutions and then click the View
details icon of the case solution you want to install.
2. On the Snapshots tab, click the export link of the snapshot.
3. Select the IBM® Business Automation
Workflow Installation
Package (.zip) option and then click Export.

## Procedure

The following steps use the IBM BPM
Explorer ops to run the installation by using REST APIs, although you can use any REST client to run
the APIs:

1. Go to IBM BPM Explorer ops on
https://host\_name:port\_number/ops/explorer. The server address
must be the URL of Workflow Server.
2. Under System, run the POST /system/login REST API with the
login\_request parameter, using the example values.
For more information, see the REST API reference.
3. Click Try it out to run the REST API.
4 Under Container, run the POST /std/bpm/containers/install REST API withthese parameters:
    - BPMCSRFToken - The value returned from the /system/login
call.
    - install\_file - The .zip file you exported for your snapshot.
    - inactive - Deactivates the snapshot after you install it. This parameter is
false by default.
    - caseDosName - The name of the case design object store. You can get this
from your administrator.
    - caseProjectArea - The target environment or project area for case
artifacts. You can omit this value if the default project area is defined. You can get this from
your administrator.
    - caseOverwrite - Set this parameter to true.
5. Click Try it out to run the REST API.
6 To determine when the case solution has been installed, run the GET/std/bpm/containers/{container}/versions/{version} REST API with these parameters:

- BPMCSRFToken - The value returned from the /system/login call.
- container - The acronym for the case solution.
- version - The acronym for the snapshot being installed.
7. Click Try it out to run the REST API.

## Results