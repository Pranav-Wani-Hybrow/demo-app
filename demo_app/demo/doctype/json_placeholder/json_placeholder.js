// Copyright (c) 2026, demo and contributors
// For license information, please see license.txt

frappe.ui.form.on("Json Placeholder", {
    refresh: function(frm){
        if(frm.doc.userid && !frm.doc.title && !frm.doc.completed){
        frm.add_custom_button(__('Fetch Data'),function(){
            frappe.call({
                method : "demo_app.demo.doctype.json_placeholder.json_placeholder.fetch_data",
                args: {
                    userid: frm.doc.userid
                },
                callback: function(r){
                    if(r.message){
                        frm.set_value("title", r.message.title);
                        frm.set_value("completed", String(r.message.completed));
                        // ---------------OR----------------
                        // frm.set_value("completed", r.message.completed ? "true" : "false");
                    }
                    frappe.msgprint("Data Fetched Successfully");
                    frm.save();
                    frm.refresh_fields();
                }
            })
        })
    }
        // -------------This is another way to fetch data from JS code-----------------

        // frm.add_custom_button(__('Fetch Data'), async function(){

        //     if(!frm.doc.userid){
        //         frappe.msgprint("Please enter User ID");
        //         return;
        //     }

        //     try {
        //         frappe.dom.freeze("Fetching data...");

        //         const response = await fetch(
        //             `https://jsonplaceholder.typicode.com/todos/${frm.doc.userid}`
        //         );

        //         if (!response.ok) {
        //             throw new Error("API error");
        //         }

        //         const data = await response.json();

        //         frm.set_value("title", data.title);
        //         frm.set_value("completed", String(data.completed));

        //         frappe.msgprint("Data fetched successfully");
        //         frm.refresh(); // Optional: Refresh the form to reflect changes
        //     }
        //     catch (err) {
        //         frappe.msgprint("Failed to fetch data");
        //         console.error(err);
        //     }
        //     finally {
        //         frappe.dom.unfreeze();
        //     }
        // });
    }
});
