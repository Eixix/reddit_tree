import Sigma from "sigma";
import Graph from "graphology";
import FA2Layout from 'graphology-layout-forceatlas2/worker';


fetch('/reddit_sigma.json')
    .then(response => response.json())
    .then(data => {
        const container = document.getElementById("container");

        const graph = new Graph();

        data.nodes.forEach(node => graph.addNode(node.id, {label: node.label}))
        data.edges.forEach(edge => graph.addEdge(edge.source, edge.target))


        graph.nodes().forEach((node, i) => {
            const angle = (i * 2 * Math.PI) / graph.order;
            graph.setNodeAttribute(node, "x", 100 * Math.cos(angle));
            graph.setNodeAttribute(node, "y", 100 * Math.sin(angle));
        });

        const renderer = new Sigma(graph, container);


        const layout = new FA2Layout(graph, {
            iterations: 50,
            settings: {
                adjustSizes: true,
                gravity: 100,
                barnesHutOptimize: true
            },
        })

        layout.start()

        setTimeout(() => layout.kill(), 100000)

    });
