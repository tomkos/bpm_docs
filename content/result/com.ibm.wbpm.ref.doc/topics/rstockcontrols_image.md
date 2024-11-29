# Image (deprecated)

<!-- image -->

## Restrictions and limitations

None

## Data binding

| Binding description                                                                                                                                                                                                                                                                                                                                                                                                                                           | Data type   |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| Contains the location of the image that this control displays. Typically, you bind this control to an image stored as a web file. If you bind this control to a web file, the URL is the relative path to retrieve the file from the server. If you bind to a variable, the variable must contain a URL that is resolvable on the server. Tip: While you can use absolute URLs, relative URLs are better because they can avoid triggering security warnings. | Url         |

## Configuration properties

<!-- image -->

| Configuration property      | Description                                                                                                                             | Data type   |
|-----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|-------------|
| Alternate Text              | Enter a description of the image to make it accessible for users and technologies that cannot see the image.                            | String      |
| Height                      | Set the number of pixels to reserve for the height of the image. The image scales to fit this size if necessary.                        | Integer     |
| Width                       | Set the number of pixels to reserve for the width of the image. The image scales to fit this size if necessary.                         | Integer     |
| Caption                     | Enter text to display with the image.                                                                                                   | String      |
| Caption Vertical Position   | Set whether the caption is above or below the image.The default value is Above.                                                         | String      |
| Caption Horizontal Position | Set whether the caption aligns to the left side of the image, to the right side of the image, or is centered.The default value is Left. | String      |