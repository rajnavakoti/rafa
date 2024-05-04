# Migrating Get Access Cards to Platform

In this guide, we will walk you through the process of migrating Get Access Cards for your platform plugins.
This is an essential step to ensure the transition from Get-access to Platforms on Allen.
We will cover the prerequisites, the step-by-step migration process, and how to verify the success of the migration.

## Prerequisites

Ensure that the platform is onboarded using the [onboarding](./overview#onboarding) section.

## Illustration and examples

This guide includes examples that illustrate the migration process of the JFrog Get Access Cards.

## Plugin.ts file

The `plugin.ts` file in Backstage is the main entry point for a plugin. This file is where you define the plugin and any extensions it provides. You can find all your current GetAccess cards defined here.

## Migration Process

Follow these steps to migrate the Get Access Cards:

### 1. Identify Your Get Access Cards.

Get Access Cards are typically created using the `createWorkflowsRequestExtension` and then named and exported. Make a note of the names of the exported `workflowRequestExtensions`.

### 2. Create the Platform Extension.

1. Open the `plugin.ts` file.
2. Define a constant named `PLATFORM_NAME` and assign it the name of your platform. This name must match the `name` property in the platform yaml file.
3. Create a new Platform extension using the `createPlatform` function provided by the `platform` plugin, and export it.
   - Pass the `PLATFORM_NAME` constant as the name.
   - Pass the names of the `workflowRequestExtensions` (identified in the previous step) as an array to the `selfServiceExtensions` parameter.

#### Template code 1

```Typescript
const PLATFORM_NAME = '<Name_found_in_plaform_yaml>'
export const <plaform_extension_name> = esJfrogPlugin.provide(
  createPlatform({
    name: PLATFORM_NAME,
    selfServiceExtensions: [
      <WorkflowRequestExtension1>
      <WorkflowRequestExtension2>
      ...
    ],
  }),
);
```

#### Example with JFrog

In this example we will register the 2 Workflow Request Extensions

```typescript
const PLATFOMR_NAME = 'artifactory';

export const JfrogPlatformExtension = esJfrogPlugin.provide(
  createPlatform({
    name: PLATFOMR_NAME,
    selfServiceExtensions: [
      JFrogProjectCreateExtension,
      GenerateTokenExtension,
    ],
  }),
);
```

### 3. Exporting the Platform Extension from the plugin

Open the main `index.ts` in the plugin and add the exported platform extension.

```typescript
export {
<Your Plugin>,
<WorkflowRequestExtention1>, // <-- used by get access
<WorkflowRequestExtention2>, // <-- used by get acesss
<PlatformExtention> // <--- Add your new extention here
} from './plugin';

```

#### Example es-frog

```typescript
export {
  esJfrogPlugin,
  BecomeAdminExtension,
  JFrogRepoCreateExtension,
  JfrogPlatformExtension, // <--
} from './plugin';
```

### 4. Registering your platform Extensions

1. Navigate to the `App.tsx` file
2. Include your newly created platform extension in the `<PlatformsExtensions>` list. This list is located under the `/platforms` path.
   Refer back to [Step 3](#3-exporting-the-platform-extension-from-the-plugin) if you need a reminder on how to export the platform extension from the plugin.

#### Template Code 3

```html
  <Route path="/platforms" element={<PlatformsPage />}>
    <PlatformsExtensions>
      <Platform_extentions_1 />
      <Platform_extentions_2 />
      <Your_platform_extention /> //<-- add your extention
    </PlatformsExtensions>
  </Route>
```

#### Example es-jfrog

```html
    <Route path="/platforms" element={<PlatformsPage />}>
      <PlatformsExtensions>
        <GithubPlatformExtention />
        <JfrogPlatformExtension /> //<-- the newly imported one
      </PlatformsExtensions>
    </Route>
```

### 5. Verify the Migration

1. Run the server
2. Open your platform page.
3. Open the self-service tab and verify that if the Get Access cards are showing.

### 6. Redirecting the Get Access cards to self-service cards

1. Navigate to the plugins.ts file
2. Append the PLATFORM_NAME to createWorkflowsRequestExtension as the platform parameter.

This redirect your users from the get access page to your actual platform self service card.

#### Example Redirecting

```typescript
export const AddRepositoryToInstallationExtension = esGithubPlugin.provide(
  createWorkflowsRequestExtension({
    name: ....
    title: ....,
    component: ....
    tags: .... ,
    img: ....,
    supportInfo: ....,
    platform: PLATFORM_NAME, // <---
  }),
);
```
