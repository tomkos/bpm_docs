<!-- image -->

# Managing builds

## About this task

- Builds in IBM Integration Designer

In IBM Integration Designer, workspace resources are stored in several types of authoring projects, such as modules, mediation modules, libraries, and component test projects. Depending on the number of authoring projects in the workspace and the specific build activities that occur during a build, it can take varying amounts of time for a build to complete. However, you can now choose the specific build activities that you want to occur during an automatic or manual build, which can help you significantly reduce build times.
- Build Activities view

In IBM Integration Designer, the Build Activities view is the designated tool for managing builds. It features a simple user interface that enables you to easily select build activities for both automatic and manual builds and invoke immediate manual builds that are independent of your build activity selections. The Build Activities view also enables you to view the build and server status of business integration projects as well as the operational state of supported servers.
- Setting Preferences

By default, the user-definable preferences for the Build Activities view are already optimized for builds. However, in the course of your build activities, you may find that you want to change some preferences.
- Specifying build activities for builds

In the Build Activities view, you can specify the build activities that you want to have invoked whenever an automatic or manual build occurs. For example, you can choose to have your projects validated but not have deploy code generated during a build. This can substantially reduce the time required for builds to complete. Or you can choose to have your projects validated and deploy code generated during a build. Or you can even choose to have your projects validated and deploy code generated during a build, plus have the integration modules and component test projects that currently reside on running servers updated on completion of the build.
- Invoking manual builds

In the Build Activities view, you can invoke an immediate manual build that will temporarily override any build activity selections. For example, you can invoke a build that will validate your business integration projects and generate deploy code for your integration modules and component test projects. Or you can invoke an immediate build that will validate your projects and generate deploy code plus automatically update the integration modules and component test projects that currently reside on running servers. If you occasionally find that these build capabilities are not sufficient to synchronize the projects in your workspace with the same projects on the server, a menu item is provided that enables you to remove your projects from the server, regenerate deploy code and backing projects, and redeploy the projects to the server.
- Viewing the status of projects

In the Project Status section of the Build Activities view, you can see the build status for individual business integration projects as well as the server status for integration modules and component test projects. The build status includes information on whether the projects have been validated and whether deploy code has been generated. The server status includes information on the current operational state of the server and whether any integration modules or component test projects have been deployed to the server.
- Publishing changed resources to servers

If changed (new, modified, or deleted) resources exist in your workspace and you click the Update Running Servers button in the Build Activities view, a window will open that enables you to view the resources and choose whether to publish the updates to the servers.