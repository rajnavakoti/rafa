# API Lifecycle

We have now made it available for users to send in the lifecycle along with the publishing of the API. Simply send it in your request body as "lifeCycleState": "value". If not passed, the value will default to "published". The values that is available to choose from is, draft, published, deprecated & retired.

## Draft 
Services which is under development with a high possibility to become a provided service

## Published
Services that are available today for consumer

## Deprecated

No new subscriber should be allowed to subscribe to that API. Requests from existing consumers will be fulfilled as usual. There could be a chance that the another version of same events may exist and over the time all the existing consumer should be migrated and started consuming new version of the events

## Retired

Services which is going to be stopped after an agreed date. It means before that date all consumer need to move to the alternate service.