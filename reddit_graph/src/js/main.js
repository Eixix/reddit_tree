import Sigma from "sigma";
import Graph from "graphology";
import ForceSupervisor from "graphology-layout-force/worker";


fetch('/reddit_sigma.json')
    .then(response => response.json())
    .then(data => {
        const container = document.getElementById("container");

        const graph = new Graph();

        data.nodes.forEach(node => graph.addNode(node.id))
        data.edges.forEach(edge => graph.addEdge(edge.source, edge.target))

        console.log(graph);

        graph.nodes().forEach((node, i) => {
            const angle = (i * 2 * Math.PI) / graph.order;
            graph.setNodeAttribute(node, "x", 100 * Math.cos(angle));
            graph.setNodeAttribute(node, "y", 100 * Math.sin(angle));
        });

        const renderer = new Sigma(graph,
            container);

        const layout = new ForceSupervisor(graph)
        layout.start()


        // const layout = new FA2Layout(graph, {
        //     settings: {gravity: 1},
        //     getEdgeWeight: 'weight'
        // })

        // layout.start()
    });
