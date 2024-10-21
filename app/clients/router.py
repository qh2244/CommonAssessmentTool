from fastapi import APIRouter, HTTPException
from app.clients.service.logic import interpret_and_calculate
from app.clients.schema import PredictionInput
from app.clients.database import get_db_connection

router = APIRouter(prefix="/clients", tags=["clients"])

@router.post("/predictions")
async def predict(data: PredictionInput):
    # Input data to SQLite
    conn = get_db_connection()
    conn.execute('''
        INSERT INTO clients (age, gender, work_experience, canada_workex, dep_num, canada_born,
                             citizen_status, level_of_schooling, fluent_english, reading_english_scale,
                             speaking_english_scale, writing_english_scale, numeracy_scale, computer_scale,
                             transportation_bool, caregiver_bool, housing, income_source, felony_bool,
                             attending_school, currently_employed, substance_use, time_unemployed,
                             need_mental_health_support_bool)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (data.age, data.gender, data.work_experience, data.canada_workex, data.dep_num, data.canada_born,
          data.citizen_status, data.level_of_schooling, data.fluent_english, data.reading_english_scale,
          data.speaking_english_scale, data.writing_english_scale, data.numeracy_scale, data.computer_scale,
          data.transportation_bool, data.caregiver_bool, data.housing, data.income_source, data.felony_bool,
          data.attending_school, data.currently_employed, data.substance_use, data.time_unemployed,
          data.need_mental_health_support_bool))
    conn.commit()
    conn.close()

    return {
        "prediction_result": interpret_and_calculate(data.model_dump())
    }

# get client by id
@router.get("/{client_id}")
async def get_client(client_id: int):
    conn = get_db_connection()
    client = conn.execute('SELECT * FROM clients WHERE id = ?', (client_id,)).fetchone()
    conn.close()
    if client is None:
        raise HTTPException(status_code=404, detail="Client not found")
    return dict(client)
