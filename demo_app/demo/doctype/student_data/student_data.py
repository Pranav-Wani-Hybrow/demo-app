# Copyright (c) 2025, demo and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class StudentData(Document):
    pass

@frappe.whitelist()
def call_api(student_name):
    return f"API called successfully for student: {student_name}"