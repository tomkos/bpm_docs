# Using formatting with language localization resources in a heritage coach
(deprecated)

## About this task

## Procedure

1. Open a service that includes several variables, and click
the Variables tab.
2. Click the Link Localization button
and select the localization resource (in this example, Localized Formats)
that you want to link to the service variables as a resource bundle.
3. Create a heritage coach that includes an input text control named Time. Then bind the
formatting of the control to the localization resource bundle and localization key by typing
<#= tw.resource.LocalizedFormats.time #> into the
Format field.
4. Save your changes.
5. Optional: You can test the binding. To
test the binding, change the interface language to svenska in IBM® Process
Portal preferences.
Then run the BPD that contains the service and run the task fromProcess Portal. When
a you enter a 6-digit value such as 182400 into the
Time field, the value should be formatted to 18.24.00 ,
which conforms to the formatting that you specified.