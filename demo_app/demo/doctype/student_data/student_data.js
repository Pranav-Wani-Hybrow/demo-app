// Copyright (c) 2025, demo and contributors
// For license information, please see license.txt
//9316dfe3d592476:bb1e51767b1d5d7
frappe.ui.form.on("Student Data", {
    refresh: function(frm) {
        frm.add_custom_button(__('Call API'), function() {
            frappe.call({
                method:"demo_app.demo.doctype.student_data.student_data.call_api",
                args: {
                    student_name: frm.doc.name1
                },
                callback: function(r){
                    frappe.msgprint(r.message);
                }
            })
        });
    }
});
