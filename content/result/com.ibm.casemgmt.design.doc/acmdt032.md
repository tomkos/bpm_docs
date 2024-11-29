# Creating translated form templates for your case management application (deprecated)

## About this task

After
you complete this task, your users can set their browser locale or
the application language value in the Change Language and
Locale Settings window to the language of their choice,
and open the translated version of the form in the language.

## Procedure

To create translated form templates and map the translated
form templates to your case management application, complete the following
steps:

1 If you use FileNet® eForms , create translated formtemplates by completing the following steps:
    1. In your development environment, change the operating
system locale of the FileNet eForms
Designer server
to the language in which you want to create a form template.
For example, change your operating system to French to create
a form template in French.
    2. Open FileNet eForms
Designer,
and then create a translated form template.
 If you use
an existing form template, you should save the translated version
of the form template in a different name. 
 For example,
you can name the translated version of a form template that is named application to application\_fr or application\_french because
the translated version of the form template is in French.
2. If you use IBM® Forms,
follow the procedure in the IBM Forms product
documentation for creating translated form templates in IBM Forms Designer.
 If
you use an existing form template, you should save the translated
version of the form template in a different name. 
 For
example, you can name the translated version of a form template that
is named application to application\_fr or application\_french because
the translated version of the form template is in French.
3. Add the translated version of the form template that you created in the previous step to your
target object store by using IBM Content
Navigator.
4. Create a localization proxy document by copying and pasting
the following example text into a file with the extension .ilp.

<?xml version="1.0"?>
<localizationProxy>
     <default>
         <version>current</version>
         <id>{00F556FD-6625-462A-8880-32E00C022AA0}</id>
     </default>
     <mappings>
         <mapping locale="en-us">
             <version>current</version>
             <id>{00F556FD-6625-462A-8880-32E00C022AA0}</id>
         </mapping>
         <mapping locale="zh-cn">
             <version>released</version>
             <id>{01BF8FED-D301-4A1E-A054-519D5356F8E9}</id>
         </mapping>
         <mapping locale="fr">
             <version>released</version>
             <id>{DC5F4290-3CCF-401B-A551-60F61D182B6D}</id>
         </mapping>
     </mappings>
</localizationProxy>
Important: Be sure
to note the behavior that is documented in Step 9: Select a localization
proxy document as an attachment for the Form Attachment
Work Details page. The form template that is associated
with the current locale of the case worker is opened. The form data
document is saved with a reference to the specific form template that
was opened to create the form data. The specific form data template
is used to open the form data document in subsequent steps regardless
of the locale of the case worker.
Save the
localization proxy document. The localization proxy document file
name can be any name, but the extension must be .ilp.
5. In the localization proxy document, modify the following
parameters:

version
The version of the form template to use. The valid values are
current, released, or specific. When the version is released or current,
the ID is a version series ID. When the version is specific, the ID
is ID.A form template vsID or ID is
a unique string of 32 hexadecimal characters enclosed by brackets
in the following format: {xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx}. For
example, a form template vsID or ID might
be {00F556FD-6625-462A-8880-32E00C022AA0}.

mapping locale
Maps the browser language with the template.The value in the <default></default>  node
is used to display a page if a mapping cannot be established by using
the value in the <mappings></mappings> node.

id
The identification number of the translated form template that
you created in an earlier step. In the localization proxy document,
you can add as many translated form templates as you need.

You can map from locale to sub-locale, but
not from sub-locale to locale. For example, from the sample proxy
document, if the browser locale is fr , the template
with the following ID is used: {DC5F4290-3CCF-401B-A551-60F61D182B6D}.
 If the browser locale is zh-cn, the template with
the following ID is used: {01BF8FED-D301-4A1E-A054-519D5356F8E9}.
 If the browser locale is zh, the default template
is used.
6. Add the localization proxy document to the target object store as an object of the document
class by using IBM Content
Navigator. Record the identification number of
the translated form template for use in a later step.
7 In Case Builder ,configure all Form widgets in your case management solution to usethe localization proxy document:

1. For each page that contains the Form widget, except
the Form Attachment Work Details page, open the
page in Page Designer and click the Edit Settings icon
on the Form widget.
2. Select Form template from the Open
the form by using list. For Version,
select the version of the localization proxy document to use. For Version
series ID or Version ID, enter
the version series ID or version ID of the localization proxy document.
3. Save and deploy the solution.
8. Select a localization proxy document as an attachment for
the Form Attachment Work Details page.
The form template that is associated with the current
locale of the case worker is opened. The form data document is saved
with a reference to the specific form template that was opened to
create the form data. The specific form data template is used to open
the form data document in subsequent steps regardless of the locale
of the case worker.