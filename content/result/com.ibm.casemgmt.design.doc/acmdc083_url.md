# Opening pages using URLs

## About this task

By using a URL, you can open a solution page or the task details page that was created in
Case Builder in the respective
section of the Pages tab. For work items that use a workflow process, the URL
can open the process task details adapter page.

- Opening a specific solution page
- Opening a FileNet P8 process task page
- Opening a workflow process task page

## Opening a specific solution page

You can create a URL that opens a specific solution page after you log in to Case Client.

### About this task

The URL can open a solution page that was created in Case Builder in the Solution
Pages section of the Pages tab. The URL can open only a static
solution page that can be assigned to a role. The URL cannot open a dynamic solution page, such as a
page that was created in the Case Details Pages section of the
Pages tab.

```
http://server\_name:port\_number/navigator/?desktop=baw&feature=Cases&tos=TOS03\_ccp00010&solution=solution\_prefix&page=page\_ID&pageType=staticPage
```

### Procedure

To create a URL that opens a specific solution page:

1. Determine the base URL of a solution by clicking the Test link in
Case Builder. To find the
Test link, hover the cursor over the solution on the Manage
Solutions page.

For example, the base URL of a solution with a prefix of ABC123 has the
following
format:http://MyServer:Port/navigator/?desktop=baw&feature=Cases&tos=TOS03\_ccp00010&solution=ABC123
2. Add the following page information to the base URL:
&page=page\_ID&pageType=staticPage

To find the page ID, open the solution in Case Builder. The page ID is displayed in
the Unique Identifier box in the Solution Pages
section of the Pages tab.

For example, if you want a solution page with the MyWork page ID to open
when users log in to Case Client,
use the following URL:
http://MyServer:Port/navigator/?desktop=baw&feature=Cases&tos=TOS03\_ccp00010&solution=ABC123&page=MyWork&pageType=staticPage

## Opening a FileNet P8 process task page

You can create a URL that opens a specific FileNet P8 process task page after you log in
to Case Client.

### About this task

The URL can open a FileNet P8 task details page that was created in Case Builder in the Task Details
Pages section of Pages tab.

```
http://server\_name:port\_number/navigator/?desktop=baw&feature=Cases&tos=TOS03\_ccp00010&solution=solution\_prefix&queueName=queue\_Name&wobNum=wob\_Num
```

## Opening a workflow process task page

You can create a URL that opens a details adapter page for a workflow process task after
you log in to Case Client.

### About this task

The URL can open a specific details adapter page that was created in Case Builder in the Task Details
Pages section of Pages tab and configured for an activity with a
workflow process.

```
http://server\_name:port\_number/navigator/?desktop=baw&feature=Cases&tos=TOS03\_ccp00010&solution=solution\_prefix&taskId=task\_Id
```