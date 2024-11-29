# Translating custom strings

## Before you begin

Deploy the solution before you translate the customized
string. When you deploy the solution, the nls/Resources.js file
is created or modified in the IBM® Business Automation
Workflow/Solutions/solution\_name folder
in the design object store or staging object store.

The recommended best practice is to treat all translated custom
string resources like other solution assets. Those assets should be
tested and maintained in a design object store in the development
environment first. Then, you move those assets to a production environment,
which means that all available translated custom string resources
are moved to the staging object store in the test environment. Finally,
you move the complete translated solution to a production environment,
which uses the design object store.

Although this procedure
takes longer for the translated strings to be available in a production
environment, it is the best way to  maintain the solution definition,
the generated default language resources, and any other manually translated
custom string resources.

## About this task

- Page titles
- Action labels and menu labels in widgets
- Title for the tabbed layout, title for the titled layout, custom
property label, and property hint in views.

## Procedure

To translate a custom string:

1. Using IBM Content
Navigator, browse to the
design\_or\_staging\_object\_store\_name/IBM Business Automation
Workflow/Solutions/solution\_name/nls
folder.
2. Download the Resources.js file.
3. Create your target locale directory in the original directory.
For example, if your target locale is French, create the
following directory: design\_or\_staging\_object\_store\_name/IBM Business Automation
Workflow/Solutions/solution\_name/nls/fr.
The locale values are case sensitive. Use hyphen separators instead of underscores in the
locale values. For example, specify en-us instead of
en\_us. If your solution locale is French and you want to translate the
solution to English, use locale en.
4. Edit the downloaded Resources.js file.
Change the value for the custom string to the translated value for
your locale.
For example, change the English value for
a customized page title: "New Work": "New Work" to
a localized title: "New Work":"Nouveau Travail"

Attention: The encoding of the Resources.js file
must be set to UTF-8 or UTF-8 without BOM.
5. Make the same changes for any other customized strings
that you want to translate.
6. Add the translated Resources.js file
to the design\_or\_staging\_object\_store\_name/IBM Business Automation
Workflow/Solutions/solution\_name/nls/fr folder
as a document of Document class and as a major version. The document
title must be Resources.js.
7. Repeat these steps for each language you want to translate
to.
8. Redeploy the solution.

## Results