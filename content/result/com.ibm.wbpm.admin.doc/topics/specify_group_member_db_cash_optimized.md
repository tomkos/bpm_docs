# Optimizing the group member cache heap size

## Procedure

- To reduce the heap usage, you can set the group-member-cache-memory-optimized
property to true, which causes the cache objects to be stored with a reduced memory
allocation. However, the drawback is that additional object conversions are needed when objects are
retrieved from the cache, which could reduce performance.
For
example:<server merge="mergeChildren">                 
    <group-member-cache-memory-optimized merge="replace">true</group-member-cache-memory-optimized>
</server>
- To limit the number of groups that are held in the GroupMembers cache, you can set the
group-member-cache-max-size  property. When the limit is reached, the least
recently used (LRU) group will be replaced when a cache miss occurs. 
For example, to limit the cache to 200
groups:<server merge="mergeChildren">
    <group-member-cache-max-size merge="replace">200</group-member-cache-max-size>
</server>Important: The actual memory size of the cache will depend on the size of the groups that are
cached.