# Configuring the list of documents for the Content List widget

## Procedure

To configure the Content List widget:

1. Click the Edit Settings icon.
2. Click the Setting tab.
3 Select the method for populating the Content List widget: Option Description Property list The Content List widget is to retrieve documents by using the list of document IDs that are contained in the payload of the Display documents event. You must create a custom widget or use the Script Adapter widget to provide the property list to the Content list widget. Wire the event that is published by this widget to the Display documents event that is handled by the Content List widget. Stored search The Content List widget is to retrieve documents by running the specifiedstored search. To specify the stored search: To obtain the version series ID in IBM® ContentNavigator : You can also create a custom widget or use the Script Adapter widget tospecify the stored search dynamically at run time. To do so, you configure the custom widget orScript Adapter widget to provide the version series ID and version of the stored search. You thenwire the widget to the Search with stored search event that is handled by the Content List widget.This wire overrides the value that is configured for the Content List widget in Case Builder .

| Option        | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|---------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Property list | The Content List widget is to retrieve documents by using the list of                     document IDs that are contained in the payload of the Display documents event.                       You must create a custom widget or use the Script Adapter widget to provide                       the property list to the Content list widget. Wire the event that is published                       by this widget to the Display documents event that is handled by the Content                       List widget.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Stored search | The Content List widget is to retrieve documents by running the specified stored search. To specify the stored search: Select the version of the stored search that you want to run. Enter the version series ID of the stored search. You can obtain the identifier by viewing the system properties for the search.   To obtain the version series ID in IBM® Content Navigator: Click the Open Search View icon and then select your target object store. Open the folder that contains the stored search file. Right-click the file and click Link > View Link. Select and copy the portion of the URL that contains the version series ID. In the URL, vsid=" indicates the start of the version series ID.For example, to select a version series ID, select only the highlighted portion of the following URL:http://server\_name:port/navigator/bookmark.jsp ?desktop=Desktop Name&repositoryid="repository\_ID&repositoryType=p8 &docid="StoredSearchsearch\_id&mimeType=application%2Fx-filenet-search &template\_name=StoredSearch&version=released &vsid="%7B F0525657-0000-C622-ADC9-F1CEAD28F92C %7DTip: Do not include the %7B prefix or %7D suffix when you copy the ID.     You can also create a custom widget or use the Script Adapter widget to specify the stored search dynamically at run time. To do so, you configure the custom widget or Script Adapter widget to provide the version series ID and version of the stored search. You then wire the widget to the Search with stored search event that is handled by the Content List widget. This wire overrides the value that is configured for the Content List widget in Case Builder. |