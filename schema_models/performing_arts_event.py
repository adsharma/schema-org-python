from dataclasses import dataclass

from schema_models.event import Event


@dataclass
class PerformingArtsEvent(Event):
    """
    Live performance <a class="localLink" href="http://schema.org/Event">Event of the performing arts (music, theatre, dance, acrobatics, spoken word), including performance art and performative sports (e.g. choreographed forms of martial arts, figure skating, competitive ballroom dancing).<br/><br/>Note: Use <a class="localLink" href="http://schema.org/additionalType">additionalType</a> to differentiate between productions / shows (PerformanceWork, EventSeries), tours (EventSeries), and individual performances.
    """
