# Universal Skill-Based Recommendation System (135 lines)
# DSA: Dictionary, List, Set, Merge Sort | 10+ Roles Per Domain (40+ Total)

# MULTI-DOMAIN SKILL MAPPING - 10+ ROLES EACH (Dictionary of Sets)
skill_databases = {
    "Software Jobs": {
        "Frontend Developer": {"html", "css", "javascript", "react", "angular", "vue", "typescript", "tailwind"},
        "Backend Developer": {"python", "django", "flask", "node.js", "sql", "api", "c#", "java", "spring", ".net"},
        "Data Scientist": {"python", "pandas", "numpy", "ml", "statistics", "sql", "scikit-learn", "tensorflow"},
        "DevOps Engineer": {"docker", "kubernetes", "aws", "jenkins", "linux", "ci/cd", "terraform", "ansible"},
        "Fullstack Developer": {"html", "css", "python", "react", "sql", "api", "javascript", "node.js"},
        "Mobile Developer": {"swift", "kotlin", "flutter", "react native", "java", "dart", "xcode", "android studio"},
        "Database Admin": {"sql", "mysql", "postgresql", "mongodb", "oracle", "redis", "backup", "performance tuning"},
        "QA Engineer": {"selenium", "testing", "pytest", "jira", "automation", "cypress", "postman", "load testing"},
        "Cloud Engineer": {"aws", "azure", "gcp", "terraform", "docker", "kubernetes", "serverless", "vpc"},
        "Cybersecurity": {"firewall", "encryption", "penetration", "network security", "siem", "ids/ips", "malware analysis"},
        "UI/UX Designer": {"figma", "sketch", "prototyping", "user research", "adobe xd", "wireframing", "usability"},
        "Blockchain Dev": {"solidity", "ethereum", "smart contracts", "web3", "rust", "hyperledger", "ipfs"}
    },
    "Healthcare Jobs": {
        "General Doctor": {"anatomy", "diagnosis", "medicine", "patient care", "medical ethics", "emergency response"},
        "Surgeon": {"surgery", "anatomy", "sterilization", "patient care", "surgical tools", "post-op care"},
        "Nurse": {"patient care", "medicine", "vital signs", "empathy", "wound care", "iv therapy", "catheterization"},
        "Pharmacist": {"medicine", "dosage", "pharmacy", "counseling", "drug interaction", "inventory management"},
        "Dentist": {"teeth", "oral surgery", "xray", "filling", "root canal", "braces", "periodontics"},
        "Radiologist": {"xray", "mri", "ct scan", "image analysis", "ultrasound", "pet scan", "radiology reporting"},
        "Physiotherapist": {"exercise", "rehabilitation", "muscle therapy", "electrotherapy", "manual therapy"},
        "Anesthesiologist": {"anesthesia", "pain management", "surgery support", "ventilation", "monitoring"},
        "Pediatrician": {"child care", "vaccination", "growth monitoring", "neonatology", "developmental assessment"},
        "Psychiatrist": {"mental health", "therapy", "medication", "counseling", "psychopharmacology", "crisis intervention"},
        "Lab Technician": {"blood test", "microscope", "sample analysis", "pcr", "centrifugation", "quality control"}
    },
    "Business Jobs": {
        "Marketing Manager": {"marketing", "social media", "analytics", "campaigns", "seo", "content strategy", "brand management"},
        "Sales Executive": {"communication", "negotiation", "sales", "relationship", "cold calling", "closing deals", "crm"},
        "Accountant": {"accounting", "taxes", "excel", "financial report", "gaap", "audit", "bookkeeping"},
        "HR Manager": {"recruitment", "training", "employee relations", "payroll", "performance review", "compliance"},
        "Financial Analyst": {"excel", "forecasting", "budgeting", "analysis", "valuation", "financial modeling", "tableau"},
        "Project Manager": {"planning", "team management", "budget", "timeline", "risk management", "agile", "scrum"},
        "Business Analyst": {"requirements", "process mapping", "stakeholder", "data analysis", "sql", "visio"},
        "Operations Manager": {"logistics", "supply chain", "process optimization", "inventory", "vendor management"},
        "Customer Support": {"communication", "problem solving", "empathy", "ticketing", "escalation", "documentation"},
        "Entrepreneur": {"business plan", "networking", "risk management", "fundraising", "pitching", "market research"},
        "Legal Advisor": {"contracts", "compliance", "regulations", "litigation", "corporate law", "intellectual property"}
    },
    "Creative Jobs": {
        "Graphic Designer": {"photoshop", "illustrator", "typography", "color theory", "indesign", "branding"},
        "Content Writer": {"writing", "seo", "research", "grammar", "copywriting", "blogging", "editing"},
        "Video Editor": {"premiere", "after effects", "color grading", "motion graphics", "davinci resolve", "sound editing"},
        "Photographer": {"photoshop", "lighting", "composition", "camera", "lens knowledge", "post processing"},
        "Animator": {"blender", "after effects", "3d modeling", "rigging", "maya", "unity", "keyframing"},
        "Fashion Designer": {"sketching", "sewing", "fabric knowledge", "trends", "pattern making", "draping"},
        "Interior Designer": {"space planning", "3d rendering", "color schemes", "autocad", "sketchup", "furniture design"},
        "Music Producer": {"ableton", "mixing", "mastering", "sound design", "fl studio", "logic pro", "synths"},
        "Architect": {"autocad", "3d modeling", "structural design", "revit", "bim", "sustainable design"},
        "Copywriter": {"advertising", "persuasive writing", "brand voice", "headlines", "a/b testing"},
        "Web Designer": {"figma", "html", "css", "user experience", "webflow", "responsive design"}
    }
}

