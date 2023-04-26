import Sigma from "sigma";
import Graph from "graphology";
import louvain from 'graphology-communities-louvain';
import NoverlapLayout from 'graphology-layout-noverlap/worker';
import chroma from "chroma-js"

fetch('/reddit_sigma.json')
  .then(response => response.json())
  .then(data => {
    const container = document.getElementById("container");

    const graph = new Graph();

    const maxSize = data.nodes.map((node) => node.size).reduce((prev, cur) => prev < cur ? cur : prev)

    data.nodes.forEach(node => graph.addNode(node.id, { label: node.label, size: Math.max(5, (node.size / maxSize) * 30) }))
    data.edges.forEach(edge => graph.addEdge(edge.source, edge.target))

    const graphModularity = louvain.detailed(graph)
    louvain.assign(graph)

    const colors = chroma.scale('OrRd').colors(graphModularity.count)

    graph.nodes().forEach((node, i) => {
      const angle = (i * 2 * Math.PI) / graph.order;
      //const community = graph.getAttribute(node, "community")
      //graph.setNodeAttribute(node, "color", colors[community])
      graph.setNodeAttribute(node, "x", graphModularity.communities[node] + 100 * Math.cos(angle));
      graph.setNodeAttribute(node, "y", 100 * Math.sin(angle));
    });

    const renderer = new Sigma(graph, container);
    // const layout = new NoverlapLayout(graph);

    // layout.start()

  });
