# Generating URLs of managed assets

## About this task

The com\_ibm\_bpm\_coach.getManagedAssetUrl global JavaScript function composes the
URL to the managed assets without checking whether the asset exists or not.

## Procedure

1. Use the following syntax: 

syntax
com\_ibm\_bpm\_coach.getManagedAssetUrl = function(assetName,
assetType, projectShortName,
returnWithoutAssetName, additionalPath,
addBuildNumberParameter)

returns
the URL of the managed asset. If assetType is not one of the three allowed
(see the following table), the function returns null. The returned URL looks something like the
following
example:/teamworks/webasset/<snapshot ID>/<assetType>/<assetName><additionalPath>?build=xxxx The
snapshot ID is determined by the framework and the other parts of the URL by the parameters that you
include.
2 Use the following parameters: Parameter Description assetName (String ) The file name of the managed asset. Note: You can use the'! ' notation to reference a file inside an archive. For example, if you arepointing to an image file in a .zip file, use the following format for the URL:file .zip !path /file .extension . assetType (String ) The type of the managed asset. Must be one of the following: projectShortName (String ) The short name of the project where the managed asset is requested. If this isnot provided, the current project is assumed. If the module is in a referenced toolkit, you mustinclude the PROJECT parameter to ensure that the view can use module in thecontext of the process application. returnWithoutAssetName (Boolean ) (Optional) Sets whether the returned URL includes the asset name. If thisparameter is not provided, the default is false, and the asset name is included in the URLpath. additionalPath (String ) (Optional) If the returnWithoutAssetName parameter is setto false, appends the provided path to the assetName in the returned URL. addBuildNumberParameter (Boolean ) (Optional) Sets whether the returned URL includes the current build number asa query parameter. The build number is unique for different versions and fix packs. If you are usingthe returned URL to retrieve the asset directly, use this parameter to prevent the browser loading astale version from its cache.

| Parameter                         | Description                                                                                                                                                                                                                                                                                                           |
|-----------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| assetName (String)                | The file name of the managed asset. Note: You can use the '!' notation to reference a file inside an archive. For example, if you are pointing to an image file in a .zip file, use the following format for the URL: file.zip!path/file.extension.                                                                   |
| assetType (String)                | The type of the managed asset. Must be one of the following:  com\_ibm\_bpm\_coach.assetType\_WEB: web managed asset (css, png, ..)  com\_ibm\_bpm\_coach.assetType\_SERVER: server managed asset (for example zip, jar)  com\_ibm\_bpm\_coach.assetType\_DESIGN: design managed asset (xsl)                                      |
| projectShortName (String)         | The short name of the project where the managed asset is requested. If this is not provided, the current project is assumed. If the module is in a referenced toolkit, you must include the PROJECT parameter to ensure that the view can use module in the context of the process application.                       |
| returnWithoutAssetName (Boolean)  | (Optional) Sets whether the returned URL includes the asset name. If this parameter is not provided, the default is false, and the asset name is included in the URL path.                                                                                                                                            |
| additionalPath (String)           | (Optional) If the returnWithoutAssetName parameter is set to false, appends the provided path to the assetName in the returned URL.                                                                                                                                                                                   |
| addBuildNumberParameter (Boolean) | (Optional) Sets whether the returned URL includes the current build number as a query parameter. The build number is unique for different versions and fix packs. If you are using the returned URL to retrieve the asset directly, use this parameter to prevent the browser loading a stale version from its cache. |