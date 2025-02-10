from schema_models.learning_resource import LearningResource


class Syllabus(LearningResource):
    """
    A syllabus that describes the material covered in a course, often with several such sections per [[Course]] so that a distinct [[timeRequired]] can be provided for that section of the [[Course]].
    """
