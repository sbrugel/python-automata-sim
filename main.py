import copy, os, sys

STR_TEST_CASES = [
    "", # empty string
    "a", # single chars
    "b",
    "aa", # pairs of chars
    "bb",
    "ab",
    "ba",
    "aba", # trios of chars
    "bab",
    "abb",
    "baa",
    "aab",
    "bba",
    "aaa",
    "bbb",
    "aaaa", # 4 chars
    "bbbb",
    "abab",
    "aaab",
    "abbb",
    "abba",
    "baba",
    "baaa",
    "bbba",
    "baab",
    "aabb",
    "bbaa",
    "ababbbaaabba", # long strings of even len
    "ababbbaaabbb",
    "abaaaabbbaaa",
    "abaaaabbbaab",
    "abbbbbbbbbbb",
    "aabbbbbbbbbb",
    "bbaaaaaaaaaa",
    "baaaaaaaaaaa",
    "bbaaaaaaaaab",
    "abbbbbbbbbba",
    "ababbbaaaba", # long strings of odd len
    "ababbbaaabb",
    "abaaaabbbaa",
    "abaaaabbbab",
    "abbbbbbbbbb",
    "aabbbbbbbbb",
    "bbaaaaaaaaa",
    "baaaaaaaaaa",
    "bbaaaaaaaab",
    "abbbbbbbbba",
    "aababb", # other random stuff
    "bbabaa"
]

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

    """
    This returns True if every state in the FSM has a transition from it for every letter in the alphabet provided.
    """
    def states_have_all_transitions(self) -> bool:
        for state in self.states:
            trans_from_state = [trans for trans in self.transitions if trans.start == state]
            if len(trans_from_state) < len(self.alphabet):
                return False
        return True
            
    """
    This returns the transition with the given letter and start state. If it doesn't exist, it returns None.
    """
    def find_transition(self, letter: str, start: State) -> Transition:
        transitions = []
        for trans in self.transitions:
            if trans.letter == letter and trans.start == start:
                transitions.append(trans)
            
        if len(transitions) == 0: return None
        else: return transitions

    def __str__(self) -> str:
        ret_str = 'FSM Data:'
        ret_str += '\n\tAlphabet: ' + ', '.join(self.alphabet)
        ret_str += '\n\tStates:'
        for state in self.states:
            ret_str += '\n\t\t' + str(state)
        ret_str += '\n\tStarting State:\n\t\t' + str(self.start_state)
        ret_str += '\n\tTransitions:'
        for trans in self.transitions:
            ret_str += '\n\t\t' + str(trans)
        return ret_str
    
"""
Clears the terminal.
"""
def os_agnostic_clear():
    if sys.platform == 'win32':
        os.system('cls')
    else:
        os.system('clear')

"""
Gets the state with the given ID (starts from 0).
"""
def find_state_by_id(states: [State], id: int) -> State:
    for state in states:
        if state.name == 'q' + str(id):
            return state
    
    return None

"""
Traverses the machine from this state with the given string, start state, and path so far.
    fsm: The FSM
    testing_str: The string remaining
    start_state: The state this simulation starts at
    current_path: The states travelled to so far
Returns true if it ends in accept state, false if not, as well as the final path traversed.
"""
def start_simulation(fsm: FSM, testing_str: str, start_state: State, current_path: list) -> bool:
    state_pointer = start_state # where are we at in the FSM?
    path = copy.deepcopy(current_path) # list of tuples showing where the simulation went
    while not testing_string == '':
        current_char = testing_string[0]
        valid_transitions = fsm.find_transition(current_char, state_pointer)
        if len(valid_transitions) == 1:
            path.append((current_char, state_pointer.name, valid_transitions[0].end.name))
            state_pointer = valid_transitions[0].end # move to the next state
            testing_string = testing_string[1:] # remove first char
        elif len(valid_transitions) == 0:
            return (False, path)
        else:
            pass

    return (False, [])

