# wagtail-mautic

Adds Mautic Marketing Automation into a Wagtail site with a few simple template tags

## Installation

Install using pip

    pip install wagtail-mautic

Now add the application `wagtail_mautic` to your Django applications. In your _base.py_ settings file:

```python
    INSTALLED_APPS = [
        ...
        "wagtail.contrib.settings",
        "wagtail_mautic",
        ...
        ]
```

Add the site settings to your context processors:

```python
    'OPTIONS': {
        'context_processors': [
            ...

            'wagtail.contrib.settings.context_processors.settings',
        ]
    }
```

Migrate your models:

    python manage.py migrate

## Add your Mautic setup information

When you spin up your Wagtail app, you should now see a new Mautic settings in the Wagtail admin screen.

![Navigation in Wagtail admin](screenshots/settings_selector.png)

Add in the URL for your Mautic instance (including the https://) to the **Mautic Url** field.

![Mautic settings](screenshots/mautic_settings.png)

## Add Mautic page tracking

The template tag `{% mautic_tracker %}` can be added to any page and this will add in the Mautic tracking code. The tag will only add text when the Mautic URL has been added in the settings.

To install site-wide add this to your _base.html_ template or similar.

Recommended placement is to add the tracking code as the last item in the `<body> ... </body>` tag section.

## Add Mautic prefetch tags

For faster loading of pages, the Mautic site can be set up with a pre-fetch `<link>` in the header.  To add this to your site, add the `{% mautic_prefetch %}` tag within the `<head></head>` of your templates.
