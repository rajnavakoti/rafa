# What is the Platform?

The [Platform Plugin](https://allen.ingka.com/platforms) is a powerful tool designed to enhance the developer experience on Allen. This plugin facilitates easy access to essential development tools such as GitHub, Vault, Kong, Artifactory and more. By onboarding tools seamlessly, developers can streamline their workflow and focus on building innovative solutions.
​

## Onboarding

The plugin utilizes a YAML configuration file to onboard products. Below is a template for the YAML file:
​

```yaml
apiVersion: ingka.com/v1alpha1
kind: Platform
metadata:
  title: API Gateway
  name: api-gateway
  description: An API gateway is an API management tool that sits between a client and a collection of backend services. It acts as a reverse proxy to accept all application programming interface (API) calls, aggregate the various services required to fulfill them, and return the appropriate result.
  links:
    - title: Slack Channel
      url: https://ikea.enterprise.slack.com/archives/CNSCXHH33
    - title: Support
      url: https://jira.digital.ingka.com/servicedesk/customer/portal/68
spec:
  lifecycle: production
  owner: es-core
  category: Integration
  subCategory: API Management
  overview: >
    # Introduction
     Kong Gateway is a lightweight, fast, and flexible cloud-native API gateway. An API gateway is a reverse proxy that lets you manage, configure, and route requests to your APIs.
​
    ## Key Features
     * Leverage workflow automation and modern GitOps practices
     * Decentralize applications/services and transition to microservices
     * Create a thriving API developer ecosystem
     * Proactively identify API-related anomalies and threats
     * Secure and govern APIs/services, and improve API visibility across the entire organization.
     * Check out learning labs at [Kong Academy](https://education.konghq.com/users)
```

### Properties

All below properties are mandatory in your `platform.yaml` file for Platform onboarding.

> Note: If the product doesn't exist in the [Technology Platforms in IRP](https://confluence.build.ingka.ikea.com/x/uWslKg) page, then it should be approved by the Enterprise Architecture.
> ​

- **apiVersion:** Specifies the version of the API for the Platform Plugin. You can keep the template value.
  ​
- **kind:** Represents the type of resource being created, it has to be "Platform". You can keep the template value
  ​
- **metadata:** Contains essential metadata about the platform, including title, name, description, and relevant links
  ​

  - **title**: Title of the product visible to the user.
  - **name:** Name of the product used for routing. It has to be skew case.
  - **description:** A brief description of the product to be displayed on the landing page.
  - **links:** A list of relevant links (e.g., Slack Channel, Jira Support)..
    ​

- **spec:** Encompasses specific details about the platform, such as lifecycle, owner, category, subcategory, and an overview.
  ​
  - **lifecycle:** It has to be one of these values: "`experimental`, `emerging`, `production`, `deprecated`, `sunset`, `retired`"
  - **owner:** Team name of the owner of the product.
  - **category:** Categories are predefined for the product.
  - **subCategory:** Subcategory based on the category of the product.
  - **imagePath:** Relative path of the image to the root of the repo.
  - **overview:** A brief overview of the product to be displayed on product details page. Overview is mandatory for all products

### Getting Started

​
To onboard Platforms, follow these steps:
​

> Note: If the Platforms plugin is not visible on Allen, check the "Feature Flags" tab under the Allen Settings.
> ​

1. Create a YAML file on the root path of your repo based on the provided template. e.g. `<platform>.yaml`.
   ​
2. Customize the metadata and specifications according to the product you want to onboard.

3. Add an image (.svg or .png format) of the product preferably within the same directory where `<platform>.yaml` file is located. (`imagePath` will be used to locate the image file)​
   ​
4. Copy the url link of the `<platform>.yaml` to clipboard.
   ​
5. Navigate to the **Register Component** section on Allen portal.
   ​
6. Paste the url into the **Select URL** input field. Click Analyze button.
   ​
7. Details of the product should be visible under **Review** step.
   ​
8. Click import.
   ​
9. Navigate to **Platforms** section and observe the product under the defined sub-category.
   ​
10. When you click on the product link, details of the product and the overview page should be visible.

Contact the [Support Slack Channel](https://ikea.enterprise.slack.com/archives/C066SDWE3L4) if any image size issues emerge.
​

### Possible errors

- Validation Errors:
  - Repo not created within [`ingka-group-digital`](https://github.com/ingka-group-digital)
  - Mandatory fields are not populated.
  - Category or subcategory mismatch
  - Yaml file is not under the root path
  - Product is already onboarded.
    ​

For any other errors please contact the [Support Slack Channel](https://ikea.enterprise.slack.com/archives/C066SDWE3L4)
