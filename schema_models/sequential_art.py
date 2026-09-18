from dataclasses import dataclass

from schema_models.book import Book


@dataclass
class SequentialArt(Book):
    """
    An art forms that use images deployed in a specific order for the purpose of graphic storytelling (i.e., narration of graphic stories) or conveying information. Examples of SequentialArt are Franco-Belgian Bande Dessinée, Comics in the USA and 漫画 (Manga) in Japan.
    """
