#!/usr/bin/python

from ansible.module_utils.basic import *
from ansible.module_utils.bla import bla_utils

module = AnsibleModule(
    argument_spec = dict()
)
module.exit_json(changed=True, hello=bla_utils())
