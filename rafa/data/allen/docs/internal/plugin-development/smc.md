# System Master Catalog APIs

Allen is subscribed to the System Master Catalog Business APIs and you can call them from your plugin.

## Frontend plugin

1. Add `plugin-ingka-smc` to your plugin's `package.json`.

2. Use the `smcApiRef` in your React component:

```ts
const smcApi = useApi(smcApiRef);

// ...

const { value, error, loading } = useAsync(async () => {
  return await smcApi.getSystem('ARTFACT');
});
```

## Backend plugin

1. Add `plugin-ingka-smc-common` to your plugin's `package.json`.

2. Construct an instance of `SmcClient` in your router or in any place where you want to use it:

```ts
// options.config contains the config passed to the backend plugin
const smcApi = SmcClient.fromConfigForBackend(options.config);

// ...

// Use the smcApi to fetch data
const systems = await smcApi.getSystems();
```

**NOTE**: All systems from SMC are already ingested into Allen's catalog, so unless you have a good reason for interacting with the SMC APIs directly, you should make use of the `catalogApiRef` to fetch systems as needed.
