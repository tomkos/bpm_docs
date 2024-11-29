# Video

## Data binding

## Configuration properties

Under Configuration,
set or modify the appearance and behavior properties for the view.

<!-- image -->

| Appearance configuration property   | Description                                                                                                                                                                           | Data type   |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| Width                               | Specifies the width of the view. You can specify the width in px (pixels), % (percent), or em units. For example, 50px, 20%, or 0.4em. If no unit type is specified, px is assumed.   | String      |
| Height                              | Specifies the height of the view. You can specify the height in px (pixels), % (percent), or em units. For example, 50px, 20%, or 0.4em. If no unit type is specified, px is assumed. | String      |
| Poster image                        | The URL for the poster image.                                                                                                                                                         | String      |

| Behavior configuration property   | Description                                                                       | Data type   |
|-----------------------------------|-----------------------------------------------------------------------------------|-------------|
| Video source type                 | The type of video. Choose from MP4, WEBM, FLV and M3U8.                           | String      |
| Auto preload                      | When this option is enabled, video data begins loading as soon as the view loads. | Boolean     |
| Auto play                         | When this option is enabled, the video starts playing as soon as view is loaded.  | Boolean     |

| Track configuration property   | Description                                                                                                                                                                                                                                                                                                                                     | Data type   |
|--------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| source\_Filename                | The name of the text file that contains the track text. The file must be in WebVTT format and it must be added as a managed asset in the  library.                                                                                                                                                                                              | String      |
| languageCode                   | The two-letter code for the language of the text track. You must use a valid BCP 47 language tag. For example, en for English.                                                                                                                                                                                                                  | String      |
| label                          | The label for the track that is shown to the user. For example, the label appears as an option in a menu that lists the different languages available for subtitles.                                                                                                                                                                            | String      |
| kind                           | The type of track. Supported types are Subtitles, Captions, and Chapters.                                                                                                                                                                                                                                                                       | String      |
| default                        | Select the default option to show the language that is defined in this track by default. For example, you might define a track for English, another for French and another for German. You can set one of these tracks to be the default. If you do not set a default, the viewer must select the language from the captions or subtitles menu. | Boolean     |

## Events

- On load: Activated when the view loads for
exampleme.setWidth(${DeviceSensor}.getDeviceInfo().clientWidth)

## Methods

For detailed information on the available methods for Video, see the Video JavaScript API.

## Additional resources

For information about how to create a coach or page, see Building coaches. 
For information about standard properties
(General, Configuration,
Positioning, Visibility, and HTML
Attributes), see View properties.