from typing import Any, Dict

from .model import ExceptionModel


class DocsApi:
    @classmethod
    def create_error_responses(cls, *args: ExceptionModel) -> Dict[Any, Any]:
        responses: Dict[int | str, Dict[str, Any]] = {
            422: {
                "content": {
                    "application/json": {
                        "examples": {
                            f"FastApiError": {
                                "value": {
                                    "detail": [
                                        {
                                            "loc": ["string", 0],
                                            "msg": "string",
                                            "type": "string",
                                        }
                                    ]
                                },
                            },
                        }
                    }
                },
            }
        }
        for basemodel in args:
            if basemodel.status not in responses:
                responses.update(
                    {
                        basemodel.status: {
                            "content": {
                                "application/json": {
                                    "examples": {
                                        f"{basemodel.__class__.__name__}": {
                                            "value": basemodel.model_dump(mode='json'),
                                        },
                                    }
                                }
                            },
                        }
                    }
                )
            else:
                responses[basemodel.status]["content"]["application/json"][
                    "examples"
                ].update({basemodel.__class__.__name__: {"value": basemodel.model_dump(mode='json')}})
        return responses