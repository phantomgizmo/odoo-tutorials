# Odoo tutorials

This repository hosts the code for the bases of the modules used in the
[official Odoo tutorials](https://www.odoo.com/documentation/latest/developer/tutorials.html).

It has 3 branches for each Odoo version: one for the bases, one for the
[Discover the JS framework](https://www.odoo.com/documentation/latest/developer/tutorials/discover_js_framework.html)
tutorial's solutions, and one for the
[Master the Odoo web framework](https://www.odoo.com/documentation/latest/developer/tutorials/master_odoo_web_framework.html)
tutorial's solutions. For example, `17.0`, `17.0-discover-js-framework-solutions` and
`17.0-master-odoo-web-framework-solutions`.

# Learning journey

Learning resource: https://www.odoo.com/documentation/18.0/developer/tutorials/setup_guide.html

1. Setup odoo on local device, result: Finished setting up odoo (setup db, clone odoo repo and init db)
2. Architecture overview:
   - Has n tier architecture, presentation, logic, and data
   - presentation consists of HTML5, JS, and CSS
   - logic exclusively written in Python
   - data tier only supports PostrgreSQL as RDBMS
   - module can ADD new business logic, or ALTER existing business logic.
   - Module also referred to as addons, odoo search for addons from addons-path/
   - Business Object -> business object declared as python class (think this is similar to a model in conventional web framework).
   - Object views -> the UI
   - Data files -> XML or CSV files declaring the model data (e.g. views or reports, config data, demo data, etc.)
   - Web controllers -> handle requests from web browsers
   - Static web data -> images, css or JS files
     Output: Understood odoo architecture overview, folder structure and module definition. Found hr_attendance module which might be useful for the testcase. Read the module documentation.
3. After reading the attendance documentation, i gained a lot of insight on how to finish given testcase.
4. A New Application:
   - Prepare addon directory
   - Register new addon into the apps
     Output: Able to create empty module, register new module into apps
5. Models and basic fields:
   - Automatic fields
   - models and fields module
     Output: Able to create basic model
6. Security:
   - Data access right can be defined in ir.model.access.csv
     Output: Defined access right for estate.property model and register it in manifest
7. UI:
   - Learn about root menu, first level menu and action.
   - Learn about tree, list and form view
     Output: Able to create basic tree and form view.

Solution to be implemented:

1. Model & Business logic:
   Problems:
   1. Extends existing hr.attendance model and add additional specified in the testcase.
   2. Create new model wit specified fields in the testcase. However, i cannot find "Time" data type so i just borrowed data type used for "work from" and "work to" in module "resource".
   3. Features:
      - Find a way to convert check-in datetime type into hours, then substract converted check-in with start_time + grace_periods.
      - Convert check-out into hours, substract check-out with end_time
      - -
      - -
2. UI:
   Problems:
   1. -
   2. -
   3. -
   4. -
