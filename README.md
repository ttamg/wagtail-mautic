# wagtail-mautic

Adds Mautic Marketing Automation into a Wagtail site with a few simple template tags

## Installation

Install using pip

    pip install wagtail-mautic

Now add the application `wagtail_mautic` to your Django applications. In your _base.py_ settings file:

```python
    INSTALLED_APPS = [
        ...
        "wagtail_mautic",
        ...
        ]
```

Migrate your models:

    python manage.py migrate

## Setup

Wnen you spin up your Wagtail app, you should now see a new Mautic settings in the Wagtail admin screen

Add in the URL for your Mautic instance (including the https://) to the **Mautic Url** field.

## Add Mautic page tracking

The template tag `{% mautic_tracker %}` can be added to any page and this will add in the Mautic tracking code.

To install site-wide add this to your _base.html_ template or similar.

Recommended placement is to add the tracking code as the last item in the `<body> ... </body>` tag section.
