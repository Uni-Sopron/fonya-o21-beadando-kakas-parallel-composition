from dfa import DFA
from json import dump
from copy import deepcopy

class DFA_utils:

    @staticmethod
    def parallel_composition( dfa_1:DFA, dfa_2:DFA, filename_for_new_dfa:str="paralleled_dfa.json") -> None:
        states= [(x,y) for x in dfa_1.get_states() for y in dfa_2.get_states()]
        alphabet= list(set(dfa_1.get_alphabet() + dfa_2.get_alphabet()))
        initial_state= states[0]
        accepting_states= [(x,y) for x in dfa_1.get_accepting_states() for y in dfa_2.get_accepting_states()]

        transitions= []
        for s1, s2 in states:
            for symbol in alphabet:
                    key_1 = (s1, symbol)
                    key_2 = (s2, symbol)
                           
                    if symbol not in dfa_1.get_alphabet():
                        state_2= dfa_2.get_transitions()[key_2]
                        transitions.append({"from": s1+s2, "with": symbol, "to": s1+state_2})

                    elif symbol not in dfa_2.get_alphabet():
                        state_1= dfa_1.get_transitions()[key_1]
                        transitions.append({"from": s1+s2, "with": symbol, "to": state_1+s2})

                    else:
                        state_1= dfa_1.get_transitions()[key_1]
                        state_2= dfa_2.get_transitions()[key_2]
                        transitions.append({"from": s1+s2, "with": symbol, "to": state_1+state_2})


        result= {
            "states": [x+y for x,y in states],
            "alphabet": alphabet,
            "transitions": transitions,
            "initial_state": initial_state[0] + initial_state[1],
            "accepting_states": [x+y for x,y in accepting_states]
        }
        with open(filename_for_new_dfa, "w") as file:
            dump(result, file, indent=4)

    @staticmethod
    def accessible_part(dfa:DFA, filename_for_new_dfa:str="dfa_after_ac.json") -> None:
        transitions= []

        #Append the first transitions
        for symbol in dfa.get_alphabet():
            key= (dfa.get_initial_state(), symbol)
            transition= {"from": dfa.get_initial_state(), "with": symbol, "to": dfa.get_transitions()[key]}
            transitions.append(transition)
            print(transitions)

        # for state in dfa.get_states():
        #     for symbol in dfa.get_alphabet():
        #         key= (tuple(state), symbol)
        #         transition= {"from": state, "with": symbol, "to": dfa.get_transitions()[key]}
        #         if transition not in transitions:

        # for _ in range(0, len(dfa.get_states())-2):
        #     for state in dfa.get_states():
        #         transitions_to_temp= list(map(lambda transition: transition["to"], transitions))
        #         for symbol in dfa.get_alphabet():
        #             key= (state, symbol)
        #             transition= {"from": state, "with": symbol, "to": dfa.get_transitions()[key]}
        #             if (state in transitions_to_temp or state == dfa.get_initial_state()):
        #                 if state not in states:
        #                     states.append(state)
        #                 if transition not in transitions:
        #                     transitions.append(transition)
        reachable_states= list(set(map(lambda transition: tuple(transition["to"]), transitions)))
        states= [dfa.get_initial_state(), *reachable_states]
        accepting_states= list(filter(lambda state: state in states, dfa.get_accepting_states()))

        result= {
            "states": states,
            "alphabet": dfa.get_alphabet(),
            "transitions": transitions,
            "initial_state": dfa.get_initial_state(),
            "accepting_states": accepting_states
        }
        with open(filename_for_new_dfa, "w") as file:
            dump(result, file, indent=4)

        

if __name__ == "__main__":
    # "./json/dfa_1.json"
    # "./json/dfa_2.json"
    dfa_1= DFA("./json/dfa_1.json")
    dfa_2= DFA("./json/dfa_2.json")
    DFA_utils.parallel_composition(dfa_1, dfa_2)
    dfa_3= DFA("paralleled_dfa.json", verbose=True)
    # DFA_utils.accessible_part(dfa_3)
    # dfa_4= DFA("dfa_after_ac.json")