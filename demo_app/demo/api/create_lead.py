import frappe
from frappe import _

@frappe.whitelist(allow_guest=False)
def create_lead(data):
    """
    Create Lead from external application
    """

    if isinstance(data, str):
        data = frappe.parse_json(data)

    # Mandatory fields
    required_fields = ["lead_name", "email_id", "mobile_no"]
    for field in required_fields:
        if not data.get(field):
            frappe.throw(_("{0} is required").format(field))

    # Duplicate check (email or mobile)
    existing_lead = frappe.db.exists(
        "Lead",
        {"email_id": data.get("email_id")}
    ) or frappe.db.exists(
        "Lead",
        {"mobile_no": data.get("mobile_no")}
    )

    if existing_lead:
        return {
            "status": "exists",
            "lead": existing_lead
        }

    lead = frappe.get_doc({
        "doctype": "Lead",
        "lead_name": data.get("lead_name"),
        "email_id": data.get("email_id"),
        "mobile_no": data.get("mobile_no"),
        "company_name": data.get("company_name"),
        "source": data.get("source") or None,
        "lead_owner": data.get("lead_owner") or frappe.session.user,
        "status": "Lead"
    })

    lead.insert(ignore_permissions=True)

    return {
        "status": "success",
        "lead": lead.name
    }


