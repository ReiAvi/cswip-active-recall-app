from agents.agent_loader import load_project_overview, extract_agent_definition, extract_global_rules

def main():
    # Load Project Overview file
    content = load_project_overview()

    # Display Global Rules at startup
    print("=== Global Project Rules ===")
    print(extract_global_rules(content))
    print("\n")

    # Interactive loop for agent loading
    while True:
        agent_name = input("Enter agent name (or 'exit' to quit): ").strip()
        if agent_name.lower() == 'exit':
            break
        try:
            definition = extract_agent_definition(content, agent_name)
            print(f"\n=== {agent_name} ===")
            print(definition)
            print("\n")
        except ValueError as e:
            print(e)
            print("Try again. Ensure the name matches the section header in Project_Overview.txt.\n")

if __name__ == "__main__":
    main()
