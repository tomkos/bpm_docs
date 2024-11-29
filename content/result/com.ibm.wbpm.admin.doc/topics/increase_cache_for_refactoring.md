# Increasing the maximum number of cached objects during refactoring

Your attempt to copy or clone a large project might fail with an error.

```
CWLLG1274E: An exception occurred. com.ibm.bpm.pal.PALException: RepositoryServicesCore.cloneProcessApp.fail: 
Number of Objects to copy 1200 is larger than max-cached-objects-during-refactoring 256
```

To fix or avoid this error, increase the value of the
max-cached-objects-during-refactoring setting.

| Element                               |   Default setting | Description                                                                                                                                                                                                                                                                           |
|---------------------------------------|-------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| max-cached-objects-during-refactoring |              256  | This setting limits the number of objects that can be involved in a copy operation. For example, if you have a snapshot with 1200 objects, this setting must be set to more than this number of objects to successfully create a project based on a copy of that snapshot or version. |

```
<server>
     <repository>
          <max-cached-objects-during-refactoring merge="replace">256</max-cached-objects-during-refactoring>
     </repository>
</server>
```

For information about the 100Custom.xml file's location and how to create,
modify, and deploy it, see The 100Custom.xml file and configuration.