## Accessing user data and info through the AppContext

When developing components throughout different plugins, quite often one needs to fetch
some info on the authenticated user and since this is a common practice we created this
`ingka-react` package that provides the `AppContext` which contains most of the things that are
shared between plugins.

To use the context as a first step you need to make sure to include the `ingka-react` package into your `package.json`. Then you can import it and use it with:

```typescript
import {
  AppContext,
  AppContextProps,
  AppContextUserSettings,
} from 'ingka-react';

const appContext = React.useContext<AppContextProps>(AppContext);

// The appContext.user object exposes the following attributes:
// appContext.user.mail - authenticated user's email address
// appContext.user.displayName - authenticated user's displayName
// appContext.user.givenName - authenticated user's givenName
// appContext.user.username - authenticated user's network id
// appContext.user.adGroups - authenticated user's ad groups
// appContext.user.memberOf - a list of relations to backstage entities
console.log(appContext.user);

// The appContext.userSettings object exposes the following attributes:
// appContext.userSettings.insightsDefaultGroup - The default group when rendering the team insights page
// appContext.userSettings.insightsAsLandingPage - If enabled team insights will be rendered as a landing page for the authenticated user
console.log(appContext.userSettings);

// The appContext.setUserSettings function lets you update/set the settings for the authenticated user
// NOTE: Currently the userSettings data is stored in the browser's local storage
const params = {
  insightsAsLandingPage: true,
  insightsDefaultGroup: 'my-group',
};
appContext.setUserSettings(params);

// The appContext.loading indicates whether or not the data has been loaded
console.log(appContext.loading);

// The appContext.error indicates whether or not there has been an error while trying to load the data
console.log(appContext.error);
```
