import re

def load_project_overview(path="data/Project_Overview.txt"):
    """Load the entire Project_Overview.txt file."""
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def extract_agent_definition(content, agent_name):
    """
    Extract the definition of a specific agent from the Project Overview.
    Captures everything after '<Agent Name> Definition' until the next agent header or EOF.
    """
    pattern = rf"{agent_name}\s*Definition\s*-+\s*([\s\S]*?)(?=\n[A-Z][^\n]*Definition|\Z)"
    match = re.search(pattern, content, re.IGNORECASE)
    if match:
        return match.group(1).strip()
    else:
        raise ValueError(f"Agent definition for '{agent_name}' not found.")

def extract_global_rules(content):
    """Extract the Global Project Rules section from the Project Overview."""
    pattern = r"(Global Project Rules.*?)(?=\n\d+\.|\Z)"
    match = re.search(pattern, content, re.DOTALL | re.IGNORECASE)
    return match.group(1).strip() if match else "No Global Rules Found"

