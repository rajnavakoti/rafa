# What is the Marketplace?

The [Marketplace](https://allen.ingka.com/marketplace) is a place to share InnerSource projects and reusable software components. It brings discoverability and reusability of software components with all engineers at Ingka. It allows you to publish your reusable components like GitHub Actions reusable workflows or Terraform modules.

## Publish to the Marketplace

To add reusable components to the Marketplace, you need to register them in Allen. This is done by adding the `catalog-info.yaml` file to the repository where your reusable component is and then registering it in Allen's register component page. If you are planing to develop a new reusable component, you can make use of the Marketplace reusable component template.

> Not all software components are reusable. Before publishing, please consider whether your software component can be used by other teams.

### Publish InnerSource projects

To add an [InnerSource](https://allen.ingka.com/docs/default/component/ospo/inner-source/) project to the Marketplace, create a new file called `catalog-info.yaml` in your repository with the following content:

```yaml
apiVersion: backstage.io/v1alpha1
kind: Component
metadata:
  name: name-of-project
  description: Description of InnerSource project
  tags:
    - inner-source
spec:
  type: website # can also be: service, library, other
  owner: my-team # The core team owning the InnerSource project
  lifecycle: production
```

For reference, you can take a look at the following InnerSource projects:

- Allen - https://github.com/ingka-group-digital/developer-portal/blob/main/catalog-info.yaml
- lint-asyncapi - https://github.com/ingka-group-digital/lint-asyncapi/blob/main/catalog-info.yaml#L1-L21

### Publish existing reusable software components

#### 1. Create the catalog entity descriptor file

The catalog entity descriptor file describes your reusable component and is used to register it to the Allen software catalog. The marketplace builds on top of the catalog by using specific types of entities.

Create the entity descriptor file with the name `catalog-info.yaml` and push it to your repository. Make sure to change it so that it's applicable for your reusable component.

```yaml
apiVersion: backstage.io/v1alpha1
kind: Resource
metadata:
  name: security-scan
  description: This reusable workflow allows you to scan your repository with Trivy and Blackduck for vulnerabilities
  annotations:
    github.com/project-slug: ingka-group-digital/security-scan-workflow # The repository name
  tags:
    - security
    - blackduck
    - trivy
spec:
  type: workflow
  owner: developer-portal-core # Change to your own team
  lifecycle: production
```

Currently, valid `spec.type` values are `workflow`, `composite-action`, `terraform-module` and `helm-chart`.

If your reusable software component is [InnerSource ready](https://allen.ingka.com/docs/default/component/ospo/inner-source/checklist-for-making-a-repository-innersource-ready/), you can also add the `inner-source` tag under `metadata.tags`.

#### 2. Register your reusable component

Open the [register component page](https://allen.ingka.com/catalog-import) and provider the full URL to the `catalog-info.yaml` file and go through the wizard to register it.

Allen will periodically fetch the `catalog-info.yaml` file and update in the catalog if there are any changes.

### Create a new GitHub Actions reusable component

If you want to create a new GitHub Actions reusable workflow or composite action, you can use our starter template. The template generates the following:

- "Hello World" example reusable workflow or composite action that can be edited directly
- GitHub Actions workflows to automatically manage the release process of the reusable component
- The Allen catalog entity descriptor file and automatically registers your reusable component to the Marketplace

To generate the reusable component, open the template wizard [here](https://allen.ingka.com/create/template/ComponentTemplate/github-reusable-component/wizard) and go through it. Once finished, you will have a new repository containing your reusable component.

## Would you like to contribute?

Use the following channels to leave us feedback:

- Slack [#marketplace-dev](https://ingka.slack.com/archives/C03P2DSN75K)
- Report bugs or request features [here](https://github.com/ingka-group-digital/developer-portal/issues/new/choose).
