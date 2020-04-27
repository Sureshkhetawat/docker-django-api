from typing import List, Dict, Callable, Tuple
SlotValidationResult = Tuple[bool, bool, str, Dict]

def validate_finite_values_entity(values: List[Dict], supported_values: List[str] = None,
                                invalid_trigger: str = None, key: str = None,
                                support_multiple: bool = True, pick_first: bool = False, **kwargs) -> SlotValidationResult:
    """
    Validate an entity on the basis of its value extracted.
    The method will check if the values extracted("values" arg) lies within the finite list of supported values(arg "supported_values").

    :param pick_first: Set to true if the first value is to be picked up
    :param support_multiple: Set to true if multiple utterances of an entity are supported
    :param values: Values extracted by NLU
    :param supported_values: List of supported values for the slot
    :param invalid_trigger: Trigger to use if the extracted value is not supported
    :param key: Dict key to use in the params returned
    :return: a tuple of (filled, partially_filled, trigger, params)
    """

    if len(values)==0:
        return (False, False, invalid_trigger, {})
    
    parameters = {}
    parameters[key] = []
    for valuedict in values:
        if valuedict['value'] in supported_values:
            parameters[key].append(valuedict['value'].upper())
    
    if len(values) == len(parameters[key]):
        filled = True
        partially_filled = False
        trigger = ""
    else:
        filled = False
        trigger = invalid_trigger
        if len(parameters[key])>0:     # subset of values are valid
            partially_filled = True
        else:
            if len(values)>0:
                partially_filled = True
            else:
                partially_filled = False
        parameters = {}
    
    if pick_first==False and support_multiple==False:
        raise Exception("Check testcase")

    if pick_first==True:
        parameters[key] = parameters[key][0]

    return (filled, partially_filled, trigger, parameters)