def main():
    os_agnostic_clear()
    fsm = FSM(['a', 'b'], [], None, [])

    # alphabet = input('Enter letters of the alphabet separated by commas: ').strip().replace(' ', '').split(',')
    # invalid_alphabet = any(len(alpha) > 1 for alpha in alphabet) # letters cannot be more than one char long
    # while (len(alphabet) == 1 and alphabet[0] == '') or invalid_alphabet:
    #     alphabet = input('Enter letters of the alphabet separated by commas: ').strip().replace(' ', '').split(',')
    #     invalid_alphabet = any(len(alpha) > 1 for alpha in alphabet)
    # fsm.alphabet = alphabet

    os_agnostic_clear()
    while True: # keep reading inputs until we get a num >= 2
        try:
            num_states = int(input('How many states? (at least 2) '))
            max_state_id = num_states - 1
            if num_states >= 2:
                break
        except ValueError:
            print('')

    os_agnostic_clear()
    start_state = None
    while True: # keep reading inputs until we get a num between 0 and max state id
        try:
            start_state = int(input('Enter the ID of the start state, between 0 and ' + str(max_state_id) + ': '))
            if not (start_state < 0 or start_state > max_state_id):
                break
        except ValueError:
            print('')

    os_agnostic_clear()

    while True: # keep reading inputs until we get a valid input (comma separated of existing state IDs)
        accepting_states = input('Enter the IDs of the accepting states separated by commas between 0 and ' + str(max_state_id) + ': ').strip().replace(' ', '').split(',')
        try:
            any_invalid_states = any((int(id_given) > max_state_id or int(id_given) < 0) for id_given in accepting_states)
            if any_invalid_states or (len(accepting_states) == 1 and accepting_states[0] == ''):
                continue
        except ValueError:
            continue
        break
    
    for i in range(num_states): # create all the states
        this_state = State('q' + str(i), str(i) in accepting_states)
        fsm.states.append(this_state)
    fsm.start_state = find_state_by_id(fsm.states, int(start_state))

    os_agnostic_clear()

    while True:
        print('Current Transitions:')
        for trans in fsm.transitions:
            print('\t' + str(trans))
        print('State IDs range from 0 to', max_state_id)
        trans = input('Enter a transition in this format: \'LETTER (or \'EP\' for epsilon), FROM_STATE_ID, TO_STATE_ID\'. Enter nothing to stop: ').strip().replace(' ', '').split(',')

        if len(trans) == 1 and trans[0] == '' and not len(fsm.transitions) == 0: # submitting
            # if not fsm.states_have_all_transitions(): # only reached when trying to submit
            #     os_agnostic_clear()
            #     print('ERROR: Not all states have transitions for every letter! Clearing transitions...')
            #     fsm.transitions = []
            #     continue

            # clear duplicate transitions
            fsm.transitions = list(set(fsm.transitions))
            break

        if not len(trans) == 3: # incomplete transition
            os_agnostic_clear()
            print('ERROR: Submit 3 items for each transition')
            continue

        valid_letter = trans[0] in fsm.alphabet or trans[0] == 'EP'
        valid_from = 0 <= int(trans[1]) <= max_state_id
        valid_to = 0 <= int(trans[2]) <= max_state_id
        if not valid_letter or not valid_from or not valid_to:
            os_agnostic_clear()
            print('ERROR: One of your inputs was invalid (i.e. letter not in alphabet, invalid state ID)')
            continue

        # if fsm.find_transition(trans[0], find_state_by_id(fsm.states, int(trans[1]))):
        #     os_agnostic_clear()
        #     print('ERROR: A transition for this start state with this letter already exists and was not added')
        #     continue

        new_trans = Transition(trans[0], find_state_by_id(fsm.states, int(trans[1])), find_state_by_id(fsm.states, int(trans[2])))
        fsm.transitions.append(new_trans)
        os_agnostic_clear()

    os_agnostic_clear()
    print(fsm)

    for testing_string in STR_TEST_CASES:
        if start_simulation(fsm, testing_string, fsm.start_state, [])[0]:
            print('\033[92mThe string', (orig_str if not orig_str == '' else 'EMPTY STRING'), 'is in the language\033[0m')
        else:
            print('\033[91mThe string', (orig_str if not orig_str == '' else 'EMPTY STRING'), 'is NOT in the language\033[0m')

        orig_str = testing_string # for printing purposes

        if state_pointer.accepting:
            print('\033[92mThe string', (orig_str if not orig_str == '' else 'EMPTY STRING'), 'is in the language\033[0m')
        else:
            print('\033[91mThe string', (orig_str if not orig_str == '' else 'EMPTY STRING'), 'is NOT in the language\033[0m')
        tuple_to_str = ", ".join([f"({str(item[0])} {str(item[1])}-{str(item[2])})" for item in path])
        print('\t' + tuple_to_str)

main()
