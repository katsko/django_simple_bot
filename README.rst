===========================
Demo: Telegram bot + Django
===========================

This is a simple demo of integration Telegram bot (pyTelegramBotAPI lib) and Django.

Recive message, save to DB and show info: record ID and count records in DB.


Install
=======

.. code-block:: shell-session

    git clone https://github.com/katsko/django_simple_bot.git
    cd django_simple_bot
    # activate venv if necessary
    # and install python libs
    pip install -r requires/requires.txt
    # create DB in PostgreSQL (or change DB settings in django settings)
    # run django migrate and create superuser for Django admin
    ./manage.py migrate
    ./manage.py createsuperuser
    ./manage.py runserver


Public URL and HTTPS
====================

If you don't have public URL, you can use ngrok service https://ngrok.com/.

Download ngrok, create account, run setup (ngrok config add-authtoken ...).

Run ngrok in CLI, you take public URL.


Tokens
======

Before run django app, you shoud create settings file from template.

Copy django_simple_bot/settings_local.tmpl to django_simple_bot/settings_local.py

Open django_simple_bot/settings_local.py in text editor and write correct tokens.


Telegram bot token
------------------

Each Telegram bot have a token. Create your bot https://core.telegram.org/bots#3-how-do-i-create-a-bot and save token or use your exist token.

Write token to TG_TOKEN variable in django_simple_bot/settings_local.py


Telegram webhook settings
-------------------------

Telegram send message to bot-server by https. You shoud tell your public URL to Telegram.

This demo app contains function to create URL for webhook and send this to Telegram.

Write random string to TG_SECRET_LINK variable in django_simple_bot/settings_local.py. Run django app (./manage.py runserver) run ngrok and open admin page to authorization as superuser (you create this user befor by command ./manage.py createsuperuser) URL like this: https://***.ngrok.io/admin/. After authorization you should open a secial page in browser, url like this: https://***.ngrok.io/tg/settings. When you open this page, Django app run tg_webhook_url_settings function and send secret URL to Telegram.


Description
===========

Parts of this demo code:

* List of libs in requires/requires.txt: Django, Telegram lib and PostgreSQL lib.
* Django settings (settings.py, url.py, etc).
* Django ORM model: base/models.py.
* Django views: base/views.py.
* Telegram bot handlers: base/tg.py.


Django views
------------


tg_webhook
~~~~~~~~~~

All telegram messages (for your bot) will send to this function. If request send to secret link, request data will convert to json and send to bot-object.


tg_webhook_url_settings
~~~~~~~~~~~~~~~~~~~~~~~

Function for tell Telegram about your public URL. This function take a public ngrok subdomain, add a secret part and send full URL to Telegram.


Bot handlers
------------

start
~~~~~

This function send to user a welcome message.


info
~~~~

This function send to user a count of DB records.


get_msg
~~~~~~~

This function recive all messages (except /start and /info), save message to DB and replay to user a message ID.


Django model
------------

Msg
~~~

This is a very simple model to create one table with two columns: id and text.

When demo app recive a message (except /start and /info), message will save to this database table.
