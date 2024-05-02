<p align="center">
  <img width="25%" height="25%" src="./assets/logo.svg">
</p>

🔥 **Latest stable version**: v1.1.0 ([Florence](https://en.wikipedia.org/wiki/Florence) Edition)

🤔 For **questions** use [discussions page](https://github.com/ingka-group-digital/lint-asyncapi/discussions)

📃 For **new feature requests and bug reports** use [issues page](https://github.com/ingka-group-digital/lint-asyncapi/issues)

🙌 **Join our community on [#cop-api-standards](https://ingka.slack.com/archives/C0485JDACH1) channel!**

---

## How to use it?

### As a GitHub action

Add the following step to your GitHub workflow job:

> **_Recommendation:_** run it before publishing the API to Kong API Gateway

```yaml
- uses: ingka-group-digital/lint-asyncapi@v1.1.0
    with:
      files: |
        <file-1-path>
        <file-2-path>
```

### As a GitHub workflow

You can create a separate GitHub workflow to lint-asyncapi spec files:

> **_Recommendation:_** run it whenever a new change in the spec files is pushed

```yaml
name: Lint AsyncAPI files

on:
  workflow_dispatch:
  push:
    paths:
      - <spec-files-path>

jobs:
  lint-asyncapi:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repository
        uses: actions/checkout@v3

      - name: Lint AsyncAPI specifications
        uses: ingka-group-digital/lint-asyncapi@v1.1.0
        with:
          files: |
            <file-1-path>
            <file-2-path>
```

### As a CLI tool

You can run the linter locally by executing the package with `npx` and passing the path to a yaml AsyncAPI specification file.

> **_Recommendation:_** use as a CLI and pass the path to the AsyncAPI specification .yaml file

`npx @ingka-group-digital/lint-asyncapi ./examples/asyncapi-01.yaml`

### As an npm package

You can install the linter as npm package and run it in your own application, npm package is deployed in Ingka JFrog Artifactory. To install the npm package in your application need to follow below steps:

1. You need username and password to install and publish a module in Jfrog registry. you can request a username and auth token via [Allen](https://allen.ingka.com/get-access/jfrog-create-token)

2. Need to have an \_auth token which can be achived by running below command

```
curl -u {{ username }}:{{ password }} https://artifactory.build.ingka.ikea.com/artifactory/api/npm/auth

```

3. create a .npmrc file in the root of your application as below, replace the ${TOKEN} with \_auth token generated in above step.

```
always-auth = true
@ingka-group-digital:registry=https://artifactory.build.ingka.ikea.com/artifactory/api/npm/ingka-npm-shared-local/
//artifactory.build.ingka.ikea.com/artifactory/api/npm/ingka-npm-shared-local/:_auth=${TOKEN}
registry=https://registry.npmjs.com

```

3. to install the package run below command

```
npm install @ingka-group-digital/lint-asyncapi
```

4. import the module in your file and lint the asyncapi spec as below

```
import { asyncapiLint } from '@ingka-group-digital/lint-asyncapi';
const stringifiedAsyncApiSpec = `asyncapi: 2.6.0
info:
  title: Account Service
  version: 1.0.0
  description: This service is in charge of processing user signups :rocket:
channels:
  user/signedup:
    subscribe:
      message:
        $ref: '#/components/messages/UserSignedUp'
components:
  messages:
    UserSignedUp:
      payload:
        type: object
        properties:
          displayName:
            type: string
            description: Name of the user
          email:
            type: string
            format: email
`;
(async () => {
  const results = await asyncapiLint(stringifiedAsyncApiSpec);
 // do something with the results..
})();
```

> **_Recommendation:_** use as a JS module in your own application

## What is it?

`lint-asyncapi` is a GitHub action, CLI tool and npm package that helps you find problems with your AsyncAPI specification and ensure that it follows [INGKA API standards](https://github.com/ingka-group-digital/api-standards/blob/main/docs/EventAPI/README.md) maintained by API Management team.

## Why you need it?

- to make sure your AsyncAPI spec file follows [INGKA API standards](https://github.com/ingka-group-digital/api-standards/blob/main/docs/EventAPI/README.md);
- to automate AsyncAPI linting as part of your CI/CD pipeline;

## How it works?

This GitHub action runs a script on the provided AsyncAPI spec file. The script analyzes the file, checks it against list of rules and shows possible problems. Under the hood it uses `@stoplight/spectral-core` npm package for linting the file and configuring these rules.

> **_NOTE:_** Every rule has a `severity` property which defines the severity level of the problem if the assertion is false. Possible values are: `error`, `warn` and `info`.
>
> In case of a negative assertion:
>
> - If a rule uses `error` severity, the problem will be printed out and then the pipeline will fail.
> - If the rule uses `warn` severity, the problem will be printed out but the pipeline will continue.
> - If the rule uses `info` severity, the suggestion will be printed out but the pipeline will continue.

## Which rules are used in this action?

Current set of rules contains [recommended rules](https://docs.stoplight.io/docs/spectral/1e63ffd0220f3-async-api-rules) from the `spectral` package and the custom rules implemented on top of the recommended ones. Both of them together form the rules which conform [INGKA API standards](https://github.com/ingka-group-digital/api-standards/blob/main/docs/EventAPI/README.md) provided by the EVENTM team. All rules are listed in [asyncapiRulset](src/asyncapiRulset.ts) under the `rules` property.

### Recommended rules (34)

| Rule                                        | Severity | Description|
| ------------------------------------------- | -------- | ----------------------------------------------------------------------------------- |
| `asyncapi-channel-no-empty-parameter`       | error    | Channel parameter declarations cannot be empty. [Read more](https://docs.stoplight.io/docs/spectral/1e63ffd0220f3-async-api-rules#asyncapi-channel-no-empty-parameter)                                                                                                                  |
| `asyncapi-channel-no-query-nor-fragment`    | error    | Query parameters and fragments shouldn't be used in channel names. [Read more](https://docs.stoplight.io/docs/spectral/1e63ffd0220f3-async-api-rules#asyncapi-channel-no-query-nor-fragment)                                                                                            |
| `asyncapi-channel-no-trailing-slash`        | error    | Keep trailing slashes off of channel names, as it can cause some confusion. [Read more](https://docs.stoplight.io/docs/spectral/1e63ffd0220f3-async-api-rules#asyncapi-channel-no-trailing-slash)                                                                                       |
| `asyncapi-channel-parameters`               | error    | All channel parameters should be defined in the parameters object of the channel. [Read more](https://docs.stoplight.io/docs/spectral/1e63ffd0220f3-async-api-rules#asyncapi-channel-parameters)                                                                                        |
| `asyncapi-channel-servers`                  | warn     | Channel servers must be defined in the servers object. [Read more](https://docs.stoplight.io/docs/spectral/1e63ffd0220f3-async-api-rules#asyncapi-channel-servers)                                                                                                                      |
| `asyncapi-headers-schema-type-object`       | error    | The schema definition of the application headers must be of type “object”. [Read more](https://docs.stoplight.io/docs/spectral/1e63ffd0220f3-async-api-rules#asyncapi-headers-schema-type-object)                                                                                       |
| `asyncapi-info-contact-properties`          | warn     | The asyncapi-info-contact rule will ask you to put in a contact object, and this rule will make sure it's full of the most useful properties: name, url, and email. [Read more](https://docs.stoplight.io/docs/spectral/1e63ffd0220f3-async-api-rules#asyncapi-info-contact-properties) |
| `asyncapi-info-contact`                     | error    | Info object should contain contact object. [Read more](https://docs.stoplight.io/docs/spectral/1e63ffd0220f3-async-api-rules#asyncapi-info-contact)                                                                                                                                     |
| `asyncapi-info-description`                 | error    | AsyncAPI object info description must be present and non-empty string. [Read more](https://docs.stoplight.io/docs/spectral/1e63ffd0220f3-async-api-rules#asyncapi-info-description)                                                                                                     |
| `asyncapi-info-license-url`                 | info     | Mentioning a license is only useful if people know what the license means, so add a link to the full text for those who need it. [Read more](https://docs.stoplight.io/docs/spectral/1e63ffd0220f3-async-api-rules#asyncapi-info-license-url)                                           |
| `asyncapi-info-license`                     | warn     | The info object should have a license key. [Read more](https://docs.stoplight.io/docs/spectral/1e63ffd0220f3-async-api-rules#asyncapi-info-license)                                                                                                                                     |
| `asyncapi-latest-version`                   | info     | Checking if the AsyncAPI document is using the latest version. [Read more](https://docs.stoplight.io/docs/spectral/1e63ffd0220f3-async-api-rules#asyncapi-latest-version)                                                                                                               |
| `asyncapi-message-examples`                 | warn     | All examples in message object should follow payload and headers schemas. [Read more](https://docs.stoplight.io/docs/spectral/1e63ffd0220f3-async-api-rules#asyncapi-message-examples)                                                                                                  |
| `asyncapi-operation-description`            | warn     | Operation objects should have a description. [Read more](https://docs.stoplight.io/docs/spectral/1e63ffd0220f3-async-api-rules#asyncapi-operation-description)                                                                                                                          |
| `asyncapi-operation-operationId-uniqueness` | error    | OperationId must be unique across all the operations (except the ones defined in the components). [Read more](https://docs.stoplight.io/docs/spectral/1e63ffd0220f3-async-api-rules#asyncapi-operation-operationId-uniqueness)                                                          |
| `asyncapi-operation-operationId`            | error    | Operation ID is essentially a reference for the operation and it must be present. [Read more](https://docs.stoplight.io/docs/spectral/1e63ffd0220f3-async-api-rules#asyncapi-operation-operationId)                                                                                     |
| `asyncapi-operation-security`               | info     | Operation security values must match a scheme defined in the components.securitySchemes object. [Read more](https://docs.stoplight.io/docs/spectral/1e63ffd0220f3-async-api-rules#asyncapi-operation-security)                                                                          |     | `asyncapi-payload-default` | error | default objects should be valid against the payload they decorate. [Read more](https://docs.stoplight.io/docs/spectral/1e63ffd0220f3-async-api-rules#asyncapi-payload-default) |
| `asyncapi-payload-examples`                 | error    | Values of the examples array should be valid against the payload they decorate. [Read more](https://docs.stoplight.io/docs/spectral/1e63ffd0220f3-async-api-rules#asyncapi-payload-examples)                                                                                            |
| `asyncapi-payload-unsupported-schemaFormat` | info     | Explicitly setting schemaFormat is not supported by Spectral, so if you use it this rule will emit an info message and skip validating the payload. [Read more](https://docs.stoplight.io/docs/spectral/1e63ffd0220f3-async-api-rules#asyncapi-payload-unsupported-schemaFormat)        |
| `asyncapi-payload`                          | error    | When schemaFormat is undefined, the payload object should be valid against the AsyncAPI 2 Schema Object definition. [Read more](https://docs.stoplight.io/docs/spectral/1e63ffd0220f3-async-api-rules#asyncapi-payload)                                                                 |
| `asyncapi-schema-default`                   | error    | Default objects should be valid against the schema they decorate. [Read more](https://docs.stoplight.io/docs/spectral/1e63ffd0220f3-async-api-rules#asyncapi-schema-default)                                                                                                            |
| `asyncapi-schema-examples`                  | error    | Values of the examples array should be valid against the schema they decorate. [Read more](https://docs.stoplight.io/docs/spectral/1e63ffd0220f3-async-api-rules#asyncapi-schema-examples)                                                                                              |
| `asyncapi-schema`                           | error    | Validate structure of AsyncAPI v2 specification. [Read more](https://docs.stoplight.io/docs/spectral/1e63ffd0220f3-async-api-rules#asyncapi-schema)                                                                                                                                     |
| `asyncapi-server-no-empty-variable`         | error    | Server URL variable declarations cannot be empty. [Read more](https://docs.stoplight.io/docs/spectral/1e63ffd0220f3-async-api-rules#asyncapi-server-no-empty-variable)                                                                                                                  |
| `asyncapi-server-no-trailing-slash`         | warn     | Server URL should not have a trailing slash. [Read more](https://docs.stoplight.io/docs/spectral/1e63ffd0220f3-async-api-rules#asyncapi-server-no-trailing-slash)                                                                                                                       |
| `asyncapi-server-not-example-com`           | warn     | Server URL should not point to example.com. [Read more](https://docs.stoplight.io/docs/spectral/1e63ffd0220f3-async-api-rules#asyncapi-server-not-example-com)                                                                                                                          |
| `asyncapi-server-security`                  | warn     | Server security values must match a scheme defined in the components.securitySchemes object. [Read more](https://docs.stoplight.io/docs/spectral/1e63ffd0220f3-async-api-rules#asyncapi-server-security)                                                                                |
| `asyncapi-server-variables`                 | warn     | All server URL variables should be defined in the variables object of the server. [Read more](https://docs.stoplight.io/docs/spectral/1e63ffd0220f3-async-api-rules#asyncapi-server-variables)                                                                                          |
| `asyncapi-servers`                          | warn     | A non-empty servers object is expected to be located at the root of the document. [Read more](https://docs.stoplight.io/docs/spectral/1e63ffd0220f3-async-api-rules#asyncapi-servers)                                                                                                   |
| `asyncapi-tag-description`                  | info     | Tags alone are not very descriptive. Give folks a bit more information to work with. [Read more](https://docs.stoplight.io/docs/spectral/1e63ffd0220f3-async-api-rules#asyncapi-tag-description)                                                                                        |
| `asyncapi-tags-uniqueness`                  | warn     | Tags must not have duplicate names (identifiers). [Read more](https://docs.stoplight.io/docs/spectral/1e63ffd0220f3-async-api-rules#asyncapi-tags-uniqueness)                                                                                                                           |
| `asyncapi-tags`                             | warn     | AsyncAPI object should have non-empty tags array. [Read more](https://docs.stoplight.io/docs/spectral/1e63ffd0220f3-async-api-rules#asyncapi-tags)                                                                                                                                      |
| `asyncapi-unused-components-schema`         | warn     | Potential unused reusable schema entry has been detected. [Read more](https://docs.stoplight.io/docs/spectral/1e63ffd0220f3-async-api-rules#asyncapi-unused-components-schema)                                                                                                          |
| `asyncapi-unused-components-server`         | warn     | Potential unused reusable server entry has been detected. [Read more](https://docs.stoplight.io/docs/spectral/1e63ffd0220f3-async-api-rules#asyncapi-unused-components-server)                                                                                                          |

### Custom rules (10)

| Rule                                            | Severity | Description                                                                                                                                                                                                                                | Implemented |
| ----------------------------------------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| `custom-info-description`                       | error    | Write a well formatted brief description of your API with atleast 30 char long.                                                                                                                                                            | yes         |
| `custom-info-title`                             | error    | title should not be empty.                                                                                                                                                                                                 | yes         |
| `custom-info-version`                           | error    | Version must be present and follow sementic versioning.                                                                                                                                                                                    | yes         |
| `custom-info-contact-email`                     | error    | email must be present inside contact object(preferred group emailId)                                                                                                                                                                       | yes         |
| `custom-channel-name`                           | error    | Follow naming standard for Topic. [Read more](https://allen.ingka.com/docs/default/component/api-standards/EventAPI/topic-naming-standards/)                                                                                               | no          |
| `custom-channel-name`                           | error    | If specified, Topic Properties are necessary for a particular type messaging broker or platform. [Read more](https://allen.ingka.com/docs/default/component/api-standards/EventAPI/#platform-specific-standards)                           | no          |
| `custom-component-message`                      | warn     | Always provide event version as major version only.                                                                                                                                                                                        | no          |
| `custom-component-schema`                       | error    | Always provide Schema version as major.minor version only.                                                                                                                                                                                 | no          |
| `custom-channel-x-ingka-attributes-visibility`  | error    | Each event must use `x-ingka-attributes.visibility` and value must be one of: ['private', 'ikea-internal', 'ikea-partner', 'ingka-internal']. [Read more](https://allen.ingka.com/docs/default/component/api-standards/common/visibility/) | no          |
| `custom-channel-x-ingka-attributes-reusability` | error    | Each event must use `x-ingka-attributes.reusability` and value must be one of: ['business', 'system', 'single-purpose']. [Read more](https://allen.ingka.com/docs/default/component/api-standards/common/reusability/)                     | no          |
| `custom-channel-x-ingka-attributes-status`      | error    | Each event must use `x-ingka-attributes.status` and value must be one of: ['draft', 'published', 'deprecated', 'retired']. [Read more](https://allen.ingka.com/docs/default/component/api-standards/common/lifecycle/)                     | no          |
| `custom-component-header`                       | error    | Use hyphenated header parameters.                                                                                                                                                                                                          | no          |

## How to add and configure existing rules?

You can use any rule which comes out of the box of `spectral` package. Full list of those rules may be found [here](https://docs.stoplight.io/docs/spectral/1e63ffd0220f3-async-api-rules). In order to override the severity of the rule which is being added via the `recommended` config, simply add it to the [asyncapiRulset.ts](src/asyncapiRulset.ts) under the `rules` property like this:

```typescript
// src/asyncapiRulset.ts

export default {
  ...
  rules: {
    // Overriding severity of the rule from the recommended config
    'asyncapi-info-description': 'error',
  }
}
```

## How to create custom rules?

In order to create custom rules you can:

- create custom rule with spectral built-in assertion functions;
- create custom assertion functions (if built-in functions do not fulfill the required functionality);

Below you may find an example of a custom rule, which uses both spectral built-in functions and custom functions:

```typescript
// src/asyncapiRuleset.ts

import { defined } from '@stoplight/spectral-functions';

export default {
  ...
  rules: {
    // The rule ID should be unique, meaningful and start with a `custom-` prefix.
    'custom-info-version': {
      // `message` is the problem message that will be shown in case the assertion is false.
      message: 'Version must be present and follow semantic versioning.',
      // `severity` helps to define the importance of following the rule.
      severity: 'error',
      // `given` tells Spectral which part of the JSON or YAML file to target by using JSONPath (Spectral uses JSONPath Plus).
      given: '$.info',
      // `then` specifies which properties of the `given` object should be validated and which assertion to use.
      then: [
        {
          // `field` is the property within the path (defined by property `given`) which custom rule should assert.
          field: 'version',
          // `function` contains an assertion which will be used against the `field`.
          // Spectral has a set of built-in assertion functions such as `truthy` or `pattern`,
          // which can be used when validating the `field`.
          // Here we are using a built-in `defined` assertion.
          // These functions can be imported from the `@stoplight/spectral-functions` package.
          function: defined,
        },
      ],
    },
  }
}
```

Custom assertion functions can be passed in `function` property same as spectral built-in functions. An example of a custom function implementation is shown below:

```typescript
// src/functions/fieldLength.ts

export function fieldLength(input: string, options: { min: number }): object[] {
  // Condition is handled in spectral standard rules so it's better to leave it.
  if (!input) {
    return [];
  }

  if (input.length < options.min) {
    // Return a problem because assertion is false.
    return [
      {
        message: `Write a well formatted brief description of your API with at least 30 char long.`,
      },
    ];
  }

  return [];
}
```

### :key: dependabot

By default, this action uses the `dependabot`

As described in the [official GitHub documentation](https://github.com/dependabot/dependabot-core):

> When you use the repository's dependabot finds and fixes vulnerabilities in your dependencies

### :key: release drafter

By default, this action uses the `release drafter`

As described in the [official GitHub documentation](https://github.com/marketplace/actions/release-drafter):

> When you use the repository's release drafter automatically creates a draft release on merge to main

### :pray: If you would like to contribute ?

1. Start a `discussion`
2. Create an `issue` with `feature request` or `bug` label
3. Clone and branch out
4. Push and create a PR

[Please follow this link to know more](https://github.com/ingka-group-digital/lint-asyncapi)
