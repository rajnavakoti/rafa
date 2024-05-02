# Manage REST API in APIM Catalog

## [![](./images/pin.svg)](#table-of-contents) Table of contents

1. [Validate API Specification Document](#validate-api-specification-document)
2. [Publish API Specification Document](#publish-api-specification-document)
3. [Update API Specification Document](#update-api-specification-document)
4. [Delete API Specification Document](#delete-api-specification-document)
5. [FAQ](#faq)

## [![](./../../images/pin.svg)](#validate-api-specification-document) Validate API Specification Document

You can make delete to your API specification file,markdown files or change the data-concept in API Catalog.More information about it can be found here: [APIM Catalog API](https://allen.ingka.com/catalog/prod/api/apim-catalog-api-v2/definition#/Specifications/validateSpec)

Below sample request:

```
curl -X 'POST' \
  'https://api.ingka.ikea.com/apim/catalog/v2/specs/validate' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -H 'X-Client-Id: <CLient id received during onbaording>' \
  -d '{
  "specUrl": "https://raw.githubusercontent.com/ingka-group-digital/apim-consumer-org-service/development/src/api/apim-consumer-org-api.yaml"
}'

```

## [![](./../../images/pin.svg)](#update-api-specification-document) Update API Specification Document

You can make update to your API specification file,markdown files or change the data-concept in API Catalog.More information about it can be found here: [APIM Catalog API](https://allen.ingka.com/catalog/prod/api/apim-catalog-api-v2/definition#/rest/updateApiMeta).

Below sample request body:

```
curl -X 'PATCH' \
  'https://api.ingka.ikea.com/apim/catalog/v2/apis/rest' \
  -H 'accept: */*' \
  -H 'Content-Type: application/json' \
  -H 'X-Client-Id: <CLient id received during onbaording>' \
  -d '{
  "specUrl": "<API spec in github raw url format>",
  "environment": "<environement>", // dev,stage or prod
  "onboardingDocUrl": "<Markdown file for API onbaoridng in github raw url format>",
  "apiAccessDocUrl": "<Markdown file for API access in github raw url format> ",
  "dataConceptName": "<Data Concept for the API>
}'

```

## [![](./../../images/pin.svg)](#delete-api-specification-document) Delete API Specification Document

You can make delete to your API specification file,markdown files or change the data-concept in API Catalog.More information about it can be found here: [APIM Catalog API](https://allen.ingka.com/catalog/prod/api/apim-catalog-api-v2/definition#/rest/deleteSpec)

Below sample request:

```
curl -X 'DELETE' \
  -H 'accept: */*' \
  -H 'X-Client-Id: <CLient id received during onbaording>' \
  'https://api.ingka.ikea.com/apim/catalog/v2/apis/rest/apim-catalog-api/stage?version=1.0.0'

```

## [![](./../../images/pin.svg)](#faq) FAQ

Q1:
