base_single_import = "import {{package_list}}\n"
base_from_import = "from {{module}} import {{component_list}}\n"
base_flow_template_decorator = "@flow({{arguments}})\n"
base_task_template_decorator = "@task({{arguments}})\n"
function_header = "def {{function_name}}({{argument_list}}):\n"
pass_command = "pass\n"
task_flow_from_import = "from prefect import task, flow\n"
                     