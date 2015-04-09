#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Last modified: Yang Kai (kai.yang@bugua.com)

"""
a tiny flow chart maker
"""
revision = '0.1'
import pydot


def flow_chart_maker(nodes_text, edges):
    graph = pydot.Dot(graph_type='digraph')

    nodes = {}
    for item in nodes_text:
        if isinstance(item, list):
            parameters = {}
            for para in item[1:]:
                if para in ['box', 'parallelogram', 'diamond']:
                    parameters['shape'] = para
                elif para in ['rounded']:
                    parameters['style'] = para
            nodes[item[0]] = pydot.Node(item[0], **parameters)
            graph.add_node(nodes[item[0]])
        else:
            nodes[item] = pydot.Node(item, shape="parallelogram")
            graph.add_node(nodes[item])

    for item in edges:
        if len(item) > 2:
            graph.add_edge(pydot.Edge(nodes[item[0]], nodes[item[1]], label=item[2]))
        else:
            graph.add_edge(pydot.Edge(nodes[item[0]], nodes[item[1]]))

    graph.write_png('example_graph.png')


if __name__ == "__main__":
    nodes_text = [
        ['Start', 'box', 'rounded'],
        'input',
        ['if valid?', 'diamond'],
        'good',
        'retry',
        ['End', 'box', 'rounded'],
    ]
    edges = [
        ('Start', 'input'),
        ('input', 'if valid?'),
        ('if valid?', 'good', 'yes'),
        ('if valid?', 'retry', 'no'),
        ('retry', 'input'),
        ('good', 'End'),
    ]
    flow_chart_maker(nodes_text, edges)