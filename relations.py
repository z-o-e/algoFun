'''
>>> relations = [
    Relation("animal", "mammal"),
    Relation("animal", "bird"),
    Relation("lifeform", "animal"),
    Relation("cat", "lion"),
    Relation("mammal", "cat"),
    Relation("animal", "fish")]
>>> parents_list, origin = findOrigin(relations)
>>> dfsprint(parents_list,origin, space)
lifeform
  animal
    mammal
      cat
        lion
    bird
    fish

'''
class Relation(object):
  def __init__(self, parent, child):
    self.parent = parent
    self.child = child

relations = [
    Relation("animal", "mammal"),
    Relation("animal", "bird"),
    Relation("lifeform", "animal"),
    Relation("cat", "lion"),
    Relation("mammal", "cat"),
    Relation("animal", "fish")]

def findOrigin(relations):
    parents_dict, children = {}, [] 
    for r in relations:
        if r.child not in children:
            children.append(r.child)
        if r.parent not in parents_dict:
            parents_dict[r.parent] = [r]
        else:
            parents_dict[r.parent].append(r)
                
    for i in range(len(relations)):
        if relations[i].parent not in children:
            origin = relations[i].parent

    return parents_dict, origin 

def dfsprint(parents_dict, name, space):
    #print pp, pp.parent
    print ' '*space+name
    if name not in parents_dict:
        return
    
    for c in parents_dict[name]:
        dfsprint(parents_dict, c.child, space+1)
        