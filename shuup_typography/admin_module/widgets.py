# -*- coding: utf-8 -*-
# This file is part of Shuup Typography.
#
# Copyright (c) 2012-2018, Shuup Inc. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.

from django.core.urlresolvers import reverse_lazy
from shuup.admin.forms.widgets import QuickAddRelatedObjectSelect


class QuickAddFontFamilySelect(QuickAddRelatedObjectSelect):
    url = reverse_lazy("shuup_admin:typography_font.new")
