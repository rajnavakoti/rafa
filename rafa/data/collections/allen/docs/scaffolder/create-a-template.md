# Create a template

- Official documentation - [Writing Templates](https://backstage.io/docs/features/software-templates/writing-templates/)

Templates are stored as entities in Allen's software catalog under a kind called `Template`. You can create your own templates with a small yaml descriptor file which describes the template and its metadata, along with some input variables that your template will need, and then a list of actions which are then executed by the scaffolding service.

A simple `template.yaml` descriptor file might look something like this:

```yaml
apiVersion: scaffolder.backstage.io/v1beta3
kind: Template
# some metadata about the template itself
metadata:
  name: demo-template
  title: Test Action template
  description: scaffolder template demo
spec:
  owner: my-team
  type: service

  # these are the steps which are rendered in the frontend with the form input
  parameters:
    - title: Fill in some steps
      required:
        - name
      properties:
        name:
          title: Name
          type: string
          description: Unique name of the component
          ui:autofocus: true
        owner:
          title: Owner
          type: string
          description: Owner of the component
          ui:field: OwnerPicker
          ui:options:
            catalogFilter:
              kind: Group
    - title: Choose a location
      required:
        - repoUrl
      properties:
        repoUrl:
          title: Repository Location
          type: string
          ui:field: RepoUrlPicker
          ui:options:
            # requestUserCredentials is mandatory, this will make use of the user's identity
            # when interacting with GitHub
            requestUserCredentials:
              secretsKey: USER_OAUTH_TOKEN
            allowedHosts:
              - github.com
            allowedOrganizations:
              - ingka-group-digital

  # here's the steps that are executed in series in the scaffolder backend
  steps:
    - id: fetch-base
      name: Generate template
      action: fetch:template
      input:
        url: ./template
        values:
          name: ${{ parameters.name }}
          owner: ${{ parameters.owner }}

    - id: publish
      name: Publish
      action: publish:github
      input:
        allowedHosts: ['github.com']
        description: This is ${{ parameters.name }}
        repoUrl: ${{ parameters.repoUrl }}
        token: ${{ secrets.USER_OAUTH_TOKEN }}

    - id: register
      name: Register
      action: catalog:register
      input:
        repoContentsUrl: ${{ steps['publish'].output.repoContentsUrl }}
        catalogInfoPath: '/catalog-info.yaml'

  # some outputs which are saved along with the job for use in the frontend
  output:
    links:
      - title: Repository
        url: ${{ steps['publish'].output.remoteUrl }}
      - title: Open in catalog
        icon: catalog
        entityRef: ${{ steps['register'].output.entityRef }}
```

- `spec.parameters` - `FormStep | FormStep[]`

The `spec.parameters` section defines the inputs required for your template. These inputs are then passed to the template and replaced in the generated files.

The inputs are presented as a sequence of steps in the frontend. Each step is a `JSONSchema` which defines the input fields which are rendered by the `react-jsonschema-form` library. You can find a lot of examples [here](https://rjsf-team.github.io/react-jsonschema-form/). You can also live edit your template by opening the [template editor](https://allen.ingka.com/scaffold/edit) and clicking "Edit Template Form".

Each field in the `JSONSchema` can also contain special `ui:*` properties which allow you to customize the input field. For example, you can set `ui:field: Secret` to render a field which masks the input and marks the value provided as sensitive, so it doesn't show up in the logs. You can find all custom input fields and their options in the [TemplateEditor](https://allen.ingka.com/scaffold/edit) and clicking "Custom Field Exporter".

Read the [official documentation](https://backstage.io/docs/features/software-templates/writing-templates/#specparameters---formstep--formstep) for more information.

- `spec.steps` - `Action[]`

The `spec.steps` array is a list of actions which are executed in series by the scaffolder backend. Each action is a separate step in the scaffolder job.

```yaml
- id: fetch-base # A unique id for the step
  name: Fetch Base # A title displayed in the frontend
  if: ${{ parameters.name }} # Optional condition, skip the step if not truthy
  each: ${{ parameters.iterable }} # Optional iterable, run the same step multiple times
  action: fetch:template # An action to call
  input: # Input that is passed as arguments to the action handler
    url: ./template
    values:
      name: ${{ parameters.name }}
```

You can find all available actions on the [Installed actions page](https://allen.ingka.com/scaffold/actions).

## Templating syntax

The Scaffolder templates use the [nunjucks])(https://mozilla.github.io/nunjucks/templating.html) library for the templating syntax.

To substitute variables in your templated files with an input from the user, you can do:

```txt filename="templated-file.txt"
Hello ${{ values.name }}
```

The `${{ values.name }}` string will be replaced with the input from the user. An example template descriptor file would be:

```yaml
apiVersion: scaffolder.backstage.io/v1beta3
kind: Template
metadata:
  name: v1beta3-demo
  title: Test Action
  description: scaffolder v1beta3 template demo
spec:
  owner: my-team
  type: service
  parameters:
    - title: Fill in some steps
      required:
        - name
      properties:
        name:
          title: Name
          type: string
          description: Unique name of your project
  ...
  steps:
    - id: fetch-base
      name: Fetch Base
      action: fetch:template
      input:
        url: ./template
        values:
          name: ${{ parameters.name }}
```

Notice that the `parameters` section defines the `name` property. This will make it render in the frontend as a text input field. Then the value of that input field is passed in the `fetch:template` action under `input.values`.

## Register the template

Once you have your template and the `template.yaml` descriptor file ready, you can register it in the Allen catalog. You do this by opening the Allen [catalog import](https://allen.ingka.com/catalog-import) page and passing it the url to your `template.yaml` file from your repository.