def manual_set_intersection(student_skills, job_skills):
    """Manual set intersection"""
    
    student_set = set(student_skills)
    job_set = set(job_skills)
    common_skills = set()
    for skill in student_set:
        if skill in job_set:
            common_skills.add(skill)
    
    return common_skills

def skill_match_score(student_skills, job_skills, gpa):
    """Core scoring algorithm"""
    
    common_skills = manual_set_intersection(student_skills, job_skills)
    match_count = len(common_skills)
    total_job_skills = len(job_skills)
    skill_ratio = match_count / total_job_skills
    gpa_weight = gpa / 10
    score = skill_ratio * gpa_weight * 100
    
    return round(score, 1)

def merge(left, right):
    """Merge Sort helper"""
    
    result = []
    i,j = 0,0
    
    while (i < len(left) and j < len(right)):
        if (left[i][1] >= right[j][1]):
            result.append(left[i])
            i = i + 1
        else:
            result.append(right[j])
            j = j + 1
    
    
    result=result+left[i:]
    result=result+right[j:]
    return result

def merge_sort(scores):
    """Merge Sort - O(n log n)"""
    
    if (len(scores) <= 1):
        return scores
    mid = len(scores) // 2
    left = merge_sort(scores[:mid])
    right = merge_sort(scores[mid:])
    
    return merge(left, right)

def generate_recommendations(student, domain="Software Jobs"):
    """Generate top 3 recommendations per domain"""
    
    job_roles = skill_databases[domain]
    scores = []
    
    for job, skills in job_roles.items():
        score = skill_match_score(student["skills"], skills, student["gpa"])
        scores.append((job, score))
    
    return merge_sort(scores)[:3]

def format_recommendation(job, score):
    """Formatted output"""
    quality=""
    if(score>=80):
        quality = "🔥  Perfect"
    elif(score>=60):
        quality = "✅  Very good"
    else:
        quality = "➡️  Good"
    # quality = "🔥" if score >= 80 else "✅" if score >= 60 else "➡️" #if Comprehension
    
    return f"{job:<20} {score:>5}% {quality}"

def show_results(student, domain):
    """Display results"""
    
    print(f"\n{domain:^50}")
    print(f"{student['name']:>12} | GPA: {student['gpa']:>4}")
    print(f"Skills: {', '.join(student['skills'])}")
    recs = generate_recommendations(student, domain)
    
    for job, score in recs:
        print(format_recommendation(job, score))

# MAIN EXECUTION - 40+ Job Roles Demo
print("🌍 UNIVERSAL SKILL SYSTEM | 40+ JOBS (10+ per domain)")
print("Software | Healthcare | Business | Creative\n" + "-"*65)

demo_students = [
    {"name": "Rahul", "skills": ["python", "sql", "excel"], "gpa": 8.7},
    {"name": "Priya", "skills": ["patient care", "medicine"], "gpa": 8.2},
    {"name": "Amit", "skills": ["marketing", "excel", "communication"], "gpa": 9.1},
    {"name": "Sneha", "skills": ["photoshop", "writing"], "gpa": 8.5}
]

domains = ["Software Jobs", "Healthcare Jobs", "Business Jobs", "Creative Jobs"]
for student, domain in zip(demo_students, domains):
    show_results(student, domain)

# Interactive mode
print("\n🎯 Test any combination:")
while True:
    name = input("\nName (quit): ").strip()
    if name.lower() == 'quit':
        break
    skills = [s.strip() for s in input("Skills: ").lower().split(',') if s.strip()]
    domain = input("Domain: ").strip() or "Software Jobs"
    gpa = float(input("GPA: "))
    show_results({"name": name, "skills": skills, "gpa": gpa}, domain)

print("\nDSA: Dict(44 roles), List, Set Intersection, Merge Sort")