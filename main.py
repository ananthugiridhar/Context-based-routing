from typing import NewType
import graph_data
import nodes
import edges
import network
import optimal_path
import project


def main():
    prompt = "select the function you want to perform\n     1. show the nodes\n     2. deploy the edges\n     3. deploy the network\n     4. find the optimal path\n     5. project implimentaion\n  \n  selection :   "
    choice = input(prompt)

    if choice == "1":
        nodes.node()
    elif choice == '2':
        edges.run()
    elif choice == '3':
        network.deploy_network()
    elif choice == '4':
        optimal_path.dijkstra()
    elif choice == '5':
        project.project()

    else:
        print("give a valid choice")


main()
