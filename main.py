class State:
    def __init__(self, name: str, accepting: bool) -> None:
        self.name = name
        self.accepting = accepting

    def __str__(self) -> str:
        return 'State Name: ' + self.name + '\tAccepting? ' + str(self.accepting)

class Transition:
    def __init__(self, letter: str, start: State, end: State) -> None:
        self.letter = letter
        self.start = start
        self.end = end

    def __str__(self) -> str:
        return 'Transition with letter ' + self.letter + ' from ' + self.start.name + ' to ' + self.end.name

class FSM:
    def __init__(self, alphabet: [str], states: [State], start_state: State, transitions: [Transition]) -> None:
        self.alphabet = alphabet
        self.states = states
        self.start_state = start_state
        self.transitions = transitions

    def __str__(self) -> str:
        ret_str = 'FSM Data:'
        ret_str += '\n\tAlphabet: ' + ', '.join(self.alphabet)
        ret_str += '\n\tStates:'
        for state in self.states:
            ret_str += '\n\t\t' + str(state)
        ret_str += '\n\tStarting State:\n\t\t' + str(self.start_state)
        ret_str += '\n\tAccepting States:'
        for state in self.states:
            if state.accepting:
                ret_str += '\n\t\t' + str(state)
        ret_str += '\n\tTransitions:'
        for trans in self.transitions:
            ret_str += '\n\t\t' + str(trans)

        return ret_str

def find_state_by_id(states: [State], id: int) -> State:
    for state in states:
        if state.name == 'q' + str(id):
            return state
    
    return None

def main():
    fsm = FSM([], [], None, [])

    alphabet = input('Enter letters of the alphabet separated by commas: ')
    while len(alphabet) == 1 and alphabet[0] == '':
        alphabet = input('Enter letters of the alphabet separated by commas: ')
    fsm.alphabet = alphabet.strip().replace(' ', '').split(',')

    while True:
        try:
            num_states = int(input('How many states? '))
            max_state_id = num_states - 1
            break
        except ValueError:
            print('')

    start_state = None
    while True:
        try:
            start_state = int(input('Enter the ID of the start state, between 0 and ' + str(max_state_id) + ': '))
            if not (start_state < 0 or start_state > max_state_id):
                break
        except ValueError:
            print('')

    accepting_states = input('Enter the IDs of the accepting states separated by commas between 0 and ' + str(max_state_id) + ': ').strip().replace(' ', '').split(',')
    while len(accepting_states) == 1 and accepting_states[0] == '':
        accepting_states = input('Enter the IDs of the accepting states separated by commas between 0 and ' + str(max_state_id) + ': ').strip().replace(' ', '').split(',')
    
    for i in range(num_states):
        this_state = State('q' + str(i), str(i) in accepting_states)
        fsm.states.append(this_state)
    fsm.start_state = find_state_by_id(fsm.states, int(start_state))

    while True:
        print('Current Transitions:')
        for trans in fsm.transitions:
            print('\t' + str(trans))
        print('State IDs range from 0 to', max_state_id)
        trans = input('Enter a transition in this format: \'LETTER, FROM_STATE_ID, TO_STATE_ID\'. Enter nothing to stop: ').strip().replace(' ', '').split(',')
        if len(trans) == 1 and trans[0] == '' and not len(fsm.transitions) == 0:
            # TODO
            # Check every state to see if they have an edge for all letters
            # If there is one without, print error and try again
            break

        if not len(trans) == 3:
            continue

        valid_letter = trans[0] in fsm.alphabet
        valid_from = 0 <= int(trans[1]) <= max_state_id
        valid_to = 0 <= int(trans[2]) <= max_state_id
        if not valid_letter or not valid_from or not valid_to:
            continue
        # TODO: check for duplicate transitions (use sets!)

        new_trans = Transition(trans[0], find_state_by_id(fsm.states, int(trans[1])), find_state_by_id(fsm.states, int(trans[2])))
        fsm.transitions.append(new_trans)

    print(fsm)

    str_test_cases = ['', 'a', 'b', 'aa', 'bb']
    for test in str_test_cases:
        pass
    
    # TODO
    # Init array of test cases
    # For each test case
        # Start with a pointer which points to starting state of FSM
        # Find the edge corresponding to the current letter, starting from this state
        # Set pointer to the to state of this transition
        # Remove the first char of the string
        # If string == ''
            # If pointer is on an accepting state return True, else False

main()

"""

a
b
aa
bb
ab
ba
aba
bab
abb
baa
aab
bba
aaa
bbb
aaaa
bbbb
abab
aaab
abbb
abba
baba
baaa
bbba
baab
ababbbaaabba
ababbbaaabbb
abaaaabbbaaa
abaaaabbbaaa
abbbbbbbbbbb
aabbbbbbbbbb
bbaaaaaaaaaa
baaaaaaaaaaa
bbaaaaaaaaab
abbbbbbbbbba
"""