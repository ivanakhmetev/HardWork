def normalize_type(type_, level=0):
    """
    Reduces an arbitrarily complex type declaration into something manageable.
    """
    if not typing or not isinstance(type_, typing.TypingMeta) or type_ is AnyType: 
        return type_  
    if isinstance(type_, typing.TypeVar):
        if type_.__constraints__ or type_.__bound__:
            return type_
        else:
            return AnyType
    if issubclass(type_, typing.Union):
        if not type_.__union_params__:
            raise OverloadingError("typing.Union must be parameterized")
        return typing.Union[tuple(normalize_type(t, level) for t in type_.__union_params__)]
    if issubclass(type_, typing.Tuple):
        params = type_.__tuple_params__
        if level > 0 or params is None:
            return typing.Tuple
        elif type_.__tuple_use_ellipsis__:
            return typing.Tuple[normalize_type(params[0], level + 1), ...]
        else:
            return typing.Tuple[tuple(normalize_type(t, level + 1) for t in params)]
    if issubclass(type_, typing.Callable):
        return typing.Callable
    if isinstance(type_, typing.GenericMeta):
        base = find_base_generic(type_)
        if base is typing.Generic:
            return type_
        else:
            return GenericWrapper(type_, base, level > 0)
    raise OverloadingError("%r not supported yet" % type_)

#########################

def is_normalization_need(my_type):
    if not isinstance(my_type, typing.TypingMeta):
        return False
    if my_type is AnyType:
        return False
    if isinstance(my_type, typing.TypeVar) and my_type.__constraints__:
        return False
    if isinstance(my_type, typing.TypeVar) and type_.__bound__:
        return False
    return True

def manage_instance(mytype, typing.TypeVar):
    if mytype.__constraints__:
        return mytype
    if mytype.__bound__:
        return mytype
    return AnyType

def manage_instance(mytype, level, typing.GenericMeta):
    base = find_base_generic(mytype)
    if base is typing.Generic:
        return mytype
    return GenericWrapper(mytype, base, level > 0)

def manage_sub(mytype, level, typing.Union):
    if not mytype.__union_params__:
        raise OverloadingError("typing.Union must be parameterized")
    return typing.Union[tuple(normalize_type(t, level) for t in mytype.__union_params__)]








    
    

