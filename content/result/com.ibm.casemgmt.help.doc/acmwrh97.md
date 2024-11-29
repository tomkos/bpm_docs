# Case List widget

- The case identifier, which provides a link that the case worker
can click to open the case
- The ID of the case worker who last modified the case
- The date that the case was last modified
- The case type
- The case status
- The case stage

- Specify the default view for the list and whether case workers
can switch between views.
- Show the case health for each case in the list.
- Add a toolbar to the widget.
- Configure the pop-up menu for the widget.

## IBM Business Automation
Workflow pages
that include this widget by default

- Add Comment to Case
- Create Package
- Open Case
- Send Link to Case
- Show Link to Case

## Customized Content Platform Engine SQL
queries

The Case List widget search payload supports customized Content Platform Engine SQL queries.

For
example, you can construct the following Content Platform Engine query to search all cases
that were created by admin users (user names that include "admin"):

"SELECT
[this], t.[FolderName], t.[LastModifier], t.[DateLastModified], t.[CmAcmCaseTypeFolder],
t.[CmAcmCaseState], t.[CmAcmCaseIdentifier], t.[DateCreated], t.[Creator],
t.[Id], t.[ClassDescription] FROM [CmAcmCaseFolder] t WHERE (((t.[creator]
LIKE '%admin%' AND t.[CmAcmParentSolution] = Object({CF0CFF8C-CD8C-41D3-AC0A-1272E4F73991})
AND t.[CmAcmCaseState] > 0))) ORDER BY t.[CmAcmCaseIdentifier]";

Custom
Content Engine SQL queries must meet the following requirements:

- The SELECT statement must include the following properties: "FolderName",
"LastModifier", "DateLastModified", "CmAcmCaseTypeFolder", "CmAcmCaseState",
"CmAcmCaseIdentifier", "DateCreated", "Creator", "Id", "ContainerType",
"LockToken", "LockTimeout", "ClassDescription",
- The query must search against a Case class, either the CmAcmCaseFolder
class or its subclass.

To create the search payload object, you can use the icm.util.SearchPayload utility
class as shown in the following sample code:

```
//////////////////////////////////////////////////////////// 
// This is running in a script adapter widget 
var solution = this.getSolution(); 
var repositoryId = solution.getTargetOS().id; 
var solutionGUID = solution.solutionFolderId; 
console.log("solutionFolderId is:" + solutionGUID); 
var caseTypeName =""; 
var ceQuery = "SELECT t.[FolderName], t.[LastModifier], 
  t.[DateLastModified], t.[CmAcmCaseTypeFolder], 
  t.[CmAcmCaseState], t.[CmAcmCaseIdentifier], t.[DateCreated], 
  t.[Creator], t.[Id], t.[ClassDescription] FROM [CmAcmCaseFolder] 
  t WHERE (((t.[creator] LIKE '%admin%' AND t.[CmAcmParentSolution] 
  = Object(" + solutionGUID + ") AND t.[CmAcmCaseState] > 0))) ORDER 
  BY t.[CmAcmCaseIdentifier]"; 
console.log("ceQuery is:" + ceQuery); 

var params = {}; 
params.ObjectStore = repositoryId; 
params.ceQuery = ceQuery; 
params.CaseType = caseTypeName; 
params.solution = solution; 

var p = new icm.util.SearchPayload(); 
p.setModel(params); 
var payload = p.getSearchPayload(); 
console.log("Payload is: -----"); 
console.dir(payload); 

return payload; 
////////////////////////////////////////////////////////////
```

- Case List widget events

The Case List widget uses events to process the list of cases that are returned when a user searches for cases.