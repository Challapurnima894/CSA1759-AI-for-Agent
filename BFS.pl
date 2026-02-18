edge(a,b,1).
edge(a,c,3).
edge(b,d,1).
edge(c,d,1).
best_first(start,goal):-
    edge(start,goal,-),
    write(start,write('->'),write(goal).
