# Finite State Machine Simulator

This is a CLI simulation of a finite state machine made in Python. Made to scratch an itch to program in Python, and preparation for a side project in React I will be developing with a friend of mine, I intended this to be a FSM validator for homework assignments for CISC303, Automata Theory.

Currently this only supports the alphabet (a, b) for the automated test cases. I have code which reads input for the FSM's alphabet as comma-separated input commented out, but if it's not just those two letters you will need to write your own test cases.

This was inspired by Dr. Silber's fantastic [finite state machine simulation](https://www.eecis.udel.edu/~silber/automata). I took the idea of that application and added in a few extra things, including:
- Automatic testing based on a number of test cases (supporting only the alphabet {a, b} for now)
- Checks if every state has transitions for all letters *(this may be removed)* and checks for duplicate transitions
- Faster running per test case (you don't have to click next for each letter, it just runs the whole thing right away)

The features here are subject to change depending on what we learn in CISC303

## How to use
I would recommend using Dr. Silber's automata simulation to construct the machine beforehand, you can put the inputs as specified below in a text file then paste it into your terminal. (His simulation contains a table with all edges in the FSM)

1. Input the number of states (must be >= 2). If you create 2 states, it will create states q0 (with ID 0) and q1 (with ID 1)
2. Input the ID of the starting state (zero indexed)
3. Input the ID(s) of accepting states (zero indexed)
4. Add in transitions in this format: LETTER, FROM_STATE_ID, TO_STATE_ID. Keep entering them until you are satisfied, then hit Return with an empty input
5. Sample output for a simple FSM is included in this repository. This returns if each string test case is in the language, and how the simulation determined that. *(a q0-q1) means the test took the transition for letter 'a' between q0 and q1.*