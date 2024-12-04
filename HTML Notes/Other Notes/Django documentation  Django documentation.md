---
title: "Django documentation | Django documentation"
source: "https://docs.djangoproject.com/en/5.1/"
author:
  - "[[Django Software Foundation]]"
published:
created: 2024-12-03
description: "The web framework for perfectionists with deadlines."
tags:
  - "clippings"
---
## Django documentation¶

Everything you need to know about Django.

## First steps¶

Are you new to Django or to programming? This is the place to start!

- **From scratch:** [Overview](https://docs.djangoproject.com/en/5.1/intro/overview/) | [Installation](https://docs.djangoproject.com/en/5.1/intro/install/)
- **Tutorial:** [Part 1: Requests and responses](https://docs.djangoproject.com/en/5.1/intro/tutorial01/) | [Part 2: Models and the admin site](https://docs.djangoproject.com/en/5.1/intro/tutorial02/) | [Part 3: Views and templates](https://docs.djangoproject.com/en/5.1/intro/tutorial03/) | [Part 4: Forms and generic views](https://docs.djangoproject.com/en/5.1/intro/tutorial04/) | [Part 5: Testing](https://docs.djangoproject.com/en/5.1/intro/tutorial05/) | [Part 6: Static files](https://docs.djangoproject.com/en/5.1/intro/tutorial06/) | [Part 7: Customizing the admin site](https://docs.djangoproject.com/en/5.1/intro/tutorial07/) | [Part 8: Adding third-party packages](https://docs.djangoproject.com/en/5.1/intro/tutorial08/)
- **Advanced Tutorials:** [How to write reusable apps](https://docs.djangoproject.com/en/5.1/intro/reusable-apps/) | [Writing your first contribution to Django](https://docs.djangoproject.com/en/5.1/intro/contributing/)

## Getting help¶

Having trouble? We’d like to help!

- Try the [FAQ](https://docs.djangoproject.com/en/5.1/faq/) – it’s got answers to many common questions.
- Looking for specific information? Try the [Index](https://docs.djangoproject.com/en/5.1/genindex/), [Module Index](https://docs.djangoproject.com/en/5.1/py-modindex/) or the [detailed table of contents](https://docs.djangoproject.com/en/5.1/contents/).
- Not found anything? See [FAQ: Getting Help](https://docs.djangoproject.com/en/5.1/faq/help/) for information on getting support and asking questions to the community.
- Report bugs with Django in our [ticket tracker](https://code.djangoproject.com/).

## How the documentation is organized¶

Django has a lot of documentation. A high-level overview of how it’s organized will help you know where to look for certain things:

- [Tutorials](https://docs.djangoproject.com/en/5.1/intro/) take you by the hand through a series of steps to create a web application. Start here if you’re new to Django or web application development. Also look at the “[First steps](https://docs.djangoproject.com/en/5.1/#index-first-steps)”.
- [Topic guides](https://docs.djangoproject.com/en/5.1/topics/) discuss key topics and concepts at a fairly high level and provide useful background information and explanation.
- [Reference guides](https://docs.djangoproject.com/en/5.1/ref/) contain technical reference for APIs and other aspects of Django’s machinery. They describe how it works and how to use it but assume that you have a basic understanding of key concepts.
- [How-to guides](https://docs.djangoproject.com/en/5.1/howto/) are recipes. They guide you through the steps involved in addressing key problems and use-cases. They are more advanced than tutorials and assume some knowledge of how Django works.

## The model layer¶

Django provides an abstraction layer (the “models”) for structuring and manipulating the data of your web application. Learn more about it below:

- **Models:** [Introduction to models](https://docs.djangoproject.com/en/5.1/topics/db/models/) | [Field types](https://docs.djangoproject.com/en/5.1/ref/models/fields/) | [Indexes](https://docs.djangoproject.com/en/5.1/ref/models/indexes/) | [Meta options](https://docs.djangoproject.com/en/5.1/ref/models/options/) | [Model class](https://docs.djangoproject.com/en/5.1/ref/models/class/)
- **QuerySets:** [Making queries](https://docs.djangoproject.com/en/5.1/topics/db/queries/) | [QuerySet method reference](https://docs.djangoproject.com/en/5.1/ref/models/querysets/) | [Lookup expressions](https://docs.djangoproject.com/en/5.1/ref/models/lookups/)
- **Model instances:** [Instance methods](https://docs.djangoproject.com/en/5.1/ref/models/instances/) | [Accessing related objects](https://docs.djangoproject.com/en/5.1/ref/models/relations/)
- **Migrations:** [Introduction to Migrations](https://docs.djangoproject.com/en/5.1/topics/migrations/) | [Operations reference](https://docs.djangoproject.com/en/5.1/ref/migration-operations/) | [SchemaEditor](https://docs.djangoproject.com/en/5.1/ref/schema-editor/) | [Writing migrations](https://docs.djangoproject.com/en/5.1/howto/writing-migrations/)
- **Advanced:** [Managers](https://docs.djangoproject.com/en/5.1/topics/db/managers/) | [Raw SQL](https://docs.djangoproject.com/en/5.1/topics/db/sql/) | [Transactions](https://docs.djangoproject.com/en/5.1/topics/db/transactions/) | [Aggregation](https://docs.djangoproject.com/en/5.1/topics/db/aggregation/) | [Search](https://docs.djangoproject.com/en/5.1/topics/db/search/) | [Custom fields](https://docs.djangoproject.com/en/5.1/howto/custom-model-fields/) | [Multiple databases](https://docs.djangoproject.com/en/5.1/topics/db/multi-db/) | [Custom lookups](https://docs.djangoproject.com/en/5.1/howto/custom-lookups/) | [Query Expressions](https://docs.djangoproject.com/en/5.1/ref/models/expressions/) | [Conditional Expressions](https://docs.djangoproject.com/en/5.1/ref/models/conditional-expressions/) | [Database Functions](https://docs.djangoproject.com/en/5.1/ref/models/database-functions/)
- **Other:** [Supported databases](https://docs.djangoproject.com/en/5.1/ref/databases/) | [Legacy databases](https://docs.djangoproject.com/en/5.1/howto/legacy-databases/) | [Providing initial data](https://docs.djangoproject.com/en/5.1/howto/initial-data/) | [Optimize database access](https://docs.djangoproject.com/en/5.1/topics/db/optimization/) | [PostgreSQL specific features](https://docs.djangoproject.com/en/5.1/ref/contrib/postgres/)

## The view layer¶

Django has the concept of “views” to encapsulate the logic responsible for processing a user’s request and for returning the response. Find all you need to know about views via the links below:

- **The basics:** [URLconfs](https://docs.djangoproject.com/en/5.1/topics/http/urls/) | [View functions](https://docs.djangoproject.com/en/5.1/topics/http/views/) | [Shortcuts](https://docs.djangoproject.com/en/5.1/topics/http/shortcuts/) | [Decorators](https://docs.djangoproject.com/en/5.1/topics/http/decorators/) | [Asynchronous Support](https://docs.djangoproject.com/en/5.1/topics/async/)
- **Reference:** [Built-in Views](https://docs.djangoproject.com/en/5.1/ref/views/) | [Request/response objects](https://docs.djangoproject.com/en/5.1/ref/request-response/) | [TemplateResponse objects](https://docs.djangoproject.com/en/5.1/ref/template-response/)
- **File uploads:** [Overview](https://docs.djangoproject.com/en/5.1/topics/http/file-uploads/) | [File objects](https://docs.djangoproject.com/en/5.1/ref/files/file/) | [Storage API](https://docs.djangoproject.com/en/5.1/ref/files/storage/) | [Managing files](https://docs.djangoproject.com/en/5.1/topics/files/) | [Custom storage](https://docs.djangoproject.com/en/5.1/howto/custom-file-storage/)
- **Class-based views:** [Overview](https://docs.djangoproject.com/en/5.1/topics/class-based-views/) | [Built-in display views](https://docs.djangoproject.com/en/5.1/topics/class-based-views/generic-display/) | [Built-in editing views](https://docs.djangoproject.com/en/5.1/topics/class-based-views/generic-editing/) | [Using mixins](https://docs.djangoproject.com/en/5.1/topics/class-based-views/mixins/) | [API reference](https://docs.djangoproject.com/en/5.1/ref/class-based-views/) | [Flattened index](https://docs.djangoproject.com/en/5.1/ref/class-based-views/flattened-index/)
- **Advanced:** [Generating CSV](https://docs.djangoproject.com/en/5.1/howto/outputting-csv/) | [Generating PDF](https://docs.djangoproject.com/en/5.1/howto/outputting-pdf/)
- **Middleware:** [Overview](https://docs.djangoproject.com/en/5.1/topics/http/middleware/) | [Built-in middleware classes](https://docs.djangoproject.com/en/5.1/ref/middleware/)

## The template layer¶

The template layer provides a designer-friendly syntax for rendering the information to be presented to the user. Learn how this syntax can be used by designers and how it can be extended by programmers:

- **The basics:** [Overview](https://docs.djangoproject.com/en/5.1/topics/templates/)
- **For designers:** [Language overview](https://docs.djangoproject.com/en/5.1/ref/templates/language/) | [Built-in tags and filters](https://docs.djangoproject.com/en/5.1/ref/templates/builtins/) | [Humanization](https://docs.djangoproject.com/en/5.1/ref/contrib/humanize/)
- **For programmers:** [Template API](https://docs.djangoproject.com/en/5.1/ref/templates/api/) | [Custom tags and filters](https://docs.djangoproject.com/en/5.1/howto/custom-template-tags/) | [Custom template backend](https://docs.djangoproject.com/en/5.1/howto/custom-template-backend/)

## Forms¶

Django provides a rich framework to facilitate the creation of forms and the manipulation of form data.

- **The basics:** [Overview](https://docs.djangoproject.com/en/5.1/topics/forms/) | [Form API](https://docs.djangoproject.com/en/5.1/ref/forms/api/) | [Built-in fields](https://docs.djangoproject.com/en/5.1/ref/forms/fields/) | [Built-in widgets](https://docs.djangoproject.com/en/5.1/ref/forms/widgets/)
- **Advanced:** [Forms for models](https://docs.djangoproject.com/en/5.1/topics/forms/modelforms/) | [Integrating media](https://docs.djangoproject.com/en/5.1/topics/forms/media/) | [Formsets](https://docs.djangoproject.com/en/5.1/topics/forms/formsets/) | [Customizing validation](https://docs.djangoproject.com/en/5.1/ref/forms/validation/)

## The development process¶

Learn about the various components and tools to help you in the development and testing of Django applications:

- **Settings:** [Overview](https://docs.djangoproject.com/en/5.1/topics/settings/) | [Full list of settings](https://docs.djangoproject.com/en/5.1/ref/settings/)
- **Applications:** [Overview](https://docs.djangoproject.com/en/5.1/ref/applications/)
- **Exceptions:** [Overview](https://docs.djangoproject.com/en/5.1/ref/exceptions/)
- **django-admin and manage.py:** [Overview](https://docs.djangoproject.com/en/5.1/ref/django-admin/) | [Adding custom commands](https://docs.djangoproject.com/en/5.1/howto/custom-management-commands/)
- **Testing:** [Introduction](https://docs.djangoproject.com/en/5.1/topics/testing/) | [Writing and running tests](https://docs.djangoproject.com/en/5.1/topics/testing/overview/) | [Included testing tools](https://docs.djangoproject.com/en/5.1/topics/testing/tools/) | [Advanced topics](https://docs.djangoproject.com/en/5.1/topics/testing/advanced/)
- **Deployment:** [Overview](https://docs.djangoproject.com/en/5.1/howto/deployment/) | [WSGI servers](https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/) | [ASGI servers](https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/) | [Deploying static files](https://docs.djangoproject.com/en/5.1/howto/static-files/deployment/) | [Tracking code errors by email](https://docs.djangoproject.com/en/5.1/howto/error-reporting/) | [Deployment checklist](https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/)

## The admin¶

Find all you need to know about the automated admin interface, one of Django’s most popular features:

- [Admin site](https://docs.djangoproject.com/en/5.1/ref/contrib/admin/)
- [Admin actions](https://docs.djangoproject.com/en/5.1/ref/contrib/admin/actions/)
- [Admin documentation generator](https://docs.djangoproject.com/en/5.1/ref/contrib/admin/admindocs/)

## Security¶

Security is a topic of paramount importance in the development of web applications and Django provides multiple protection tools and mechanisms:

- [Security overview](https://docs.djangoproject.com/en/5.1/topics/security/)
- [Disclosed security issues in Django](https://docs.djangoproject.com/en/5.1/releases/security/)
- [Clickjacking protection](https://docs.djangoproject.com/en/5.1/ref/clickjacking/)
- [Cross Site Request Forgery protection](https://docs.djangoproject.com/en/5.1/ref/csrf/)
- [Cryptographic signing](https://docs.djangoproject.com/en/5.1/topics/signing/)
- [Security Middleware](https://docs.djangoproject.com/en/5.1/ref/middleware/#security-middleware)

## Internationalization and localization¶

Django offers a robust internationalization and localization framework to assist you in the development of applications for multiple languages and world regions:

- [Overview](https://docs.djangoproject.com/en/5.1/topics/i18n/) | [Internationalization](https://docs.djangoproject.com/en/5.1/topics/i18n/translation/) | [Localization](https://docs.djangoproject.com/en/5.1/topics/i18n/translation/#how-to-create-language-files) | [Localized web UI formatting and form input](https://docs.djangoproject.com/en/5.1/topics/i18n/formatting/)
- [Time zones](https://docs.djangoproject.com/en/5.1/topics/i18n/timezones/)

## Performance and optimization¶

There are a variety of techniques and tools that can help get your code running more efficiently - faster, and using fewer system resources.

- [Performance and optimization overview](https://docs.djangoproject.com/en/5.1/topics/performance/)

## Geographic framework¶

[GeoDjango](https://docs.djangoproject.com/en/5.1/ref/contrib/gis/) intends to be a world-class geographic web framework. Its goal is to make it as easy as possible to build GIS web applications and harness the power of spatially enabled data.

## Common web application tools¶

Django offers multiple tools commonly needed in the development of web applications:

- **Authentication:** [Overview](https://docs.djangoproject.com/en/5.1/topics/auth/) | [Using the authentication system](https://docs.djangoproject.com/en/5.1/topics/auth/default/) | [Password management](https://docs.djangoproject.com/en/5.1/topics/auth/passwords/) | [Customizing authentication](https://docs.djangoproject.com/en/5.1/topics/auth/customizing/) | [API Reference](https://docs.djangoproject.com/en/5.1/ref/contrib/auth/)
- [Caching](https://docs.djangoproject.com/en/5.1/topics/cache/)
- [Logging](https://docs.djangoproject.com/en/5.1/topics/logging/)
- [Sending emails](https://docs.djangoproject.com/en/5.1/topics/email/)
- [Syndication feeds (RSS/Atom)](https://docs.djangoproject.com/en/5.1/ref/contrib/syndication/)
- [Pagination](https://docs.djangoproject.com/en/5.1/topics/pagination/)
- [Messages framework](https://docs.djangoproject.com/en/5.1/ref/contrib/messages/)
- [Serialization](https://docs.djangoproject.com/en/5.1/topics/serialization/)
- [Sessions](https://docs.djangoproject.com/en/5.1/topics/http/sessions/)
- [Sitemaps](https://docs.djangoproject.com/en/5.1/ref/contrib/sitemaps/)
- [Static files management](https://docs.djangoproject.com/en/5.1/ref/contrib/staticfiles/)
- [Data validation](https://docs.djangoproject.com/en/5.1/ref/validators/)

## Other core functionalities¶

Learn about some other core functionalities of the Django framework:

- [Conditional content processing](https://docs.djangoproject.com/en/5.1/topics/conditional-view-processing/)
- [Content types and generic relations](https://docs.djangoproject.com/en/5.1/ref/contrib/contenttypes/)
- [Flatpages](https://docs.djangoproject.com/en/5.1/ref/contrib/flatpages/)
- [Redirects](https://docs.djangoproject.com/en/5.1/ref/contrib/redirects/)
- [Signals](https://docs.djangoproject.com/en/5.1/topics/signals/)
- [System check framework](https://docs.djangoproject.com/en/5.1/topics/checks/)
- [The sites framework](https://docs.djangoproject.com/en/5.1/ref/contrib/sites/)
- [Unicode in Django](https://docs.djangoproject.com/en/5.1/ref/unicode/)

## The Django open-source project¶

Learn about the development process for the Django project itself and about how you can contribute:

- **Community:** [Contributing to Django](https://docs.djangoproject.com/en/5.1/internals/contributing/) | [The release process](https://docs.djangoproject.com/en/5.1/internals/release-process/) | [Team organization](https://docs.djangoproject.com/en/5.1/internals/organization/) | [The Django source code repository](https://docs.djangoproject.com/en/5.1/internals/git/) | [Security policies](https://docs.djangoproject.com/en/5.1/internals/security/) | [Mailing lists and Forum](https://docs.djangoproject.com/en/5.1/internals/mailing-lists/)
- **Design philosophies:** [Overview](https://docs.djangoproject.com/en/5.1/misc/design-philosophies/)
- **Documentation:** [About this documentation](https://docs.djangoproject.com/en/5.1/internals/contributing/writing-documentation/)
- **Third-party distributions:** [Overview](https://docs.djangoproject.com/en/5.1/misc/distributions/)
- **Django over time:** [API stability](https://docs.djangoproject.com/en/5.1/misc/api-stability/) | [Release notes and upgrading instructions](https://docs.djangoproject.com/en/5.1/releases/) | [Deprecation Timeline](https://docs.djangoproject.com/en/5.1/internals/deprecation/)