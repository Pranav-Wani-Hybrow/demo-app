# Copyright (c) 2026, demo and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
import requests

class JsonPlaceholder(Document):
	pass

@frappe.whitelist()
def fetch_data(userid):
	url = f"https://jsonplaceholder.typicode.com/todos/{userid}"
	response = requests.get(url)
	return response.json()