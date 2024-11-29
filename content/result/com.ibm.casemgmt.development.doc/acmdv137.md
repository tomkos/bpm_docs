# Defining the widget package catalog file

```
{
    "Name":"IBM Case Manager Widget package",
    "Description":"Description of package",
    "Locale":"",
    "Version":"5.3.3",
    "Categories":[
        
        {
            "id":"EducationWidgets",
            "title":"Education Widgets"
        } 
    ],
    "Widgets":[
        {

            "id":"CustomInbasket",
            "title":"Custom Inbasket",
            "category":"EducationWidgets",
            "description":"EN description of Custom Inbasket",
            "definition":"CustomInbasket.json",
            "preview":"images/custom/custominbasket\_preview.gif",
            "icon":"images/custom/custominbasket\_icon.gif",
            "runtimeClassName":"icm.pgwidget.inbasket.CustomInbasket",
            "previewThumbnail":"images/custom/custominbasket\_thumb.gif"
        } 
    ]
]
```

| Property                 | Required or Optional   | Type       | Description                                                                                                                                                                                                                                                                                                              |
|--------------------------|------------------------|------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Name                     | Required               | String     | A name for the custom page widget package. Specify a unique name for the package to avoid overriding an existing page widget package.                                                                                                                                                                                    |
| Description              | Required               | String     | A description of the custom page widget package.                                                                                                                                                                                                                                                                         |
| Locale                   | Required               | String     | The two-character locale code for the current catalog. For example, zh is the locale code for simple Chinese.The code is added as a subfolder name when the widget definition file is retrieved. By default, the locale is set to "".                                                                                    |
| Version                  | Optional               | String     | The version number that is assigned to the widget package.                                                                                                                                                                                                                                                               |
| Categories               | Optional               | String     | The categories in Case Builder in which the custom page widgets in this package are listed.You can choose to list the page widgets in one of the following categories, which are provided by IBM® Business Automation Workflow: CaseWidgets GenericWidgets  For each category, you must provide an identifier and title. |
| Categories/id            | Required               | String     | A unique identifier for the widget category.                                                                                                                                                                                                                                                                             |
| Categories/title         | Required               | String     | The name that is to be displayed in Case Builder for the widget category.                                                                                                                                                                                                                                                |
| Widgets                  | Required               | JSON array | An array that identifies the custom page widgets in this package. For each page widget, you must provide the following information: id category title description definition preview icon runtimeClassName previewThumbnail                                                                                              |
| Widgets/id               | Required               | String     | A unique identifier for the page widget.                                                                                                                                                                                                                                                                                 |
| Widgets/category         | Required               | String     | The identifier of the category in which the page widget is to be listed in Case Builder.                                                                                                                                                                                                                                 |
| Widgets/title            | Required               | String     | The name to be displayed for the page widget in Case Builder.                                                                                                                                                                                                                                                            |
| Widgets/description      | Required               | String     | A description of the page widget. This text is used as hover help for the widget in Case Builder.                                                                                                                                                                                                                        |
| Widgets/definition       | Required               | String     | The full path and name of the definition file for the page widget.                                                                                                                                                                                                                                                       |
| Widgets/preview          | Required               | String     | The relative path and name of the resource file that contains the preview image for the page widget. For example, the value might be images/myWidget\_prv.png. The image can be a .png file or a .gif file. This image is not used in IBM Business Automation Workflow V5.2.                                              |
| Widgets/icon             | Required               | String     | The relative path and name of the resource file that contains the icon image for the page widget. For example, the value might be images/myWidget\_icon.png. The image can be a .png file or a .gif file. This image represents the page widget in the Case Builder palette.                                              |
| Widgets/runtimeClassName | Required               | String     | The class name for the page widget as specified in the runtime plug-in for the widget package.                                                                                                                                                                                                                           |
| Widgets/previewThumbnail | Required               | String     | The relative path and name of the resource file that contains the thumbnail image for the page widget. For example, the value might be images/myWidget\_thnl.png. The image can be a .png file or a .gif file. This image is not used in IBM Business Automation Workflow V5.2.                                           |