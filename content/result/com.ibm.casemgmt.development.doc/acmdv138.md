# Defining a page widget definition file

| Property         | Required or Optional   | Type   | Description                                                                                                                                                                                                                                                                    |
|------------------|------------------------|--------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| id               | Required               | String | A unique identifier for the page widget.                                                                                                                                                                                                                                       |
| category         | Required               | String | The identifier of the category in which the page widget is to be listed in Case Builder.                                                                                                                                                                                       |
| title            | Required               | String | The name to be displayed for the page widget in Case Builder.                                                                                                                                                                                                                  |
| description      | Required               | String | A description of the page widget.                                                                                                                                                                                                                                              |
| definition       | Required               | String | The full path and name of the definition file for the page widget.                                                                                                                                                                                                             |
| preview          | Required               | String | The relative path and name of the resource file that contains the preview image for the page widget. For example, the value might be images/myWidget\_prv.png. The image can be a .png file or a .gif file. This image is not used in IBM® Business Automation Workflow V5.2.   |
| icon             | Required               | String | The relative path and name of the resource file that contains the icon image for the page widget. For example, the value might be images/myWidget\_icon.png. The image can be a .png file or a .gif file. This image represents the page widget in the Case Builder palette.    |
| runtimeClassName | Required               | String | The class name for the page widget as specified in the runtime plug-in for the widget package.                                                                                                                                                                                 |
| previewThumbnail | Required               | String | The relative path and name of the resource file that contains the thumbnail image for the page widget. For example, the value might be images/myWidget\_thnl.png. The image can be a .png file or a .gif file. This image is not used in IBM Business Automation Workflow V5.2. |
| properties       | Required               | Array  | An array that defines the properties that can be set for the page widget in Case Builder.                                                                                                                                                                                      |
| events           | Required               | Array  | An array that identifies the events that the page widget publishes and subscribes to.                                                                                                                                                                                          |

```
{
    "id":"CustomInbasket",
    "title":"Custom Inbasket",
    "category":"EducationWidgets",
    "description":"EN description of Custom Inbasket",
    "definition":"CustomInbasket.json",
    "preview":"images/custom/custominbasket\_preview.gif",
    "icon":"images/custom/custominbasket\_icon.gif",
    "runtimeClassName":"icm.pgwidget.inbasket.CustomInbasket",
    "previewThumbnail":"images/custom/custominbasket\_thumb.gif",
    "properties":[
    ],
    "events":[
 
    ]
}
```