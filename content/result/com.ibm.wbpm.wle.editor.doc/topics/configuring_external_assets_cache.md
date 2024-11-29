# Configuring managed asset and managed asset classloader cache
sizes

## About this task

The <classloader-resource-map-size> parameter specifies the number of Java
classes that managed assets can contain and cache across all snapshots. The size must be large
enough to hold all the files from all the managed asset JAR files in your snapshots in the
deployment environment. When multiple snapshots include the same set of managed asset JAR files, you
must count the file contents multiple times. When a toolkit snapshot contains managed assets, you
must count the file contents only once regardless of how many process application or toolkits refer
to it. Include a buffer in the cache size you set so that it does not exceed the limit with further
application development. The following example shows how to calculate the required cache size.

- file1.jar containing 50 class files
- file2.jar containing 70 class files
- file3.jar containing 100 class files

```
<server>
    <classloader-cache-size merge="replace">1000</classloader-cache-size>
    <classloader-resource-map-size merge="replace">5120</classloader-resource-map-size>
</server>
```

You can use the following methods to calculate the memory requirements for the managed asset
cache and managed asset classloader cache. If the sizes of these caches cause memory issues for your
application cluster members, you might need to increase the Java heap size.

For each file in the managed asset JAR file, the memory that is used by the managed asset caches
is the sum of two lists. One list contains the asset and the other list contains an internal
representation. The lists are of type java.util.LinkedList, which takes a key and a
value. The key consists of a UUID and the path within the JAR file. The UUID is always 36 bytes, but
the path length and therefore the size might vary. This key is used by both lists.

```
2 x (UUID + path length) + file content + internal representation
```

```
2 x ( 36 bytes + path length) + file content + 52 bytes
```

```
* com/test/EchoService.class * com/test/EchoService.java, * META-INF/MANIFEST.MF * .classpath * .project
```

1 First list
    - Key = (e9771549-3ff8-4d81-b678-f5dfee1b1b12, com/test/EchoService.class) = 36 bytes
    - Path length = 26 bytes
    - Value = file content of com/test/EchoService.class = 931 bytes
2 Second list

- Key = (e9771549-3ff8-4d81-b678-f5dfee1b1b12, com/test/EchoService.class) = 36 bytes
- Path length = 26 bytes
- Value = "managedasset:61.f9b29441-0b1a-4f03-adfd-e98120b3c435" = 52 bytes

- When you use a managed asset, the entire JAR file is loaded, including each file that it
contains. To reduce the amount of data that is loaded, remove unnecessary files from the JAR file.
Managed assets are loaded in Lazy mode. When you try to access one class in a JAR file, the entire
JAR file is loaded.
- Memory usage depends on the file sizes and path lengths. Thousands of small files in a deep
package structure might have a significant impact on memory usage.