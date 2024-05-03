# Software Templates

The software templates feature of Allen is a tool that enables you to create new software components (microservices, libraries, pipelines, etc.) pre-configured to operate in your team context and environments. Pre-configure the template with your code stubs, favorite libraries, logging configuration, building, packaging and deployment workflows so you can get started quickly. Leverage the (Get Access)[https://allen.ingka.com/get-access] automations to create what you need, e.g. artifact repositories, tokens for deployments, etc.

## Core concepts

- **Template**. A set of templated files which can be used to generate a service by providing the required input. A **Go microservice** template containing templated files to generate a microservice based on Go, including:
  - GitHub Action workflows for building and deploying, security scanning, etc
  - Go files to bootstrap an HTTP server, set up logging, OpenTelemetry instrumentation
  - Dockerfile
- **Template entity**. An entity representing the template in the Allen software catalog. You create this entity with a `template.yaml` descriptor file which is used to define the inputs required for the template and the actions that should be executed.
- **Template actions**. Steps in your template that define what should happen as part of your template. This can be things like creating a repository, opening a pull request, creating a deploy key, integrating a repository with Vault through GitHub OIDC, etc.
- **Template parameters**. The parameters are inputs needed for the template which are provided by the user. These parameters can be to control the actions or can be substituted inside the generated files.

## Next steps

- Get started by creating your own templates [guide](./create-a-template.md).
- Check out the [template catalog](https://allen.ingka.com/scaffold) and browse through the existing templates.
