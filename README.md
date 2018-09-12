# Shuup Typography

This package adds custom typography for the [Shuup](https://shuup.com/) platform.

## Usage

After installing the addon, you just need to invoke add the rendered custom style using the renderer:


```python
from shuup_typography.models import FontFamily
from shuup_typography.renderer import render_custom_font_style

ff = FontFamily.objects.get(shop=my_shop, name="Open Sans")
custom_style = render_custom_font_style(body_font_family=ff)
print(custom_style)
```

The generated code will be:

```html
<style type="text/css">
    @font-face {
        font-family: 'Open Sans';
        src: url('/some/place/open-sans.ttf') format('truetype');
    }
    body {
        font-family: 'Open Sans';
    }
    * {
        font-family: 'Open Sans';
    }
</style>
```

This can then be injected into the `head` of your template of even through xtheme resource injection.

## Copyright

Copyright (C) 2012-2018 by Shuup Inc. <support@shuup.com>

Shuup is International Registered Trademark & Property of Shuup Inc.,
Business Address: 1013 Centre Road, Suite 403-B,
Wilmington, Delaware 19805,
United States Of America

## License

Shuup Typography addon is published under Open Software License version 3.0 (OSL-3.0).
See the LICENSE file distributed with Shuup.
