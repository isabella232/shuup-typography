# -*- coding: utf-8 -*-
# This file is part of Shuup Typography.
#
# Copyright (c) 2012-2018, Shuup Inc. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
from __future__ import unicode_literals

from django import forms
from django.utils.translation import ugettext_lazy as _
from shuup.admin.forms.widgets import FileDnDUploaderWidget
from shuup.admin.shop_provider import get_shop
from shuup.admin.utils.picotable import Column, TextFilter
from shuup.admin.utils.views import CreateOrUpdateView, PicotableListView

from shuup_typography.models import FontFamily


class FontFamilyForm(forms.ModelForm):
    class Meta:
        model = FontFamily
        exclude = ("shop",)

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request")
        super(FontFamilyForm, self).__init__(*args, **kwargs)
        self.fields["woff"].widget = FileDnDUploaderWidget(upload_path="/typography/", clearable=True)
        self.fields["woff2"].widget = FileDnDUploaderWidget(upload_path="/typography/", clearable=True)
        self.fields["ttf"].widget = FileDnDUploaderWidget(upload_path="/typography/", clearable=True)
        self.fields["svg"].widget = FileDnDUploaderWidget(upload_path="/typography/", clearable=True)
        self.fields["eot"].widget = FileDnDUploaderWidget(upload_path="/typography/", clearable=True)

    def save(self, commit=True):
        self.instance.shop = get_shop(self.request)
        return super(FontFamilyForm, self).save(commit)


class FontFamilyEditView(CreateOrUpdateView):
    model = FontFamily
    form_class = FontFamilyForm
    template_name = "shuup_typography/font_family_edit.jinja"
    context_object_name = "font_family"

    def get_queryset(self):
        return FontFamily.objects.filter(shop=get_shop(self.request))

    def get_form_kwargs(self):
        kwargs = super(FontFamilyEditView, self).get_form_kwargs()
        kwargs["request"] = self.request
        return kwargs


class FontFamilyListView(PicotableListView):
    url_identifier = "typography_font"
    model = FontFamily
    default_columns = [
        Column(
            "name",
            _("Name"),
            sort_field="name",
            display="name",
            filter_config=TextFilter(
                filter_field="name",
                placeholder=_("Filter by name...")
            )
        ),
        Column("woff", _("Woff"), display="format_woff"),
        Column("woff2", _("Woff2"), display="format_woff2"),
        Column("ttf", _("TTF"), display="format_ttf"),
        Column("svg", _("SVG"), display="format_svg"),
        Column("eot", _("EOT"), display="format_eot")
    ]

    def format_eot(self, instance):
        return instance.eot.label if instance.eot else ""

    def format_ttf(self, instance):
        return instance.ttf.label if instance.ttf else ""

    def format_woff(self, instance):
        return instance.woff.label if instance.woff else ""

    def format_woff2(self, instance):
        return instance.woff2.label if instance.woff2 else ""

    def format_svg(self, instance):
        return instance.svg.label if instance.svg else ""

    def get_queryset(self):
        return FontFamily.objects.filter(shop=get_shop(self.request))
