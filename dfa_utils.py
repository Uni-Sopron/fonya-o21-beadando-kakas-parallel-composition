from dfa import DFA
from json import dump

class DFA_util:

    @staticmethod
    def parallel_composition( dfa_1:DFA, dfa_2:DFA, filename_for_new_dfa:str="result.json") -> None:
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

        result = {
            "states": states,
            "alphabet": alphabet,
            "transitions": transitions,
            "initial_state": initial_state,
            "accepting_states": accepting_states
        }
        with open(filename_for_new_dfa, "w") as file:
            dump(result, file, indent=4)

    @staticmethod
    def accessible_part(dfa:DFA, filename_for_new_dfa:str="result.json") -> None:
        pass

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
    dfa_1 = DFA("dfa_1.json")
    dfa_2 = DFA("dfa_2.json")
    DFA_util.parallel_composition(dfa_1, dfa_2)
    dfa_3 = DFA("result.json")
    DFA_util.dfa_testing(dfa_3)