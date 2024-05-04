# Development

## Getting started

1. Read the official Backstage documentation
1. File structure
1. Set up your development environment
1. Clone the repository
1. Run an initial build
1. Run the project
1. Iterating

### Official Backstage documentation

You may find these resources helpful to learn more about Backstage which is the framework we use to develop Allen. The main parts are:

- [Overview](https://backstage.io/docs/overview/what-is-backstage)
- [Getting Started](https://backstage.io/docs/getting-started/)
- [Software Catalog](https://backstage.io/docs/features/software-catalog/software-catalog-overview)
- [Plugins](https://backstage.io/docs/plugins/)
- [Architecture Decision Records](https://backstage.io/docs/architecture-decisions/adrs-overview)

### File structure

- [packages/app](./packages/app) contains the code for the Backstage app. The Backstage app is used to configure the plugins and any global configuration.
- [packages/backend](./packages/backend) contains the code for the backend. The backend is used to configure and initialize the backend plugins.
- [plugins/](./plugins) contains code for the various plugins that we are building.

### Setup your development environment

You need to install these tools:

- [git](https://docs.github.com/en/github/getting-started-with-github/set-up-git)
- [Node.js](https://nodejs.org/en/) - Install the v18 LTS release
- [yarn](https://yarnpkg.com/getting-started/install)

#### Editor setup

It's recommended to use [Visual Studio Code](https://code.visualstudio.com/).

Install the following extensions:

- [EditorConfig](https://marketplace.visualstudio.com/items?itemName=EditorConfig.EditorConfig)
- [Prettier](https://open-vsx.org/extension/esbenp/prettier-vscode)
- [YAML](https://open-vsx.org/vscode/item?itemName=redhat.vscode-yaml)
- [ESLint](https://open-vsx.org/vscode/item?itemName=dbaeumer.vscode-eslint)

### Clone the repository

```console
git clone git@github.com:ingka-group-digital/developer-portal.git
cd developer-portal
```

### Local configuration and overrides

For local configuration and overrides, create a file `app-config.local.yaml` in the root of the project. Managing configurations in that file, being git ignored, reduces the risk of accidentally pushing sensitive configuration on editing `app-config.yaml` directly.

On running `yarn dev`, the `app-config.local.yaml` file is merged with `app-config.yaml`.

If you plan to work on a specific plugin, make sure you read the plugin's README file for any additional configurations that may be needed.

#### Microsoft OAuth SSO (mandatory)

By default required since it is the main authentication mechanism for Allen.

Add to `app-config.local.yaml`:

```
auth:
  environment: development
  providers:
    microsoft:
      development:
        clientId: <client-id>
        clientSecret: <client-secret>
        tenantId: <tenant-id>
```

Ask on [developer portal slack channel](#dt-developer-portal-dev) for your set of credentials.

??? info "(Optional) Github.com OAuth"

    Required if you want to access github.com from within Allen, e.g. component entity pages.

    This is used to configure the GitHub OAuth App to enable authentication through github.com. Create a personal [OAuth App](https://docs.github.com/en/developers/apps/creating-an-oauth-app) and set the following:

    - Application name: `<any name>`
    - Homepage URL: `<any url>`
    - Authorization callback URL: `http://localhost:7000/api/auth/github`

    Add to `app-config.local.yaml` (in `.auth.providers`)

    ```
    github:
      development:
        clientId: <client-id>
        clientSecret: <client-secret>
    ```

??? info "(Optional) GitHub Enterprise Server OAuth"

    Required if you want to access git.build.ingka.ikea.com from within Allen, e.g. component entity pages.

    This is used to configure the GitHub OAuth App to enable authentication through git.build.ingka.ikea.com. Create a personal [OAuth App](https://docs.github.com/en/developers/apps/creating-an-oauth-app) and set the following:

    - Application name: `<any name>`
    - Homepage URL: `<any url>`
    - Authorization callback URL: `http://localhost:7000/api/auth/ghe`

    Add to `app-config.local.yaml` (in `.auth.providers`)

    ```
    ghe:
      development:
        clientId: <client-id>
        clientSecret: <client-secret>
        enterpriseInstanceUrl: https://git.build.ingka.ikea.com
    ```

??? info "(Optional) GitHub tokens"

    Required if you want to ingest `catalog-info.yaml` files from git.build.ingka.ikea.com and/or github.com.

    The software catalog feature of Allen uses GitHub personal access tokens to access repositories that you want to import from and then scan those that have been imported. Create a personal access token in both https://github.com and https://git.build.ingka.ikea.com with the following scopes: `repo`, `read:user`, `user:email` and `read:org`. Make sure you "enable SSO" for the github.com access token and authorize the 'ingka-group-digital' organization.

    Add to `app-config.local.yaml`

    ```
    integrations:
      github:
        - host: github.com
          token: <github-token>
        - host: git.build.ingka.ikea.com
          apiBaseUrl: https://git.build.ingka.ikea.com/api/v3
          token: <ghes-token>
    ```

#### Populating the catalog with data

Populating the catalog with entities like systems, domains, data concepts, etc. is easiest done by manually copying a few entities and adding them locally.

1. Add the following to your local `app-config.local.yaml`:

```
catalog:
  rules:
    - allow:
        [
          Component,
          Resource,
          Location,
          ComponentTemplate,
          Template,
          Group,
          System,
          Domain,
          User,
          API,
        ]
  locations:
    - type: file
      target: ../../entities.yaml
```

2. Create a new file called `entities.yaml` at the root of the repository
3. Choose any entity from the Allen's catalog, e.g. [DEVPORT system](https://allen.ingka.com/catalog/default/system/devport)
4. Copy the entity descriptor yaml
   1. Expand the three-dots menu on the top right
   2. Click "inspect entity"
   3. Click on "Raw YAML"
5. Paste the contents in the `entities.yaml` file locally

All entities that you add to the `entities.yaml` file will be automatically registered once you start Allen locally. You can add all kinds of entity from the catalog and edit them as needed for local development.

##### (Optional) Entity providers

Entity providers are integrations with external systems to populate the Allen catalog with data from those external systems. Example, we populate all of our System and Domain entities from Ingka's System Master Catalog.

To enable Allen's entity providers, expand the needed sections.

??? info "SMC entity provider"

    In order to fill the catalog with real data from System Master Catalog you need to follow the below steps. After you have done this, you might need to restart the application and after a few minutes, data from SMC should be visible in the UI on the catalog page. Note that the header on the catalog page acts as a dropdown and you can change it to view different categories of data.

    - Create a personal IAM APP in [APP Management](https://allen.ingka.com/catalog/default/api/software-systems/onboarding) in the "Auth0 test" environment.

    - Add to `app-config.local.yaml`

    ```
    catalog:
      entityProviders:
        SMCProvider: {}

    smc:
      baseUrl: https://api.ingka.ppe.ikeadt.com
      auth:
        tokenUrl: https://testicow.accounts.ingka.com/oauth/token
        clientId: <client-id>
        clientSecret: <client-secret>
        audience: https://api.ingka.ppe.ikeadt.com

    ```

    - Replace `<client-id>` and `<client-secret>` with the credentials from the IAM APP.

??? info "Ingka Teams and Users entity providers"

    In order to fill the catalog with Ingka teams and their members you need to follow the below steps. After you have done this, you might need to restart the application and after a few minutes, the Groups and Users should be visible in the UI on the catalog page. Note that the header on the catalog page acts as a dropdown and you can change it to view different categories of data.

    - Add to `app-config.local.yaml`

    ```
    catalog:
      entityProviders:
        IngkaTeamsProvider:
          clientId: <client-id>
          clientSecret: <client-secret>
          tenantId: <tenant-id>
          filter: startswith(displayName, 'IAM_AAD_Team_')

        IngkaUsersProvider: {}

    ingkaAzureAdClient:
      clientId: <client-id>
      clientSecret: <client-secret>
      tenantId: <tenant-id>
    ```

    - Replace `<client-id>`, `<client-secret>` and `<tenant-id>` with the credentials for the Microsoft OAuth SSO.

??? info "Data Concepts entity provider"

    In order to fill the catalog with real data from Data Catalog you need to follow the below steps. After you have done this, you might need to restart the application and after a few minutes, data from the Data Catalog should be visible in the UI on the catalog page. Note that the header on the catalog page acts as a dropdown and you can change it to view different categories of data.

    - Create a personal IAM APP in [APP Management](https://allen.ingka.com/apim/app-management) in the "Auth0 production" environment.

    - Add to `app-config.local.yaml`

    ```
    catalog:
      entityProviders:
        DataConceptsProvider: {}

    allen:
      eiamApp:
        tokenUrl: https://icow.accounts.ingka.com/oauth/token
        clientId: <client-id>
        clientSecret: <client-secret>
        audience: https://api.ingka.ikea.com
    ```

    - Replace `<client-id>` and `<client-secret>` with the credentials from the IAM APP.

### Build

Install dependencies and run an initial build.

```console
yarn install
yarn tsc
yarn build:all
```

### Run

To run the project for development, run this command:

```console
LOG_LEVEL=debug \
NODE_ENV=development \
yarn dev
```

Make sure you have added needed [local configurations](#local-configuration-and-overrides).

### Iterating

`yarn dev` starts a development server that will auto-reload your changed files. This works only for existing files and not new files or the configuration file.

`yarn tsc` runs the TypeScript compiler. Running this command will check the types that you are using in your code.

`yarn test` runs the tests that have been changed since `origin/main`.

`yarn test:all` runs all tests.

`yarn lint` runs the linter.

`yarn prettier:check` runs Prettier to check for code style issues. You can fix all code style issues by running `yarn prettier:fix`.

### Upgrading backstage version

Backstage is still at a very early stage of development and there are a lot of breaking changes in between versions, so the upgrades are performed in a few manual steps.

Check out [Meld](https://meldmerge.org/) as it is a useful tool when comparing diffs.

To get the correct versions of all dependencies, type `yarn list --depth=1 | grep @backstage.` in the upstream repository.
