from setup import setup_query_engine, setup_agent, setup_tools, setup_backup_tool


def main():
    backup_tool = setup_backup_tool()
    try:
        directory_path = "../data"
        query_engine = setup_query_engine(directory_path)
        tools = setup_tools(query_engine)
        agent = setup_agent(tools)

        while True:
            prompt = input("Enter a prompt (q to quit): ")
            if prompt == "q":
                break
            result = agent.query(prompt)
            print(result)
    except Exception as e:
        print(f"An error occurred: {e}")

        result = backup_tool()
        print(result)


if __name__ == "__main__":
    main()
