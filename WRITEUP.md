
# Write-up Template

### Analyze, choose, and justify the appropriate resource option for deploying the app.

VM
An Azure VM gives you the flexibility of virtualization without having to buy and maintain the physical hardware that runs it. However, you still need to maintain the VM by performing tasks, such as configuring, patching, and installing the software that runs on it.

App Service
Azure App Service enables you to build and host web apps, mobile back ends, and RESTful APIs in the programming language of your choice without managing infrastructure. It offers auto-scaling and high availability, supports both Windows and Linux, and enables automated deployments from GitHub, Azure DevOps, or any Git repo


VM seems to be better options when you need more control but it cost more and requires to maintain whilst app service is cheaper easy to deploy and do not require maintenance.

I have chosen to use App service since I do not require any complex configuration and wanted to get something app and running as fast as possible. Which was very easy with Azure app service


### Assess app changes that would change your decision.
For me to choose VM, the app would need to have requirements for multiple environments (prod, dev, stage). Or I would need to implement integration tests which would be easier to implement on the VM. Also, I would choose VM if I need more control or needed to support a legacy application