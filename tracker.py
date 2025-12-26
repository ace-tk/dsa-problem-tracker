problems = []          
problem_map = {}     
topic_map = {}
counter = 1


def add_problem(title, topic, difficulty):
    global counter
    problem = {
        "id": counter,
        "title": title,
        "topic": topic,
        "difficulty": difficulty,
        "solved": False
    }
    problems.append(problem)
    problem_map[counter] = problem

    if topic not in topic_map:
        topic_map[topic] = []
    topic_map[topic].append(counter)

    counter += 1


def mark_solved(pid):
    if pid in problem_map:
        problem_map[pid]["solved"] = True
    else:
        print("Problem not found")


def show_by_topic(topic):
    if topic not in topic_map:
        print("No problems under this topic")
        return

    for pid in topic_map[topic]:
        p = problem_map[pid]
        status = "Solved" if p["solved"] else "Unsolved"
        print(p["id"], p["title"], "-", status)


def performance_analysis():
    total = len(problems)
    solved = sum(1 for p in problems if p["solved"])
    print("Total Problems:", total)
    print("Solved:", solved)
    print("Unsolved:", total - solved)


while True:
    print("\nDSA Problem Tracker")
    print("1. Add Problem")
    print("2. Mark Problem Solved")
    print("3. Show Problems by Topic")
    print("4. Performance Analysis")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        title = input("Problem title: ")
        topic = input("Topic (Array/Tree/Graph): ")
        difficulty = input("Difficulty (Easy/Medium/Hard): ")
        add_problem(title, topic, difficulty)

    elif choice == "2":
        pid = int(input("Enter problem ID: "))
        mark_solved(pid)

    elif choice == "3":
        topic = input("Enter topic: ")
        show_by_topic(topic)

    elif choice == "4":
        performance_analysis()

    elif choice == "5":
        break

    else:
        print("Invalid choice")
