import inspect

from typing import Type, Dict


class Plugin:
    def __init__(self, *, cls_name: str, module_name: str, cls: Type):
        self.class_name = cls_name
        self.module_name = module_name
        self.cls = cls
        self.params: Dict[str, str] = self._get_constructor_params(cls)

    def _get_constructor_params(self, cls: Type) -> Dict[str, str]:
        init_func = cls.__init__

        sig = inspect.signature(init_func)

        params = {}

        for name, param in sig.parameters.items():
            if name != "self":
                param_type = (
                    param.annotation
                    if param.annotation != inspect._empty
                    else "Unknown"
                )
                params[name] = param_type

        return params

    def __str__(self):
        return f"{self.class_name}"

    def __repr__(self):
        return self.__str__()
