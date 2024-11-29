# Configuring the Form widget to use a form template (deprecated)

## Before you begin

Ensure that a form template is created and saved in the
target object store.

## Procedure

To configure the Form widget to use a form template:

1 Find the object ID or version series ID of the form template as described in the followingtable and copy it to your Windows clipboard or to a text file. A version series ID is a unique identification string of 32 hexadecimal characters enclosed bybrackets in the following format: {xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx}. For example, a versionseries ID might be {21484408-092B-4846-A0B8-40D459836147}. Option Description IBM ContentNavigator IBM Administration Console forContent Platform Engine To get the version series ID for a specific version of a form template:

| Option                                                 | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|--------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| IBM Content Navigator                                  | Click the Open Browse View icon and then select your target object store. Open the folder that contains the template file. Right-click the file and clickLink > View Link. Select and copy the portion of the URL that contains the version series ID. In the URL, id=" indicates the start of the object ID, and vsid="  indicates the start of the version series ID. For example, to select a version series ID, select only the highlighted portion of the following URL:http://server\_name:port\_number/ navigator/bookmark.jsp?desktop=icm &repositoryId=repository\_ID& repositoryType=p8&docid=WebFormTemplate %2C%7B6EE7D4D4-928A-4CC5-8CF4-A47EC57362DE%7D %2C%7B80AB1D57-0000-CE19-9B87-209C58077101%7D& mimeType=application%2Fvnd.xfdl.design &template\_name=WebFormTemplate&version=released &vsId=%7B 80AB1D57-0000-C818-8A54 -797121485D2A %7D Tip: Do not include the %7B prefix or %7D suffix when you copy the ID. |
| IBM Administration Console for Content Platform Engine | To get the version series ID for a specific version of a form template: In the Object Stores directory, open the folder that contains the template file. Open the template file Click the Properties tab. In the property list, find the Version series property. Open the property and copy the Version series value.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |

2. In Case Builder,
open the page that contains the Form widget in Page Designer and click
the Edit Settings icon on the Form widget.
3. Select Form template from the Open the form
                        by using list.
4. In the Version menu, select the
version of the template that you want to use.
If you select Current or Released,
the next field requires the version series ID of the template. If
you select Specific, the next field requires
the specific object ID of the template.
5. In the Version ID field or the Version series
      ID field, paste the ID that you copied in step 1.
6. Save and deploy the solution.