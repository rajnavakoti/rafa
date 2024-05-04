<h1 align="center" style="display: block; font-size: 2.5em; font-weight: bold; margin-block-start: 1em; margin-block-end: 1em;">
  <br><br><strong>Managed API Catalog</strong>
</h1>

## [![](./images/pin.svg)](#table-of-contents) Table of contents

1. [What we offer](#what-we-offer)
2. [User API Specification Document Management Journey](#users-api-specification-document-management-journey)

---

## [![](./images/pin.svg)](#what-we-offer) What we offer

- Allow API owner to deploy and manage their API in managed API catalog which is visualised by Allen. Follow 'Managed API Gateway' if you want to use managed API gateway offering by APIM team. You can't use same API for both use cases.
- Allow user to manage the lifecycle of their API
- Calculate and visualise API compliance score in Allen for all API based on 'Ingka API standards'

---

## [![](./images/pin.svg)](#users-api-specification-document-management-journey) User API Specification Document Management Journey

<div align="center">
    <img src="images/api-catalog-flow.png">
</div>

### Onboarding & API Designing

This is the very 1st step for your managed API Catalog journey as an API Provider. Please note that if you are using Managed API gateway (kong) then you can handle all catalog management related process there. The scope if this onboarding is for those teams who don't use managed API gateway

<details><summary> <h4> Onboard to managed API platform </h4></summary>
<p>
This is an one time activity for each team as an API provider. Before you would able to access any service related to 'Managed API Catalog' you need to onboard your team. Onboarding to APIM is a self service offering. Click here to <a href="https://allen.ingka.com/catalog/default/api/apim-catalog-api-v2/access-api">get onboarded</a>

<p>
<b>Prerequisites:</b>
<ul>
  <li>Know the <a href="https://confluence.build.ingka.ikea.com/pages/viewpage.action?spaceKey=SYSCAT&title=System+Master+Catalog+Home">SMC system</a></li>
  <li>Know your myidentity <a href="https://allen.ingka.com/catalog?filters%5Bkind%5D=group&filters%5Buser%5D=all">team</a>. If not present already create a new and add members</li>
</ul>
</p>
<p>
<p>
<b>Outcomes:</b>
</p>
You would get a clientId. You need to use this token while using <a href="https://allen.ingka.com/catalog/prod/api/apim-catalog-api-v2/definition">catalog management API</a> for API providers.
</p>
<p>
<a href="https://allen.ingka.com/docs/default/component/apim-managed-api-gateway/onborading/onboarding/">Know more</a>
</p>
</details>

<details><summary> <h4> Design API </h4></summary>
<p>
Do it at your own way but follow Ingka API design guideline. Please follow the below know how link to know more about it. 
</p>
<p>
<b>Outcomes:</b>
</p>
A well described API specification which is aligned to Ingka API standards.
<p>
<a href="https://allen.ingka.com/docs/default/component/apim-managed-api-gateway/design_api/rest/rest/">Know more</a>
</p>
</details>

<details><summary> <h4> Validate API specification </h4></summary>
<p>
Once the API specification is created now it's time to validate it. Use the lininting tool for validating your API specification based of predefined rule set. Try to fix all issues before you jump to next steps.
Please note that when you publish the specification it would get validated against the <a href="https://github.com/ingka-group-digital/api-standards">Ingka API Standards</a> and generate a compliance score. The compliance score would be visible in Allen
</p>
<p>
<b>Outcomes:</b>
</p>
An API specification which is valid based to Ingka API standards and ready to Publish can be validated in 3 different ways:
<ul>
  <li>Github action</li>
  <li>CLI</li>
  <li>npm package</li>
</ul>

You can know about this more <a href="https://allen.ingka.com/docs/default/component/apim-managed-api-gateway/design_api/rest/rest/">here</a>.

<p>
<p>
We also have dedicated endpoints in our APIM Catalog API to validate your API specification document.

<a href="https://allen.ingka.com/docs/default/component/apim-catalog/manage_api/rest/rest/">Know how: Validate Your REST API Document</a>

</p>
</p>
</details>

### API Document Publish

Once you are onboarded and owns a valid API specification now you are ready for the next steps i.e. Publish of API document to the 'Managed API Catalog'.

<details><summary> <h4> Publish API Document  </h4></summary>
<p>
APIM team offers a management API called 'APIM Catalog API' for API catalog related activities. You need to use the apiKey (the clientId, that you received in on-baording steps) for authentication to the API.
<p>
<b>Prerequisites:</b>

<ul>
  <li>Know the SMC system for the API</li>
  <li>Know the myidentity owner of the API</li>
  <li>Know the data concept of the API</li>
  <li>Upload the API specification file in github.com</li>
  <li>Upload user onbaording and access management related documentation (in markdown format) github.com</li>
</ul>
</p>
<p>
<p>
<b>Outcomes:</b>
</p>
 If the API pubslishing is successful, then the API specification will be published to the <a href="https://allen.ingka.com/api-docs">Allen</a>.
</p>
<p>
<a href="https://allen.ingka.com/docs/default/component/apim-catalog/manage_api/rest/rest/">Know how: Publish Your REST API Document</a>
</p>
</details>
<details><summary> <h4> Verify API Document Publish </h4></summary>
<p>
<ul>
  <li>Verify if the specification is visible in <a href="https://allen.ingka.com/api-docs">Allen</a> and it has right metadata like system,owner, dataconcept etc</li> 
  <li>Verify all consumer centric markdown files related to onboarding and access are visible properly in Allen</li>
</ul>
</p>
<p>
<b>Outcomes:</b>
</p>
An API which is ready to be invoked by consumer and pubslished API specification, ready to be discovered by Allen users.
</details>

### API specification and metadata management

Over the time API Providers need to re-publish API document,update API document, delete API document.

<details><summary> <h4> Update API document </h4></summary>
<p>

APIM Catalog API provides you dedicated end-point to update your API specification file, Markdown files and metadata like:data-cocept

</p>
<p>
Please refer the link to know how to do this :
<a href="https://allen.ingka.com/docs/default/component/apim-catalog/manage_api/rest/rest/"> Update API document</a>
</p>
</details>
<details><summary> <h4> Delete API document </h4></summary>
<p>
APIM Catalog API provides you dedicated end-point to delete your API specification file, Markdown files and metadata like:data-cocept

</p>
<p>
Please refer the link to know how to do this :
<a href="https://allen.ingka.com/docs/default/component/apim-catalog/manage_api/rest/rest/">Delete API document</a>
</p>
</details>
<details><summary> <h4> Understand  API Compliance Indicator </h4></summary>
<p>

<ul>
  <li>API Management and Event management teams are working with different engineering domains to bring acceptable API standards for both 'Web API' and 'Async API'. The outcome of such engagement is API standards and best practices which are written and maintained in [Ignka API Standards](https://github.com/ingka-group-digital/api-standards).</li> 
  <li>The engaged community also worked on a [linting tool](https://github.com/ingka-group-digital/lint-openapi) that encapsulated all the rules, which are possible of validate and then validate one API specification in different stages of API development and deployment lifecycle.</li>
  <li>Based on API standard and linting tool rules API Management team scores each of the API publshes in API-Catalog and shows the result also to the user to know the error and warning in their API document so that they can improve the standard of there API.</li>
</ul>

</p>
<p> 
Please refer link to:
<a href="https://allen.ingka.com/docs/default/component/apim-catalog/compliance_indicator/rest_business_API/">Know More</a>
</p>
</details>

<details><summary> <h4> Understand data Concept  </h4></summary>
<p>
We have introduced the ability to assign the corresponding Data Concept that belongs to your API while publishing or updating. Simply add "dataConcept": "value" to the request body.
</p>
<p> 
Please refer link to:
<a href="https://allen.ingka.com/docs/default/component/apim-catalog/data_concept/data_concept/">Know More</a>
</p>
</details>

<details><summary> <h4> Understand  API Life Cycle </h4></summary>
<p>
We have now made it available for users to send in the lifecycle along with the publishing of the API.The values that is available to choose from is, draft, published, deprecated & retired.
</p>
<p> 
Please refer link to:
<a href="https://allen.ingka.com/docs/default/component/apim-catalog/lifecycle/lifecycle_description/">Know More</a>
</p>
</details>

<details><summary> <h4> Understand  API Category </h4></summary>
<p>
We have introduced the possibility to tag your API accordingly to the corresponding API Reusability Classifications while publishing or updating your api. Simply add "reusability": "value" to the request body. There is two potential classification values to choose from, system and business. If none is passed while publishing the value will default to 'business'
</p>
<p> 
Please refer link to:
<a href="https://allen.ingka.com/docs/default/component/apim-catalog/api_category/api_reusability_classification/">Know More</a>
</p>
</details>

<details><summary> <h4> Understand  Markdown files </h4></summary>
<p>
   This is coming soon.............. <br/>
    
    when you publish your Api specification document using <a href="https://allen.ingka.com/catalog/prod/api/apim-catalog-api-v2/definition#/rest/publishSpec">APIM Catalog API</a>, you will be passing two documents urls(onboardingAndAccessDocUrl,apiGenericInfoUrl) as part of request body. This will be github url of the document file. The Template for the two files can be found below.

  <ul>
    <li><a href="https://allen.ingka.com/docs/default/component/apim-catalog/user_templates/onboardandaccess">Onboarding and Access Document Template</a></li> 
    <li><a href="https://allen.ingka.com/docs/default/component/apim-catalog/user_templates/APIsGenericInfo/">API Generic Information Document Template</a></li> 
  </ul>
</p>
</details>
