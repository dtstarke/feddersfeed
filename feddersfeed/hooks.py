# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "feddersfeed"
app_title = "FeddersFeed"
app_publisher = "StarkApps"
app_description = "Customizations For Fedders"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "info@starkapps.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/feddersfeed/css/feddersfeed.css"
# app_include_js = "/assets/feddersfeed/js/feddersfeed.js"

# include js, css files in header of web template
web_include_css = "/assets/feddersfeed/css/fedders_web.css"
web_include_js = "/assets/feddersfeed/js/fedders_web.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "feddersfeed.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "feddersfeed.install.before_install"
# after_install = "feddersfeed.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "feddersfeed.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"feddersfeed.tasks.all"
# 	],
# 	"daily": [
# 		"feddersfeed.tasks.daily"
# 	],
# 	"hourly": [
# 		"feddersfeed.tasks.hourly"
# 	],
# 	"weekly": [
# 		"feddersfeed.tasks.weekly"
# 	]
# 	"monthly": [
# 		"feddersfeed.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "feddersfeed.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "feddersfeed.event.get_events"
# }

