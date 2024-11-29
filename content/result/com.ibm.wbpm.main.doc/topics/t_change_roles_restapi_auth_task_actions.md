# Changing roles for REST API authorizations on task actions

## About this task

- Business Automation Workflow administrator
- Process application administrator
- Instance owner
- Task owner

- Potential task owner
- Task collaborator
- Task team manager

## Procedure

```
<server merge="mergeChildren"> 
   <portal merge="mergeChildren">
      <authorization-level-for-task-complete-and-finish merge="replace">8560</authorization-level-for-task-complete-and-finish>
   </portal>
</server>
```

For information about how to prevent tasks from completing in suspended BPD
instances, see the topic Preventing tasks from completing in suspended BPD instances.