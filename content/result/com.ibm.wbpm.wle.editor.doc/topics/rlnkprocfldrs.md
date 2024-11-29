# Linked process folders

## Linked process folders at development time

You might implement an activity in your process as a linked process. This linked process has a
root process folder, which is automatically added to the Folders pane (that
itself resides within the Folders tab) under a Linked Process
Folders structure. The name of the root linked process folder is the name of the linked
process. Suppose that your process has an activity that is implemented by a linked process. The
linked process is named Credit Card Assessment. Then, you see a Linked Process
Folders structure in your Folders pane. Under Linked
Process Folders is a folder that is named Credit Card Assessment. You see only the root
linked process folder. You do not see any sub folders beneath the linked process root folder.

When you select a linked process folder, a Linked Process Folder Details
section opens. The Place under drop-down list places the linked process
folder under a folder in the parent Root Process Folder structure. This
placement can be helpful for the organization of all your folders. For example, a Credit Card
Assessment linked process folder might be best placed under a root process folder that is named
Credit Card Charges Under Investigation. You can place a linked process folder only under a workflow
managed folder.

The Name field states the name of the linked process folder. By default,
the name is the linked process folder name. However, you can use a JavaScript expression to specify
the name dynamically. You can use variables in the expression. Enclose literal values in quotations.
Pressing Ctrl+Space can help you create a JavaScript expression. Suppose that you
wanted to rename Credit Card Assessment because you prefer a different name. You can create the new
name, for example, "New York Credit Card Assessment", in this field.

- If you want all invocations of the linked process to share the same folder, use a folder name
expression, such as "Credit Card Assessment"
- If you want all invocations of the linked process to share the same folder on a day, use a
folder name expression that uses the current date, such as "Credit Card Assessments of " +
new Date().getFullYear() + "-" + (new Date().getMonth () + 1) + "-" + new
Date().getDate()
- If you want each invocation of a linked process to have its own folder, create a local variable
that acts as counter with a type Integer. Use the local variable in the folder name expression, such
as "Credit Card Assessment (" + (tw.local.counter ++) + ")"

## Linked process folders at run time

At run time, your users see the linked process folder in the Documents
section when the linked process is invoked.

For example, your process might have two folders under the Root Process
Folder structure. One folder is named Credit Card Charges Outstanding and it refers to a
folder on an Enterprise Content Management system. The other folder is named Credit Card Charges
Under Investigation. It is a workflow managed folder. An activity in your process is implemented
with a linked process called Credit Card Assessment. You placed Credit Card Assessment under Credit
Cards Under Investigation. Under the Credit Card Charges Under Investigation folder, you selected
all the check boxes so your users can use folders and documents. When the process instance starts,
your users see the Credit Card Charges Outstanding and Credit Card Charges Under Investigation
folders. When the activity with the linked process runs, your users see another folder: Credit Card
Assessment.

Suppose that you renamed the Credit Card Assessment linked process folder to New York Credit Card
Assessment. Your users see the folder as New York Credit Card Assessment. When you rename a linked
process folder, your users see the new name.

Suppose that you placed the Credit Card Assessment linked process folder under the Credit Cards
Under Investigation folder. When the activity with the linked process runs, your users see the
Credit Card Assessment folder under the Credit Cards Under Investigation folder. Therefore, folder
placement determines where users see the folder at run time.