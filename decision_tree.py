from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier,_tree

def print_tree(tree,features,targets,node=0,depth=0):
    t=tree.tree_
    ind=" "*depth
    if t.feature[node]!=_tree.TREE_UNDEFINED:
        print(f"{ind}if {features[t.feature[node]]}<={t.threshold[node]:2f}:")
        print_tree(tree,features,targets,t.children_left[node],depth+1)
        print(f"{ind} else:")
        print_tree(tree,features,targets,t.children_right[node],depth+1)

    else:
        print(f"{ind} return: {targets[t.value[node].argmax()]}")

iris=load_iris()
clf=DecisionTreeClassifier(max_depth=3,random_state=0).fit(iris.data,iris.target)

print("\nDecision tree rule:\n")
print_tree(clf,iris.feature_names,iris.target_names)
