import frappe
from frappe.utils import add_days

def schedule_due_dates():
    tasks = frappe.get_all("Maintenance Task", filters={"status": "Open"})
    for task in tasks:
        doc = frappe.get_doc("Maintenance Task", task.name)
        if doc.interval_duration:
            doc.due_date = add_days(doc.last_performed, doc.interval_duration)
            doc.save()
