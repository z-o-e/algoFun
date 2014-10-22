# two generative models for graphs
#
# 1. AGM (aka. affiliation graph model)
# given parameters: V (vertex), C (communities), M (memberships), {p_c} (each community c has a single probability p_c)
# the overall edge probability:
# p(u,v) = 1 - II(1-p_c) where c is the set of community that u, v both belongs to
# p(u,v) = epsilon if u and v share no communities
# problems: not able to address overlapping communities, i.e. nodes belong to multiple communities
#
# 2. BigCLAM (aka Cluster Affiliation Model for Big Networks)
# construct Factor matrix F
# where F_ij represents the strength of node i belongs to community j
# commuity A links node u,v independently with P_A(u,v) = 1-exp(-F_uA*F_vA)
# the prob. at least one common C links them P(u,v) = 1- II(1-P_c(u,v)) = 1 - exp(-F_u*F_v'), for all c in C
# Given a network G(V,E), estimate F, find F that maximizes the likelihood:
# argmax_F (II(p(u,v))*II(1-p(u,v))), where p(u,v) = 1- exp(-F_u*F_v') for all (u,v) in E# or convert to log likelihood l(F) = sum_uv(log(1-exp(-F_u*F_v'))) - sum_non_uv(F_u*F_v'), the first log sum for all (u,v) belongs to E, the second sum for (u,v)'s don't belong to E
# gradient of a single row of F_u of F:
# delta_l(F_u) = sum_uv(F_v*(exp(-F_u*F_v')/(1-exp(-F_u*F_v'))))- sum_non_v(F_v)
# the faster version cache sum_v(F_v) so that replace sum_non_v = sum_v(F_v) - F_u - sum_v(F_v)



# @param nodeID: an int representing the vertex id
# @param memberships: a list of float(<=1) representing the probabilities that the node belongs to community_i 
class node:
    def __init__(self,nodeID, memberships):
        self.nodeId = nodeId
        self.memberships = memberships

# @param communityID: an int representing the community id
# @param nodes: a list of member nodes
class community:
    def __init__(self, communityID, nodes):
    self.communityID = communityID
    self.nodes = nodes

# @param commuties: a list of community in the graph
class graphAGM:
    def __init__(self, communities):
        self.communities = communities
    
    # @param a, b: two nodes in the graph
    # @return: a float of probability that a and b are linked
    def getEdgeProb(self, a, b):
        epsilon = 10**-6
        res = 1
        for c in self.commuities:
            if a in c.nodes and b in c.nodes:
                i = c.communityID
                res *= (1-a.memberships[i]*b.memberships[i])
        res = 1-res
        if res==0:
            return epsilon
        return res 

# @param commuties: a list of community in the graph
class graphBigCLAM:
    def __init__(self, communities):
        self.communities = communities
        countN = 0
        d = collections.defaultdict(bool)
        for c in self.communities:
            countN += len(self.communities.nodes)
            for node in c.nodes:
                d[node.id] = node

        self.F = np.zeros((len(self.communities.nodes, countN)))
        for c in self.communities:
            i = c.communityID
            for node in c.nodes:
                j = node.nodeId
                self.F[i][j] = node.memberships[i]
 
    # to do
    # def estimateF
    

