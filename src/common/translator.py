from json import loads
from pathlib import Path
from typing import Self

from cachetools import TTLCache

from src._types import LangsEnum

_Translations = dict[str, dict[str, str]]


class Translator:
    """Singleton class for translating data."""

    __instance: Self | None = None

    _translations: TTLCache[LangsEnum, _Translations] = TTLCache(
        maxsize=10,
        ttl=3600,
    )

    def __new__(cls) -> Self:
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    @staticmethod
    def _to_lang(lang: LangsEnum | str) -> LangsEnum:
        """Convert the lang to LangsEnum."""
        if isinstance(lang, LangsEnum):
            return lang

        try:
            return LangsEnum(lang)
        except ValueError:
            return LangsEnum.EN
        # Default to English if the lang is not valid or not supported

    @staticmethod
    def _load_json(lang: LangsEnum) -> None:
        """Load all items from the database."""

        Translator._translations[lang] = dict(
            loads(Path(f"src/locales/{lang}/Game.json").read_bytes()),
        )

    @staticmethod
    def _find_key(lang: LangsEnum, namespace: str, key: str) -> str | None:
        """Find the key in the translations."""

        for t_namespace, t_keys in Translator._translations[lang].items():
            if namespace.lower() == t_namespace.lower():
                for t_key, t_value in t_keys.items():
                    if key.lower() == t_key.lower():
                        return t_value

        return None

    @staticmethod
    def _translate_data(
        lang: LangsEnum,
        namespace: str,
        key: str,
    ) -> str | None:
        """Translate the data to the simple model."""
        if lang not in Translator._translations:
            Translator._load_json(lang=lang)

        if (
            namespace not in Translator._translations[lang]
            or key not in Translator._translations[lang][namespace]
        ):
            return Translator._find_key(lang, namespace, key)

        return Translator._translations[lang][namespace][key]

    @staticmethod
    def translate(lang: LangsEnum | str, key: str) -> str:
        """Translate the data to the simple model."""
        lang = Translator._to_lang(lang)

        namespace, key_ = key.split(".")

        string = Translator._translate_data(
            lang=lang,
            namespace=namespace,
            key=key_,
        )

        if string is None and lang != LangsEnum.EN:
            lang = LangsEnum.EN
            string = Translator._translate_data(
                lang=LangsEnum.EN,
                namespace=namespace,
                key=key_,
            )

        if string is None and lang == LangsEnum.EN:
            string = Translator._translate_data(
                lang=LangsEnum.ZH_CN,
                namespace=namespace,
                key=key_,
            )

        if string is None:
            return key

        return string
