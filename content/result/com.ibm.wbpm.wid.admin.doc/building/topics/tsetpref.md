<!-- image -->

# Setting Preferences

## About this task

- Controlling prompts about the Build Automatically menu item

By default, you receive a prompt whenever you change a build activity in the Build Activities view and the Project > Build Automatically menu item is not in the selected state. However, you can set a preference to either suppress or display the prompt.
- Disabling or enabling the Publish Changes window

If changed resources exist in the workspace and they have not yet been published to the servers, a View and Publish Changes to Servers window will open by default when you click the Update Running Servers button. The window enables you to view the specific resources that have changed and it allows you to choose whether to publish the resources to the servers. However, you can set a preference to disable or enable the window. If you choose to disable the window, all changed workspace resources will automatically be published to the servers when you click the Update Running Servers button.
- Controlling clean build participation for libraries

When you use the Project > Clean menu item to invoke a full build of projects in the workspace, the resources in all of the libraries are automatically revalidated. If you have libraries that contain large XML schemas or WSDL files, the process of revalidating the library resources can considerably add to the time required for the build to complete. However, if you have one or more libraries that contain large files and you do not expect the libraries to change, you can exclude them from the builds and subsequently reduce the overall build time.