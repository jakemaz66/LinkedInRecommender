from langchain.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import List

#Creating Person Intel Class to collect serialized data
class PersonIntel(BaseModel):
    summary: str = Field(description="Summary of the person")
    facts: List[str] = Field(description="Interesting facts about the person")
    qualifications: List[str] = Field(
        description="Qualifications and education of the person"
    )
    argument: List[str] = Field(
        description="Argument for their performance"
    )

    def to_dict(self):
        return {
            "summary": self.summary,
            "facts": self.facts,
            "qualifications": self.qualifications,
            "argument": self.argument,
        }

person_intel_parser: PydanticOutputParser = PydanticOutputParser(
    pydantic_object=PersonIntel
)