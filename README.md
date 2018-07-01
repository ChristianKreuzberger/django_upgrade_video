# Example Repo for Upgrading Django Apps
This repo contains information about upgrading your Django application from Django 1.8 to Django 1.11, and
from Django 1.11 to Django 2.2. Those are all long term support (LTS) releases.

Please also take a look at this [YouTube Video](https://www.youtube.com/watch?v=-_nq0s46Dnc) for more information.

## Example Application

As an example application, we prepared a very basic ticket system, which allows creating aswell as editing
tickets. Tickets have a title, a description, a state, and can be assigned to any number of users. Each
user has their individual "My Tickets" page.

Each ticket can be commented on by users.

This example application makes use of Foreign Keys, Many-To-Many Fields, template tags, middlewares, views, etc... - a typical Django app.

for more information about the application (e.g., installation instructions), please take a look at [docs/app.md](docs/app.md).

## Branches

Please take a look at the following branches:

* django18 - contains the app the way it used to be with Django 1.8
* django18_to_111 - contains all commits for upgrading from 1.8 to 1.11
* master - ongoing development

# The process of upgrading

Of course, there are many features of Django that have changed over the years. But with this little example
application we are trying to cover the most basic ones, especially those that will affect almost everybody.

As a good starting point, I recommend reading [Upgrading Django](https://docs.djangoproject.com/en/1.11/howto/upgrade-version/)
on the official Django Project website. Other then that, I recommend reading the release notes of new Django
releases. They usually have a section called [Backwards incompatible changes](https://docs.djangoproject.com/en/1.9/releases/1.9/#backwards-incompatible-changes-in-1-9)
as well as a section called [Breaking changes (or Features removed)](https://docs.djangoproject.com/en/1.9/releases/1.9/#removed-features-1-9).

Another good resource is the [Django Deprecation Timeline](https://docs.djangoproject.com/en/dev/internals/deprecation/),
which contains several features that already have been deprecated, but also those that will be deprecated in the future.

It is recommended to only upgrade to the next LTS (Long Term Support) version of Django. Make sure to take a look at
[the Django Download Page](https://www.djangoproject.com/download/#supported-versions) for a good overview of which
release has long term support.

## Upgrading Django 1.8 to 1.11
See [docs/upgrade_18_to_111.md](docs/upgrade_18_to_111.md).

## Upgrading Django 1.11 to 2.2
As 2.2 has not been released, we will only cover preparations here.

Basically, what we can cover is upgrading from 1.11 to 2.0, which is written down in
[docs/upgrade_111_to_20.md](docs/upgrade_111_to_20.md).

## Docker Setup

See [docs/docker.md](docs/docker.md) for information about the docker setup.
