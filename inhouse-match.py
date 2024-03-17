def read_file(file_path):
    """Read text from a file."""
    with open(file_path, 'r') as file:
        text = file.read()
    return text

def match_resume_to_job(resume_text, job_description_text):
    """Match resume to job description."""
    resume_words = resume_text.lower().split()
    job_description_words = job_description_text.lower().split()
    
    matched_words = set(resume_words) & set(job_description_words)
    
    return matched_words

# Read resume and job description from files
resume_file_path = 'resume.txt'
job_description_file_path = 'job_description.txt'

resume_text = read_file(resume_file_path)
job_description_text = read_file(job_description_file_path)

# Match resume to job description
matched_words = match_resume_to_job(resume_text, job_description_text)

print("Matched words between resume and job description:")
for word in matched_words:
    print("-", word)
