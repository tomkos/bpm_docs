# Exporting other FileNet P8 assets

## Before you begin

## About this task

If you extend your solution with other FileNet P8 assets, you must migrate
the assets to the target domain by using the appropriate migration
tool for that asset, such as FileNet Deployment
Manager or
the Process Configuration console.

Follow these procedures to
migrate assets from the development environment target object store
to the target environment object store. These assets are not recognized
by Case Builder, but your
business processes might use these assets.

You can also follow
these procedures to move a solution from one development environment
to another. For example, if you are a solution provider and you want
to move your solution from your development environment to your customer's
development environment.

- Using FileNet Deployment Manager to export other FileNet P8 assets

Use FileNet Deployment Manager to migrate assets that were created with IBM FileNet P8 tools from the development environment target object store to the target environment object store. These assets are not recognized by Case Builder, but your business processes might use these assets.
- Include options for assets in FileNet Deployment Manager

The include options in FileNet Deployment Manager specify which related objects and associated metadata are included in the export set for an object. The include options must be set correctly to ensure that the object can be imported into any target environment.
- Exporting other FileNet P8 assets by using the Process Configuration console

Use the Process Configuration console from within IBM Administration Console for Content Platform Engine to export Process Services assets from the development environment target object store to the test or production environment target object store.