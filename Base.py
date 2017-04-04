# -*- coding: utf-8 -*-
"""
@author Parth Parikh
"""

##Simulated Annealing
import numpy as np
from numpy.random import randint
import matplotlib.pyplot as plt


class Node:
    def __init__(self, pos=(0, 0), id=0):
        self.pos = pos
        self.id = id
        self.netIds = list()

    def get_degree(self):
        return len(self.netIds)

    def get_x(self):
        return self.pos[0]

    def get_y(self):
        return self.pos[1]

    def get_distance(self, node):
        return abs(self.pos[0] - node.pos[0]) + abs(self.pos[1] - node.pos[1])

    def __str__(self):
        return str(str(self.id) + ':(' + str(self.pos[0]) + ',' + str(self.pos[1]) + ')')

    def __int__(self):
        return self.id

    def __eq__(self, i):
        return int(self) == i


class Net:
    def __init__(self, id=0):
        self.id = id
        self.nodeList = list()

    def add_node(self, node):
        self.nodeList.append(node)
        node.netIds.append(self.id)

    def add_nodes_from(self, node_list):
        for node in node_list:
            self.nodeList.append(node)

    def remove_node(self, node_id):
        self.nodeList.remove(node_id)

    def has(self, node_id):
        return node_id in self.nodeList

    def get_cost(self):
        max_x = 0
        max_y = 0
        for node in self.nodeList:
            x = node.pos[0]
            y = node.pos[0]
            if x > max_x:
                max_x = x
            if y > max_y:
                max_y = y
        return max_x + max_y

    def __len__(self):
        return len(self.nodeList)

    def __str__(self):
        string = str(self.id) + ':\n'
        for node in self.nodeList:
            string = string + '\t' + str(node) + '\n'
        return string


class Board:
    def __init__(self, id=0, nets=[], nodes=[], width=0, height=0):
        self.width = width
        self.height = height
        self.nets = nets
        self.id = id
        self.nodes = nodes

    def add_net(self, net):
        self.nets.append(net)

    def add_node(self, node):
        self.nodes.append(node)

    def get_cost(self):
        cost = 0
        for net in self.nets:
            cost = cost + net.get_cost()
        return cost

    def is_empty(self, pos):
        for node in self.nodes:
            if pos == node.pos:
                return False
        return True

    def __str__(self):
        string = str(self.id) + ":\n"
        for net in self.nets:
            string = string + str(net)
        return string


def is_pos_empty(pos, nodeList):
    for node in nodeList:
        if pos == node.pos:
            return False
    return True


def get_total_cost(nets):
    cost = 0
    for net in nets:
        cost += net.get_cost()
    return cost


def random_place_board(nodeList, width, height, debug=False):
    for node in nodeList:
        n_x = 0
        n_y = 0
        while not is_pos_empty((n_x, n_y), nodeList):
            n_x = randint(width)
            n_y = randint(height)
        if debug:
            print("NODE:%d at (%d,%d)" % (node.id, n_x, n_y))
        node.pos = (n_x, n_y)


def swap(n1: Node, n2: Node) -> None:
    pos = n1.pos
    n1.pos = n2.pos
    n2.pos = pos


def draw_board(nodeList):
    """

    :type nodeList: list
    """
    x = []
    y = []
    area = []
    for node in nodeList:
        x.append(node.pos[0])
        y.append(node.pos[1])
        area.append(np.pi * node.get_degree())

    plt.scatter(x, y, s=area)
    plt.show()

def find_node_at(pos,nodeList):
    for node in nodeList:
        if node.pos == pos:
            return node
    return False

