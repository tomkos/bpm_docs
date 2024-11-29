# Working with document attachments

## Using the addDocuments() method

```
var myMap = new tw.object.Map();
var hide = false;
var user = tw.system.user;
tw.system.currentProcessInstance.addDocument(
  TWDocument.Types.File,
  "name",
  "C:\\Projects\\WLE\\Images\\ibm.jpg",
  hide,
  user,
  myMap);
```