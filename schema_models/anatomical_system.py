from typing import List, Optional, Union

from schema_models.medical_entity import MedicalEntity


class AnatomicalSystem(MedicalEntity):
    """
    An anatomical system is a group of anatomical structures that work together to perform a certain task. Anatomical systems, such as organ systems, are one organizing principle of anatomy, and can include circulatory, digestive, endocrine, integumentary, immune, lymphatic, muscular, nervous, reproductive, respiratory, skeletal, urinary, vestibular, and other systems.
    """

    relatedCondition: Optional[Union["MedicalCondition", List["MedicalCondition"]]] = (
        None
    )
    relatedStructure: Optional[
        Union["AnatomicalStructure", List["AnatomicalStructure"]]
    ] = None
    relatedTherapy: Optional[Union["MedicalTherapy", List["MedicalTherapy"]]] = None
    associatedPathophysiology: Optional[Union[str, List[str]]] = None
    comprisedOf: Optional[
        Union[
            "AnatomicalStructure",
            List["AnatomicalStructure"],
            "AnatomicalSystem",
            List["AnatomicalSystem"],
        ]
    ] = None
