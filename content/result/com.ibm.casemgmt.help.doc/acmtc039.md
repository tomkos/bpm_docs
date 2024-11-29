# Some property values are empty for cases that are returned by a search that uses the
icm.util.SearchPayload class

```
payload.searchTemplate.setClasses([new ecm.model.SearchClass(
    caseType\_Identifier, caseType\_Identifier, "folder", true)]);
```

```
var solution = this.solution; // solution from the widget.
var params = {};
params.ObjectStore = solution.getTargetOS().id;

var criterion = new ecm.model.SearchCriterion({"id":
    "ICM\_strField", "name": "ICM\_strField", "selectedOperator": 
    "EQUAL", "dataType": "xs:string", "defaultValue" : "1234", 
    "value": "1234", "values": ["1234"]});
params.criterions = [criterion];

// params.ceQuery = "SELECT t.[FolderName], t.[LastModifier],
    t.[DateLastModified], t.[CmAcmCaseTypeFolder], 
    t.[CmAcmCaseState], t.[CmAcmCaseIdentifier], t.[DateCreated],
    t.[Creator], t.[Id], t.[ContainerType], t.[LockToken], 
    t.[LockTimeout],  t.[ClassDescription], t.[DateLastModified],
    t.[FolderName] FROM [CmAcmCaseFolder] t WHERE 
        ((((t.[CmAcmCaseIdentifier] LIKE '%%' or 
        t.[CmAcmParentSolution] =  
        Object({201323A3-271B-48CC-9C0D-7D0B20B1822C})) and 
        t.[CmAcmCaseState] > 1) )) ORDER BY 
        t.[CmAcmCaseIdentifier]";

params.CaseType = "ICM\_CaseType1";
params.solution = solution;

var searchPayload = new icm.util.SearchPayload();
searchPayload.setModel(params);

var self=this;
searchPayload.getSearchPayload(dojo.hitch(self, function(payload) {
    payload.searchTemplate.setClasses([new ecm.model.SearchClass("ICM\_CaseType1",
    "ICM\_CaseType1", "folder", true)]); 
    self.onBroadcastEvent("icm.SearchCases", payload);
}));
```