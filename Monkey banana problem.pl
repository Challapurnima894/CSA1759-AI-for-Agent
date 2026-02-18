% Legal moves
move(state(middle, onbox, middle, hasnot),
      grasp,                                   % Grasp banana
      state(middle, onbox, middle,has)).
move(state(P, onfloor,P,H),
     climb,                                       % Climb box
     state(P, onbox, P, H)).
move(state(P1,onfloor.P1,H),
     push(P1,P2),                            %Push box from P1 to P2
     state(P2, onfloor, P2,H)).
move(state(P1, onfloor,
