# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 16:01:10 2017

@author: Israël & Renan
"""
from parsers.parsing import Parser
class Dijkstra:
    def __init__(self,graph):
        self.G=graph
        self.o={}
        self.dist={}
        self.Q=[]
        
    def init_conj(self):
        for v in self.G.keys():
            self.dist[v]=1000
            self.o[v]=''
    
    def extrair_min(self):
        v=''
        mini=1000
        for q in self.Q:
            if self.dist[q]<mini:
                mini=self.dist[q]
                v=q
        self.Q.remove(v)
        return v
    
    def sp(self):
        inicial='a'
        splist=[]
        self.init_conj()
        self.Q=[x for x in self.G.keys()]
        self.dist[inicial]=0
        while self.Q != []:
            u=self.extrair_min()
            for v in self.G[u]:
                p=self.G[u][v]
                if self.dist[v]>self.dist[u]+p:
                    self.dist[v]=self.dist[u]+p
                    self.o[v]=u
                    self.Q.append(v)
                    splist.append(v)
        return [inicial]+splist

filename = input("Nome do arquivo do grafo desejado:")
p=Parser("../../"+filename)
G=p.get_list()
d=Dijkstra(G)
print("Caminho mais curto: ",[x for x in d.sp()])