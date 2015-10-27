# Badgr Server
*Digital badge management for issuers, earners, and consumers*

Badgr Server is a web application for issuing [Open Badges](http://openbadges.org). In addition to a powerful Issuer API and browser-based user interface for issuing, Badgr offers integrated badge management and sharing for badge earners. Free accounts are hosted by Concentric Sky at [Badgr.io](https://info.badgr.io), but for complete control over your own issuing environment, Badgr Server is available open source as a Python/Django application.

*Version: 1.1.0*

## How to get started on your local development environment.
Prerequisites:

  * python 2.7.x
  * virtualenv
  * npm
  * grunt
  * mysql

### Create project directory and environment
* `mkdir badgr`
* `virtualenv env`
* `source env/bin/activate` *Activate the environment (each time you start a session working with the code)*

*Obtain source code and clone into code directory*
* `git clone git@github.com:concentricsky/badgr-server.git code`
* `cd code`

*Your Directory structure will look like this with default logs and mediafiles locations:*
```
badgr
├── code
│   ├── apps
│   ├── breakdown
│   ├── build
│   ├── logs
│   ├── mediafiles
├── env
```

### Install requirements
 *from within code directory* 

* `pip install -r requirements-dev.txt`
* `npm install`

### Customize local settings to your environment
* `cp apps/mainsite/settings_local.py.example apps/mainsite/settings_local.py`
* Edit the settings_local.py file and insert local credentials for DATABASES and email, then run the following from within the `code` directory:

### Migrate databases, build front-end components
* `./manage.py migrate`
* `grunt dist` *or `grunt watch` for local development
* `./manage py createsuperuser` *follow prompts to create your first admin user account*

### Run a server locally for development
* `./manage.py runserver`
* Navigate to http://localhost:8000/accounts/login
* login, verify an email address

A browseable API is available at `/v1` and API documentation at `/docs`

### Additional configuration options
* BADGR_APPROVED_ISSUERS_ONLY:
  - If you choose to use the BADGR_APPROVED_ISSUERS_ONLY flag, this means new user accounts will not be able to define new issuers (though they can be added as staff on issuers defined by others) unless they have the Django user permission 'issuer.add_issuer'. The recommended way to grant users this privilege is to create a group that grants it in the `/staff` admin area and addthe appropriate users to that group.
