"""
This module defines the schema for client data used in the application.

Classes:
- PredictionInput: Represents the input data required for client-related operations.
"""

from pydantic import BaseModel

class PredictionInput(BaseModel):
    """
    Schema for client prediction input data.

    Attributes:
        age (int): Age of the client.
        gender (str): Gender of the client.
        work_experience (int): Total work experience in years.
        canada_workex (int): Work experience in Canada (in years).
        dep_num (int): Number of dependents.
        canada_born (str): Whether the client was born in Canada.
        citizen_status (str): Citizenship status of the client.
        level_of_schooling (str): Highest level of education completed.
        fluent_english (str): Fluency in English.
        reading_english_scale (int): Reading English proficiency scale.
        speaking_english_scale (int): Speaking English proficiency scale.
        writing_english_scale (int): Writing English proficiency scale.
        numeracy_scale (int): Numeracy proficiency scale.
        computer_scale (int): Computer proficiency scale.
        transportation_bool (str): Availability of transportation.
        caregiver_bool (str): Whether the client is a caregiver.
        housing (str): Current housing situation.
        income_source (str): Primary source of income.
        felony_bool (str): Whether the client has a felony history.
        attending_school (str): Whether the client is attending school.
        currently_employed (str): Whether the client is currently employed.
        substance_use (str): Substance use history of the client.
        time_unemployed (int): Duration of unemployment in months.
        need_mental_health_support_bool (str): Whether the client needs mental health support.
    """
    age: int
    gender: str
    work_experience: int
    canada_workex: int
    dep_num: int
    canada_born: str
    citizen_status: str
    level_of_schooling: str
    fluent_english: str
    reading_english_scale: int
    speaking_english_scale: int
    writing_english_scale: int
    numeracy_scale: int
    computer_scale: int
    transportation_bool: str
    caregiver_bool: str
    housing: str
    income_source: str
    felony_bool: str
    attending_school: str
    currently_employed: str
    substance_use: str
    time_unemployed: int
    need_mental_health_support_bool: str
