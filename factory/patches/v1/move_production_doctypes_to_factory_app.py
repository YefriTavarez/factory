# -*- coding: utf-8 -*-
# Copyright (c) 2019, Yefri Tavarez and contributors
# For license information, please see license.txt

from __future__ import unicode_literals

import frappe

from frappe import get_all
from frappe import get_doc


def execute():
    new_module = "Factory"
    old_module = "Produccion"

    doctype = "DocType"
    filters = {
        "module": old_module,
    }

    for doc in get_all(doctype, filters):
        docname = doc.name

        doc = get_doc(doctype, docname)

        doc.module = new_module

        doc.db_update()

        frappe.clear_cache(doctype=doctype)
