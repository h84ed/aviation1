from . import __version__ as app_version

app_name = "aviation"
app_title = "Aviation"
app_publisher = "Ed Harrison"
app_description = "Aviation maintenance, repair and overhaul functionality and inventory for parts"
app_email = "ed@turbinetech.aero"
app_icon = "octicon octicon-tools"
app_color = "blue"
app_license = "MIT"
source_link = "https://turbinetech.aero"
app_logo_url = "/assets/aviation/images/logo.svg"

doc_events = {
    "File": {
        "on_update": "aviation.api.version_control"
    }
}

app_include_css = "/assets/aviation/css/aviation.css"

fixtures = [
    "Custom Field",
    "Property Setter",
    "Custom Script",
    "Report",
    "Workflow",
    "Workflow State",
    "Workflow Action Master",
    {
        "dt": "DocType",
        "filters": [
            ["name", "in", [
                "Item", 
                "Item Price",
                "Asset",
                "Workflow",
                "Workflow State",
                "Aircraft", 
                "Engine", 
                "Project",
                "Maintenance Task", 
                "Work Order",
                "Airworthiness Directive", 
                "Service Bulletin",
                "Core Tracking",
                "LLP"
            ]]
        ]
    }
]

doctype_js = {
    "BOM": "public/js/bom_custom.js",
    "Stock Entry": "public/js/stock_entry.js",
}

doc_events = {
    "Asset": {
        "validate": "aviation.hooks.asset_hooks.auto_set_next_due"
    }
}

scheduler_events = {
    "daily": [
        "aviation.scripts.due_date_calculator.schedule_due_dates"
    ]
}

add_to_apps_screen = [
 	{
 		"name": "aviation",
 		"logo": "/assets/aviation/logo.png",
 		"title": "Aviation",
 		"route": "/aviation",
 		"has_permission": "aviation.api.permission.has_app_permission"
 	}
 ]

