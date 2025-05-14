# resume-optimizer-ai
 from fastapi import FastAPI, Body
from resume_optimizer.optimizer import optimize_resume

app = FastAPI()

@app.post("/optimize")
def generate_optimized_resume(
    master_resume: str = Body(...),
    job_description: str = Body(...),
    openai_key: str = Body(...)
):
    result = optimize_resume(master_resume, job_description, openai_key)
    return {"optimized_resume": result}
       
