# -*- coding: utf-8 -*-
# This file is part of Shuup Typography.
#
# Copyright (c) 2012-2018, Shuup Inc. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.

from django import forms
from django.utils.translation import ugettext_lazy as _


def get_render_custom_font_styles(theme, custom_rules, **kwargs):
    from shuup_typography.models import FontFamily
    from shuup_typography.renderer import render_custom_font_style
    body_font_family_id = theme.get_setting("body_font_family")
    header_font_family_id = theme.get_setting("header_font_family")
    base_font_size = theme.get_setting("base_font_size")
    body_font_family = None
    header_font_family = None

    if body_font_family_id:
        body_font_family = FontFamily.objects.filter(pk=body_font_family_id).first()

    if header_font_family_id:
        header_font_family = FontFamily.objects.filter(pk=header_font_family_id).first()

    return render_custom_font_style(
        body_font_family, header_font_family, base_font_size, body_font_custom_rules=custom_rules)


def get_custom_font_fields(theme, shop, **kwargs):
    if not shop:
        return []
    from shuup_typography.models import FontFamily
    from shuup_typography.admin_module.widgets import QuickAddFontFamilySelect
    font_choices = [
        (custom_font.pk, custom_font.name)
        for custom_font in FontFamily.objects.filter(shop=shop)
    ]
    font_choices.insert(0, ("", "------"))

    return [
        ("body_font_family", forms.ChoiceField(
            required=False, initial=None,
            label=_("Body font family"),
            choices=font_choices,
            widget=QuickAddFontFamilySelect(editable_model="shuup_typography.FontFamily")
        )),
        ("header_font_family", forms.ChoiceField(
            required=False, initial=None,
            label=_("Header font family"),
            choices=font_choices,
            widget=QuickAddFontFamilySelect(editable_model="shuup_typography.FontFamily")
        )),
        ("base_font_size", forms.CharField(
            label=_("Base font size"),
            required=False,
            help_text=_("Enter a valid CSS font-size value, e.g: 12px, 1.2em.")
        ))
    ]
