from dfa import DFA
from json import dump

class DFA_utils:

    @staticmethod
    def parallel_composition( dfa_1:DFA, dfa_2:DFA, filename_for_new_dfa:str="paralleled_dfa.json") -> None:
        states= [".".join([x,y]) for x in dfa_1.get_states() for y in dfa_2.get_states()]
        alphabet= list(set(dfa_1.get_alphabet() + dfa_2.get_alphabet()))
        initial_state= states[0]
        accepting_states= [".".join([x,y]) for x in dfa_1.get_accepting_states() for y in dfa_2.get_accepting_states()]

        transitions= []
        for state in states:
            dot_index= state.index(".")
            for symbol in alphabet:
                    key_1 = f"({state[:dot_index]}, {symbol})"
                    key_2 = f"({state[dot_index+1:]}, {symbol})"
                    
        
                    if symbol not in dfa_1.get_alphabet():
                        transition_1= state[:dot_index]
                        transition_2= dfa_2.get_transitions()[key_2]
                        transitions.append({"from":state, "with": symbol, "to": ".".join([transition_1,transition_2])})

                    elif symbol not in dfa_2.get_alphabet():
                        transition_1= dfa_1.get_transitions()[key_1]
                        transition_2= state[dot_index+1:]
                        transitions.append({"from":state, "with": symbol, "to": ".".join([transition_1,transition_2])})

                    else:
                        transition_1= dfa_1.get_transitions()[key_1]
                        transition_2= dfa_2.get_transitions()[key_2]
                        transitions.append({"from":state, "with": symbol, "to": ".".join([transition_1,transition_2])})

        result= {
            "states": states,
            "alphabet": alphabet,
            "transitions": transitions,
            "initial_state": initial_state,
            "accepting_states": accepting_states
        }
        with open(filename_for_new_dfa, "w") as file:
            dump(result, file, indent=4)

    @staticmethod
    def accessible_part(dfa:DFA, filename_for_new_dfa:str="dfa_after_ac.json") -> None:
        states=set()
        transitions= []
        
        for _ in range(0, len(dfa.get_states())-2):
            for state in dfa.get_states():
                transitions_to_temp= set(map(lambda transition: transition["to"], transitions))
                for symbol in dfa.get_alphabet():
                    key = f"({state}, {symbol})"
                    if state == dfa.get_initial_state() or state in transitions_to_temp:
                        states.add(state)
                        transitions.append({"from":state, "with": symbol, "to": dfa.get_transitions()[key]})

        accepting_states= filter(lambda state: state in states, dfa.get_accepting_states())

        result= {
            "states": list(states),
            "alphabet": dfa.get_alphabet(),
            "transitions": transitions,
            "initial_state": dfa.get_initial_state(),
            "accepting_states": list(accepting_states)
        }
        with open(filename_for_new_dfa, "w") as file:
            dump(result, file, indent=4)


    @staticmethod
    def dfa_testing(dfa:DFA) -> None:
        print(f"\nInput alphabet: {dfa.get_alphabet()}. Press 'Enter' without any input to quit.\n")
        while True:
            try:
                user_input = input("Please give me a word: ")
                if user_input=="": break
                print ( "Accepted." if dfa.is_accepted(user_input) else "Not accepted.")
            except KeyError:
                print("Your input contains symbols that aren't included in the alphabet of the DFA.")

if __name__ == "__main__":
    dfa_1= DFA("./json/dfa_1.json")
    dfa_2= DFA("./json/dfa_2.json")
    DFA_utils.parallel_composition(dfa_1, dfa_2)
    dfa_3= DFA("paralleled_dfa.json")
    DFA_utils.accessible_part(dfa_3)
    dfa_4= DFA("dfa_after_ac.json")
    DFA_utils.dfa_testing(dfa_4)