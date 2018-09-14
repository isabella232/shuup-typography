# -*- coding: utf-8 -*-
# This file is part of Shuup Typography.
#
# Copyright (c) 2012-2018, Shuup Inc. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.


def render_custom_font_style(body_font_family=None, header_font_family=None, base_font_size=None,
                             body_font_custom_rules=[], header_font_custom_rules=[]):
    """
    Convert the font configuration into a <style> element with all rules to be
    injected into the <head> of the page.

    :param body_font_family shuup_typography.FontFamily|None: the font to be used in body
    :param header_font_family shuup_typography.FontFamily|None: the font to be used in headers (h1, h2, etc)
    :param base_font_size str|None: the base font size to be used (12px, 1em, etc)
    :param body_font_custom_rules list: list of custom rules to apply the body custom font
    :param header_font_custom_rules list: list of custom rules to apply the header custom font

    :rtype string
    """
    context = {}
    if body_font_family:
        context["body_font_family"] = body_font_family
    if header_font_family:
        context["header_font_family"] = header_font_family
    if base_font_size:
        context["base_font_size"] = base_font_size
    if header_font_custom_rules:
        context["header_font_custom_rules"] = header_font_custom_rules
    if body_font_custom_rules:
        context["body_font_custom_rules"] = body_font_custom_rules

    from django.template import loader
    return loader.render_to_string("shuup_typography/custom_styles.jinja", context=context)
