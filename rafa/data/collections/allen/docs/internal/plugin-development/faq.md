# Frequently asked questions

### How to remove a plugin?

To remove a plugin:

1. Remove the plugin folder from `./plugins`
2. Remove the plugin from the `package.json `in `packages/app` and `packages/backend`
3. Remove any other code that references the plugin
4. Run `yarn install` to update the `yarn.lock` file
