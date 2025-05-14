# resume-optimizer-api
The ATS won't know what hit it. 
import openai

def optimize_resume(master_resume, job_description, openai_api_key):
    openai.api_key = openai_api_key

    prompt = f"""
You are a professional resume optimization assistant. Given the following master resume and job description, output a new, optimized resume tailored for the specific job. Keep the tone professional, the formatting ATS-friendly, and focus on matching the language and skills from the job description.

MASTER RESUME:
{master_resume}

JOB DESCRIPTION:
{job_description}

OUTPUT:
Optimized resume:
"""

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.3
    )

    return response['choices'][0]['message']['content'].strip()

