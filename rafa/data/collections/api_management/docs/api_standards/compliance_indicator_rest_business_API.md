# Business WebAPI Compliance Indicator- REST

## Motivation

API Management and Event management teams are working with different engineering domains to bring acceptable API standards for both 'Web API' and 'Async API'. The outcome of such engagement is API standards and best practices which are written and maintained in [Ignka API Standards](https://github.com/ingka-group-digital/api-standards).

The engaged community also worked on a [linting tool](https://github.com/ingka-group-digital/lint-openapi) that encapsulated all the rules, which are possible of validate and then validate one API specification in different stages of API development and deployment lifecycle. The linting tool would be available to use as a github workflow and as a CLI tool.

The last piece of the puzzle to bring API uniformity and standardization is to place a solution that leverages the agreed API standards in a seamless manner during the API deployment process to central API catalog and gives a better visibility of below measurement in Allen portal

- API specification standard compliance
- API implementation compliance
- API performance & health compliance

For the current MVP realease we considered only 'API specification standard compliance'.

## How the compliance indicator works

The business web API compliance indicator works based on two set of user provider data during API publication to API catalog (with or without API deployment to APIM managed gateway)

- API Specification
- API metadata

### API Specification:

The API is the most important factor in API compliance calculation. The Rules are mentioned in [Ignka REST WebAPI Standards](https://github.com/ingka-group-digital/api-standards/tree/main/docs/WebAPI). You can check the value of a column called 'lint implementation status' to understand if the rules are already part of current implementation or not.The implentation of API specification liniting is based on redocly CLI and enhancement is done based on rules mentioned in [Ignka REST WebAPI Standards](https://github.com/ingka-group-digital/api-standards/tree/main/docs/WebAPI). To follow all the rules redockly based linter enforced follow [Lint OpenAPI]https://github.com/ingka-group-digital/lint-openapi.

The lint-openapi returns API validation results with different severity (warn, error etc). The compliance indication has defined weightage for them as shown below.

| severity | weightage |
| :------- | :-------- |
| error    | 3         |
| warning  | 1         |

while calculating the overall score total violation is calculated based on count and weightage and then deducted from 100. If the total score is less than 100 then it would remain as 0 as -ve score is not shown.

Example 1: If there are 3 errors and 10 warnings in and api doc then:

                Final Score = 100 - ( 3* number of errors + 1* number of warnings)
                Final Score = 100 - ( 3*3+ 1*10)
                Final Score = 100-19
                Final Score = 81
                
 Example 2: if there are  40 error and 20 warning in an api doc then:
 
                Final Score = 100 - ( 3* number of errors + 1* number of warnings)
                Final Score = 100 - ( 3*40+ 1*20)
                Final Score = 100-140
                Final Score = 0 (since your score is coming in -ve) . 
                
### API Metadata

API metadata is Ingka business structure related properties which are softly tagged with API while publishing to API Catalog. Right now there are three set of API metadata which are part of API compliance indicator

| property                                              | weightage |
| :---------------------------------------------------- | :-------- |
| system from system master catalog                     | 3         |
| team name from myidentity (aka IGNA)                  | 3         |
| Data concept from Ingka business data concept catalog | 1         |

While publishing through the APIM catalog API system and team name are part of the onboarding process, hence data concept is the only input driven field among three
while publishing through APIM Provider API all three fields are user input driven fields. Data concept calculations is not applied to system APIs. 

## Fixing compliance issues

Depending on the scope of the issue either you need to update your specification or you need to add API business metadata

### Fixing API specification

Please go through all the violated points and understand them. You can follow [Ignka REST WebAPI Standards](https://github.com/ingka-group-digital/api-standards/tree/main/docs/WebAPI) to know more. If you are considering to modifiy the rules then please raise a pull request or discussion in the github repo itselfIf you plannning to adhere exsiting rules then once your specification is changed then you can validate them using [Lint OpenAPI](https://github.com/ingka-group-digital/lint-openapi). It support three ways of API spcification validation

- github actions
- CLI
- npm package

🎯 If you are using Kong API gateway managed by APIM then there are some additional rules which can be found [here](https://github.com/ingka-group-digital/api-standards/blob/main/docs/WebAPI/CENTRALGATEWAY.md)

(want to contribute to release another form of validation please raise one discussion in the GIT repo or reach out to APIM team)

Once you fix it please republish the specification.

### Fixing API metadata

Simply use APIM catalog API or APIM provider API request body to update API metadata

### Validating your API before publication

We have introduced a new [endpoint](https://allen.ingka.com/catalog/prod/api/apim-catalog-api-v2/definition#/Specifications/validateSpec) which can be used to validate your specs before publishing it. This will give you chance to work on your errors and warning and get rid of them before it is published and shown to the consumer of your api.
