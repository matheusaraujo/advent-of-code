# brew install graphviz
# pip install graphviz

from graphviz import Digraph


def render_graph(file_name):
    dot = Digraph()

    with open(f"{file_name}.txt", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if line:
                node, targets = line.split(" -> ")
                targets = targets.split(", ")
                if node == "broadcaster":
                    dot.node("broadcaster", shape="box")
                elif node[0] == "%":
                    node = node[1:]
                    if len(targets) != 1:
                        dot.node(node, color="blue", shape="cds")
                    else:
                        dot.node(
                            node,
                            color="blue",
                            shape="cds",
                            style="filled",
                            fillcolor="cornflowerblue",
                        )
                elif node[0] == "&":
                    node = node[1:]
                    dot.node(node, color="red", shape="hexagon")

                for target in targets:
                    dot.edge(node, target)

    dot.engine = "dot"
    dot.graph_attr["rankdir"] = "LR"

    dot.node("rx", shape="doublecircle")

    dot.render(f"_{file_name}", format="png", cleanup=True)


# render_graph("sample-input-1a")
render_graph("input")
