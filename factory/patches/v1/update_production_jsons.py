# -*- coding: utf-8 -*-
# Copyright (c) 2019, Yefri Tavarez and contributors
# For license information, please see license.txt

from __future__ import unicode_literals

import frappe

from frappe import get_all
from frappe import get_doc


def execute():
    # path = frappe.get_app_path("factory", "doctype")

    module = "Factory"

    doctype = "DocType"
    filters = {
        "module": module,
    }

    for doc in get_all(doctype, filters):
        docname = doc.name

        doc = get_doc(doctype, filters)

        doc.save(ignore_permissions=True)
