import chromadb

client = chromadb.Client()

collection = client.create_collection(name="doc_genai")

documents = ["AI Engineer: Learn Python, machine learning, deep learning, and APIs. Build AI applications using LLMs.",
    "Data Scientist: Learn Python, SQL, statistics, data visualization, and machine learning.",
    "Cybersecurity Analyst: Learn networking, Linux, security fundamentals, threat detection, and incident response.",
    "Full Stack Developer: Learn HTML, CSS, JavaScript, React, backend development, databases, and APIs.",
    "AI Automation Engineer: Learn Python, LLM APIs, workflow automation, RAG, and tools such as LangChain.",
    "Machine Learning Engineer: Learn Python, model training, feature engineering, deployment, and MLOps.",
    "Beginner AI Roadmap: Start with Python, learn basic statistics, practice machine learning, then build projects.",
    "AI Portfolio Projects: Build a chatbot, document question-answering system, AI agent, and resume analyzer."
]

collection.add(
    ids=["career_ai_engineer",
    "career_data_scientist",
    "career_cybersecurity",
    "career_fullstack",
    "career_ai_automation",
    "career_ml_engineer",
    "roadmap_ai_beginner",
    "projects_ai_portfolio"],
    documents=documents
)

result = collection.query(
    query_texts=["i know python basics which field i choose"],
    n_results=2
)

print(result)