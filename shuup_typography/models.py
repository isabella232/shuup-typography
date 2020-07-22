# -*- coding: utf-8 -*-
# This file is part of Shuup Typography.
#
# Copyright (c) 2012-2018, Shuup Inc. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from filer.fields.image import FilerFileField


@python_2_unicode_compatible
class FontFamily(models.Model):
    shop = models.ForeignKey(
        "shuup.Shop", verbose_name=_("Shop"), related_name="typography_fonts", on_delete=models.CASCADE)
    name = models.CharField(max_length=128, verbose_name=_("name"), help_text=_("Font family name"))

    woff = FilerFileField(
        verbose_name=_("WOFF Font"),
        blank=True, null=True,
        on_delete=models.SET_NULL,
        related_name="typography_woff_fonts"
    )
    woff2 = FilerFileField(
        verbose_name=_("WOFF2 Font"),
        blank=True, null=True,
        on_delete=models.SET_NULL,
        related_name="typography_woff2_fonts"
    )
    ttf = FilerFileField(
        verbose_name=_("TTF font"),
        blank=True, null=True,
        on_delete=models.SET_NULL,
        related_name="typography_ttf_fonts"
    )
    svg = FilerFileField(
        verbose_name=_("SVG font"),
        blank=True, null=True,
        on_delete=models.SET_NULL,
        related_name="typography_svg_fonts"
    )
    eot = FilerFileField(
        verbose_name=_("EOT font"),
        blank=True, null=True,
        on_delete=models.SET_NULL,
        related_name="typography_eot_fonts"
    )

    class Meta:
        verbose_name = _("Font Family")
        verbose_name_plural = _("Font Families")
        unique_together = ("shop", "name")

    def __str__(self):
        return self.name

    def get_font_sources(self):
        font_sources = []

        if self.eot:
            font_sources.append("url('%s?#iefix') format('embedded-opentype')" % self.eot.url)
        if self.woff:
            font_sources.append("url('%s') format('woff')" % self.woff.url)
        if self.woff2:
            font_sources.append("url('%s') format('woff2')" % self.woff2.url)
        if self.ttf:
            font_sources.append("url('%s') format('truetype')" % self.ttf.url)
        if self.svg:
            font_sources.append("url('%s#svgFontName') format('svg')" % self.svg.url)

        return font_sources
