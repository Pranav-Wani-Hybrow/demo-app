# Copyright (c) 2025, demo and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class StudentData(Document):
    def validate(self):
        if not self.student_name:
            frappe.throw("Student Name is required.")
        if self.age and self.age < 0:
            frappe.throw("Age cannot be negative.")

@frappe.whitelist()
def call_api(student_name):
    return f"API called successfully from js for student: {student_name}"