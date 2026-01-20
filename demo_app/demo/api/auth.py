import frappe
from frappe.auth import check_password

@frappe.whitelist(allow_guest=True)
def login(usr=None, pwd=None):
    frappe.local.no_cache = 1

    if not usr or not pwd:
        return {"status": "failed", "message": "Missing credentials"}

    try:
        # 🔐 Correct API-safe authentication
        check_password(usr, pwd)

        user = frappe.get_doc("User", usr)

        # Generate API Key
        if not user.api_key:
            user.api_key = frappe.generate_hash(length=15)

        # Generate API Secret
        if not user.api_secret:
            user.api_secret = frappe.generate_hash(length=30)

        user.save(ignore_permissions=True)

        return {
            "status": "success",
            "key_details": {
                "token": f"{user.api_key}:{user.api_secret}"
            },
            "full_name": user.full_name,
            "user": user.name
        }

    except frappe.AuthenticationError:
        return {"status": "failed", "message": "Invalid username or password"}
