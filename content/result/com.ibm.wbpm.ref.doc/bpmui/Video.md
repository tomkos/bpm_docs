### Methods

### Parent

### Helpers

<!-- image -->

| Width:        | The width in px, % or em.\r\nFor example\: 50px, 20%, 0.4em. If no unit is specified, px is assumed.   | String   |
|---------------|--------------------------------------------------------------------------------------------------------|----------|
| Height:       | Height in px, em\r\nFor example\: 50px, 0.4em. If no unit is specified, px is assumed                  | String   |
| Poster image: | URL for poster image                                                                                   | String   |

| Video source type:   | Type of video {MP4 | WEBM | FLV | M3U8}                           | VideoSourceType   |
|----------------------|-------------------------------------------------------------------|-------------------|
| Auto preload:        | When enabled, video data will begin loading as soon as view loads | Boolean           |
| Auto play:           | When enabled, video will start playing as soon as view is loaded  | Boolean           |

| Name     | Type     | Default   | Description                                                                                                     |
|----------|----------|-----------|-----------------------------------------------------------------------------------------------------------------|
| name     | {string} |           | CSS class name(s) to add to the control. Separate class names by a space if more than one class.                |
| replaced | {string} |           | CSS class name(s) to be replaced by the first argument. Separate class names by a space if more than one class. |

| Name         | Type      | Default   | Description                                                               |
|--------------|-----------|-----------|---------------------------------------------------------------------------|
| collapseFlag | {boolean} |           | Set to true to collapse the view (equivalent to a view setting of "NONE") |

| Name   | Type    | Default   | Description                                    |
|--------|---------|-----------|------------------------------------------------|
| event  | {Event} |           | Value change event (usually an onchange event) |

| Name        | Type      | Default   | Description                                |
|-------------|-----------|-----------|--------------------------------------------|
| autoPreload | {boolean} |           | set to true to enable automatic preloading |

| Name     | Type      | Default   | Description                    |
|----------|-----------|-----------|--------------------------------|
| autoplay | {boolean} |           | Set to true to enable autoplay |

| Name     | Type      | Default   | Description                                                                   |
|----------|-----------|-----------|-------------------------------------------------------------------------------|
| enabled  | {boolean} |           | Enabled/read-only flag (true to enable view, false to disable/make read-only) |
| required | {boolean} |           | Enable/disable required field flag for control                                |

| Name   | Type     | Default   | Description         |
|--------|----------|-----------|---------------------|
| height | {string} |           | Video player height |

| Name    | Type      | Default   | Description                                                    |
|---------|-----------|-----------|----------------------------------------------------------------|
| visible | {boolean} |           | Label visibility flag (true to show view label, false to hide) |

| Name   | Type     | Default   | Description                                                                                      |
|--------|----------|-----------|--------------------------------------------------------------------------------------------------|
| url    | {string} |           | Poster image url location. Poster image will be displayed over the video while it isn't playing. |

| Name   | Type     | Default   | Description            |
|--------|----------|-----------|------------------------|
| type   | {string} |           | "MP4" | "WEBM" | "FLV" |

| Name      | Type      | Default   | Description                                                                                                                                 |
|-----------|-----------|-----------|---------------------------------------------------------------------------------------------------------------------------------------------|
| valid     | {boolean} |           | Valid/invalid flag (true to set view valid, false to make it invalid - which typically shows the view with "invalid" styling and indicator) |
| errorText | {string}  |           | Validation error text to show on the invalid-styled view                                                                                    |

| Name   | Type     | Default   | Description      |
|--------|----------|-----------|------------------|
| url    | {string} |           | Video source URL |

| Name                | Type      | Default   | Description                                                                            |
|---------------------|-----------|-----------|----------------------------------------------------------------------------------------|
| data                | {Object}  |           | Value of bound data. The type of this parameter must match the type of the bound data. |
| createPseudoBinding | {boolean} |           | If set to true, creates a pseudo binding if there is no current binding.               |

| Name     | Type      | Default   | Description                                                             |
|----------|-----------|-----------|-------------------------------------------------------------------------|
| visible  | {boolean} |           | Visibility flag (true to show view, false to hide)                      |
| collapse | {boolean} |           | Set to true to collapse the control space when visible is set to false. |

| MyView.setVisible(false, false); //Equivalent to MyView.hide()   |
|------------------------------------------------------------------|
| MyView.setVisible(false, true); // Sets visibility to "None"     |

| Name   | Type     | Default   | Description        |
|--------|----------|-----------|--------------------|
| width  | {string} |           | Video Player width |

| Name   | Type   | Default                | Description                   |
|--------|--------|------------------------|-------------------------------|
| phase  | {int}  | bpmext.ui.PHASE\_NORMAL | The phase we are currently in |