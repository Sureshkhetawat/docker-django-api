from typing import List, Dict, Callable, Tuple
SlotValidationResult = Tuple[bool, bool, str, Dict]

def validate_numeric_entity(values: List[Dict], invalid_trigger: str = None, key: str = None,
                            support_multiple: bool = True, pick_first: bool = False, constraint=None, var_name=None,
                            **kwargs) -> SlotValidationResult:
    """
    Validate an entity on the basis of its value extracted.
    The method will check if that value satisfies the numeric constraints put on it.
    If there are no numeric constraints, it will simply assume the value is valid.

    If there are numeric constraints, then it will only consider a value valid if it satisfies the numeric constraints.
    In case of multiple values being extracted and the support_multiple flag being set to true, the extracted values
    will be filtered so that only those values are used to fill the slot which satisfy the numeric constraint.

    If multiple values are supported and even 1 value does not satisfy the numeric constraint, the slot is assumed to be
    partially filled.

    :param pick_first: Set to true if the first value is to be picked up
    :param support_multiple: Set to true if multiple utterances of an entity are supported
    :param values: Values extracted by NLU
    :param invalid_trigger: Trigger to use if the extracted value is not supported
    :param key: Dict key to use in the params returned
    :param constraint: Conditional expression for constraints on the numeric values extracted
    :param var_name: Name of the var used to express the numeric constraint
    :return: a tuple of (filled, partially_filled, trigger, params)
    """

    if len(values)==0:
        return (False, False, invalid_trigger, {})

    parameters = {}
    parameters[key] = []

    constraint = constraint.replace(var_name,"{0}")

    print(type(values[0]['value']))

    for valuedict in values:
        if type(valuedict['value'])==int and eval(constraint.format(valuedict['value'])):
            parameters[key].append(valuedict['value'])

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

    if pick_first==False and support_multiple==False:
        # print("Input format is wrong")
        raise Exception("Does not this request")
    
    if pick_first==True and len(parameters[key])>0:
        parameters[key] = parameters[key][0]

    return (filled, partially_filled, trigger, parameters)