"""The Python script is run as written: '${' in it is not a flowchart variable
(seamm 2026.11.6 expands '${...}' in text parameters)."""

import custom_step


def test_script_is_not_expanded():
    parameters = custom_step.CustomParameters()
    parameters["script"].value = 'print("${not_a_variable}")'
    values = parameters.current_values_to_dict(context={})
    assert values["script"] == 'print("${not_a_variable}")'
