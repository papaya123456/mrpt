from typing import Dict

from typing import overload

class CRuntimeCompiledExpression:
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, arg0: CRuntimeCompiledExpression) -> None: ...
    def assign(self) -> CRuntimeCompiledExpression: ...
    @overload
    def compile(self, expression: str) -> None: ...
    @overload
    def compile(self, expression: str, variables: Dict[str,float]) -> None: ...
    @overload
    def compile(self, expression: str, variables: Dict[str,float], expr_name_for_error_reporting: str) -> None: ...
    @overload
    def eval(self) -> float: ...
    @overload
    def eval() -> double: ...
    def get_original_expression(self) -> str: ...
    @overload
    def is_compiled(self) -> bool: ...
    @overload
    def is_compiled() -> bool: ...
    @overload
    def register_function(self, name: str, func) -> None: ...
    @overload
    def register_function(conststd, constclassstd) -> void: ...
    @overload
    def register_function(self, name: str, func) -> None: ...
    @overload
    def register_function(conststd, constclassstd) -> void: ...
    @overload
    def register_function(self, name: str, func) -> None: ...
    @overload
    def register_function(conststd, constclassstd) -> void: ...
    @overload
    def register_function(self, name: str, func) -> None: ...
    @overload
    def register_function(conststd, constclassstd) -> void: ...