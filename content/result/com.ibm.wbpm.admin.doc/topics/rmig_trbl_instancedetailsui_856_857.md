# Instance Details UI controls fail to render

- Instance Details UI controls fail to render in the browser. The
browser console might have an error related to the coachViewHelper.js file.
- IBM BPM has been migrated from V8.5.6 to IBM® Business Automation
Workflow
24.0.0.0.
- The process applications with the client-side human services that
contain the Instance Details UI controls were created in V8.5.6.

To solve the problem, add a dependency on the Responsive
Coaches toolkit 24.0.0.0 to all
process applications that have these custom Instance Details UI controls.
Process applications created in V8.5.7 automatically have this dependency.