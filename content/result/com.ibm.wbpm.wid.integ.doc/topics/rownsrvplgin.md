<!-- image -->

# Contributing your own external service or data wizard plug-in

The following topics describe the extension
point plug-ins provided for you. Extending these plug-ins allows you
to create your own unique version of them.

- Overview
- Wizard extension point
- Category extension point
- References

## Overview

Two extensible plug-ins,
usually referred to as extension points, are used to create your own
external service or data wizard.

- com.ibm.wbit.adapter.templates.ui.wizard - This extension point
describes the external service or data wizard that you will extend
with your contribution.
- com.ibm.wbit.adapter.templates.ui.category - This extension point
describes the hierarchical categories on the first page of the wizard
that you will extend with your contribution.

These two extension points together form the wizard. The
relationship is that the wizard plug-in references the category plug-in.

## Wizard extension point

The
wizard extension point is used to contribute a new wizard implementation
which can be invoked from the external service or external data wizard.

| Wizard definition attributes   | Required?   | Value                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|--------------------------------|-------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| capability                     | Required    | Specifies the capability of this wizard. If it is set to ExternalService, the wizard will appear as an option in the external service wizard. If it is set to ExternalData, the wizard will appear as an option in the external data wizard.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| category                       | Required    | The ID of the category this wizard belongs to. These are the IDs of the com.ibm.wbit.adapter.templates.ui.categoryextension. The displayed name is defined in the category extension itself. Subcategories can be delimited by double slashes (for example, BPEL.id//eForms.id).                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| class                          | Required    | The class that implements the interface com.ibm.wbit.adapter.templates.ui.IExternalServiceWizard (for capability = "ExternalService") or com.ibm.wbit.adapter.templates.ui.IExternalDataWizard (for capability = "ExternalData"). If you want the context from which the wizard is launched, the IWizard class returned from the getWizard() method must implement the interface com.ibm.wbit.adapter.templates.ui.IContextualWizard.                                                                                                                                                                                                                                                                                                    |
| configuration                  | Optional    | A qualified name (QName) specifying the configuration that will be used. The configuration defines the Discovery Agent and Resource Writer used to generate artifacts. This is only applicable for wizards set to capability = "ExternalData".                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| description                    | Required    | A description of what the wizard does. This description will be displayed in the window description, and if no HTML file is specified in the preview\_html field, then this description text is displayed in place of that.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| help\_id                        | Optional    | A root help ID that can be invoked when the user clicks inside the preview window or presses the F1 button when in the wizard. This is an F1 help ID defined in the help system.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| icon                           | Optional    | Icon associated with this wizard in the external service or external data wizard navigation tree.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| id                             | Required    | A unique identifier for this wizard.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| keywords                       | Optional    | Any tags or keywords to be used during the keyword filtering entry field. Single words are preferred, separated by commas.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| name                           | Required    | The display name to be associated with the wizard in the external service or external data wizard navigation tree.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| preview\_html                   | Optional    | This is an optional filename of a formatted HTML preview of the wizard. A regular textual description still needs to be specified, but specifying this attribute allows the wizard to display fancier formatted text whenever there is room to do so. This is a relative path to the root of the plugin. You also have to make sure that your HTML files are included in the build by adding it to the binary build properties of your plugin (for example, html/index.html would be a typical entry for this). You can also specify a .txt file for this entry. This will display properly. Lastly, if no entry is specified for this, the description box will just display the text in the description field of this extension point. |
| product                        | Optional    | A keyword specifying the product this wizard is targeted for. These are single words separated by spaces. If not specified, the assumption is that this wizard will be available for all installed products.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| qname                          | Optional    | Specifies a unique qualified name (QName) that identifies the wizard. This qualified name is of the format <.namespace>:<.localName>. qname is only applicable for wizards set to capability = "ExternalData".                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| target\_id                      | Optional    | target\_id is a sub id, which is used whenever the wizard is only to be invoked as part of another specific plugin action or wizard. Whenever, this attribute is set, it will not appear in the global view. Plugins can use the templates.ui to return TemplateWizardType with a specific ID.                                                                                                                                                                                                                                                                                                                                                                                                                                            |

```
<extension point="com.ibm.wbit.adapter.templates.ui.wizard">
 <wizardDefinition
  capability="ExternalService"
  category="com.ibm.wbit.adapter.external.category.adapters"
  class="com.ibm.wbit.adapter.emd.ui.template.wizards.CICSService"
  description="%CICS\_SERVICE\_DESCRIPTION"
  help\_id="com.ibm.wbit.adapter.emd.ui.CICSService"
  icon="icons/etool16/cicsecirar\_obj.gif"
  id="com.ibm.wbit.adapter.external.service.CICSService"
  name="%CICS\_SERVICE">
 </wizardDefinition>
</extension>
```

```
<extension point="com.ibm.wbit.adapter.templates.ui.wizard">
 <wizardDefinition
  capability="ExternalData"
  category="com.ibm.wbit.adapter.external.category.languages"
  class="com.ibm.wbit.adapter.emd.ui.template.wizards.CICSData"
  description="%COBOL\_DATA\_DESCRIPTION"
  icon="icons/etool16/cicsimsbo\_obj.gif"
  id="com.ibm.wbit.adapter.external.data.Cobol"
  name="%COBOL\_DATA"
  configuration="com/ibm/wbit/adapter/emd/cobol/writer:COBOL\_TO\_XSD"/>
 </wizardDefinition>
</extension>
```

## Category extension point

The
category extension point provides categories and subcategories for
the navigation tree in the external service and the external data
wizard. These categories are used by the wizard (com.ibm.wbit.adapter.templates.ui.wizard)
extension point.

| Category definition attributes   | Required?   | Value                                                                          |
|----------------------------------|-------------|--------------------------------------------------------------------------------|
| icon                             | Required    | The icon to represent this category in the navigation tree (16 x 16 pixels).   |
| id                               | Required    | The unique ID of this category.                                                |
| name                             | Required    | The display name of the category.                                              |
| parent\_category                  | Optional    | If this category is a subcategory, then this is the ID of its parent category. |

```
<extension point="com.ibm.wbit.adapter.templates.ui.category">
 <category
  icon="icons/obj16/adapters.gif"
  id="com.ibm.wbit.adapter.external.category.adapters"
  name="%CATEGORY\_ADAPTERS"/>
 <category
  icon="icons/obj16/ios\_obj.gif"
  id="com.ibm.wbit.adapter.external.category.languages"
  name="%CATEGORY\_LANGUAGES"/>
</extension>
```

## References

Creating an Eclipse
plug-in such as this one follows a standard process described in PDE Does Plug-ins. Inside IBM® Integration
Designer,
the example section of Contributing your own mediation primitive plug-in shows you the exact steps to create
a plug-in project, modify the plugin.xml file, and so on, which would
be similar to what you must do when creating your own external service
or data wizard plug-in.

## Related concepts

- Pattern of accessing external services with adapters
- Developing services with adapters
- Simple adapter wizard
- Migrating applications using previous adapter levels

## Related tasks

- Configuring and using adapters
- Creating a business object from a source file

## Related reference

- J2C data bindings
- A closer look at business objects from data structures
- J2C imports and exports at run time
- Trade-offs when developing adapter imports and exports
- Considerations when using adapters
- Considerations when refactoring
- Limitations for adapter imports and exports