# Add a Component to the software catalog

## Catalog-info.yaml

The source of truth for the software catalog are metadata entity descriptor YAML files, conventionally named `catalog-info.yaml` stored in GitHub or other configured origins.

```yaml
apiVersion: backstage.io/v1alpha1
kind: Component
metadata:
  name: es-service-X
  annotations:
    github.com/project-slug: ingka-group-digital/es-service-x
    backstage.io/techdocs-ref: url:https://github.com/ingka-group-digital/es-service-x
  tags:
    - java
    - quarkus
spec:
  type: service
  owner: engineering-services
  lifecycle: alpha
  system: devport
  providesApis:
    - example-api-x
  consumesApis:
    - example-api-y
```

| Field                                    | Values                                                                                                                             | Comment                                                                                                                                                                                                                                                                                                                                                                                                  |
| ---------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `kind`                                   | [`Component`, `Location`, `Resource`, `ComponentTemplate`]                                                                         |                                                                                                                                                                                                                                                                                                                                                                                                          |
| `spec.owner`                             | [Groups](https://allen.ingka.com/catalog?filters%5Bkind%5D=group), [Users](https://allen.ingka.com/catalog?filters%5Bkind%5D=user) | Group is default, thus for User prefix with `user:`, see [Entity references](./overview.md#Entity-references). To create or alter membership of a group, check [IAM documentation](https://confluence.build.ingka.ikea.com/display/EKR234IA/Team+Groups+in+Azure+AD).                                                                                                                                    |
| `spec.type`                              | [`service`, `website`, `library`, `documentation`]                                                                                 |                                                                                                                                                                                                                                                                                                                                                                                                          |
| `spec.lifecycle`                         | [`emerging`, `production`, `experimental`, `deprecated`, `sunset`]                                                                 |                                                                                                                                                                                                                                                                                                                                                                                                          |
| `spec.system`                            | [Systems](https://allen.ingka.com/catalog?filters%5Bkind%5D=system)                                                                | If missing please initiate creation, see [Create a new system - quick guide](https://confluence.build.ingka.ikea.com/x/doQBGg).                                                                                                                                                                                                                                                                          |
| `spec.providesApis`, `spec.consumesApis` | [APIs](http://allen.ingka.com/api-docs)                                                                                            | The references describes which APIs the component provides (implements) and consumes. API catalogue is a central catalogue containing all Ingka business and system APIs. Note that event APIs (`asyncapi`) are in namespace `event-portal`, referenced like `event-portal/example-api-x`. Other types of APIs (such as `openapi`, `graphql`) can be referenced just with the name e.g. `example-api-y`. |

Note that `spec.system` should use the System Master Abbreviation property. You can find this by looking at the URL of a system such as https://allen.ingka.com/catalog/default/system/DEVPORT - `DEVPORT` is the abbreviation that should be set in `spec.system`.

For more in-depth details, see [Descriptor Format](https://backstage.io/docs/features/software-catalog/descriptor-format).

## How to add entities to the software catalog

In order to add entities to the software catalog, complete the following steps:

1. Create `catalog-info.yaml` entity descriptor file in the root of your GitHub repository
1. Go to [Catalog Import](https://allen.ingka.com/catalog-import)
1. Enter URL to the created entity file

The wizard analyzes the file, previews the entities, and on acknowledge adds them to the software catalog.

**Note:** If your repositories are on [GHES](https://git.build.ingka.ikea.com) you need to install the Allen GitHub app first to provide access to your repositories. You can do this by clicking on the below link and choosing the organization where it should be installed. You must be an owner of the organization.

GitHub app for Allen: https://git.build.ingka.ikea.com/github-apps/allen-developer-portal

GitHub app for Allen (Staging): https://git.build.ingka.ikea.com/github-apps/allen-developer-portal-staging

## Updating entity metadata

Teams owning the entities are responsible for maintaining the metadata about them, and do so using their normal git workflow. Once the change has been merged, Developer Portal will automatically refresh. It is also possibly to manually trigger an update.
