# Publish REST API in APIM Catalog

## [![](./../../images/pin.svg)](#publish-api-specification-document) Publish API Specification Document

APIM team offers [APIM Catalog API](https://allen.ingka.com/catalog/prod/api/apim-catalog-api-v2/definition) that API provider/owner use to deploy API to managed API Catalog.
It's important to remember if you are using central APIM gateway then you should not use this service to publish your API to Allen. In that case you need to follow [Managed gateway offering](https://allen.ingka.com/docs/default/component/apim-managed-api-gateway)

### Prerequisites:

- You have a valid OpenAPI specification file in github.com that describe your REST API. You need to use raw url of the specification file.
- You know the SMC system, MyIdentity team and data-concept that are applicable for the API
- You have documented API onboarding and API access related steps for API consumer in markdown files and uploaded it in github.com

### Deployment Steps

#### Get raw url of your API specification file and other markdown files.

Open the file in github.com and click on raw tab present in the right side and get the url till the string '?token'.

#### Get the Authorization header:

Use the 'ClientId' you received while onboarding.

#### Prepare the request body for API document publish:

You need to carefully form the requestbody for API deployment. Read the [APIM Catalog API](https://allen.ingka.com/catalog/prod/api/apim-catalog-api-v2/definition#/rest/publishSpec) for more details of each fields of request body

Below sample request body:

```
curl -X 'POST' \
  'https://api.ingka.ikea.com/apim/catalog/v2/apis/rest' \
  -H 'accept: */*' \
  -H 'Content-Type: application/json' \
  -H 'X-Client-Id: <CLient id received during onboarding>' \
  -d '{
  "specUrl": "<API spec in github raw url format>",
  "environment": "<environment>", // dev,stage or prod
  "onboardingDocUrl": "<Markdown file for API onboarding in github raw url format>",
  "apiAccessDocUrl": "<Markdown file for API access in github raw url format> ",
  "dataConceptName": "<Data Concept for the API>
}'

```

\*\*\*Note: If you will try to republish API specification document already published you will get error.For republishing API specification , you need to use not post but the patch operation.

```