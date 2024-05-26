#!/usr/bin/env python
from ansible.plugins.action import ActionBase

# Defines key/value pairs of facts to pass onto custom module
# key = name to use on backend
# value = name of actual Ansible fact to capture
DEFAULT_FACTS = {
    "ansible_connection": "ansible_connection",
    "ansible_groups": "group_names",
    "ansible_host": "ansible_host", "ansible_hostname": "inventory_hostname",
    "ansible_port": "ansible_port", "ansible_user": "ansible_user",
    "guest_os": "ansible_os_family"
}


class ActionModule(ActionBase):
    def run(self, tmp=None, task_vars=None):
        super(ActionModule, self).run(tmp, task_vars)
        module_args = self._task.args.copy()
        for key, value in DEFAULT_FACTS.items():
            module_args[key] = self._templar._available_variables.get(value)
        return self._execute_module(module_args=module_args,
                                    task_vars=task_vars, tmp=tmp)
