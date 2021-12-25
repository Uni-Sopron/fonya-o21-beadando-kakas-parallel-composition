from dfa import DFA
from json import dump

class DFA_util:

    @staticmethod
    def parallel_composition( dfa_1:DFA, dfa_2:DFA, filename_for_new_dfa:str="result.json") -> None:
        states= [x+y for x in dfa_1.get_states() for y in dfa_2.get_states()]
        alphabet= list(set(dfa_1.get_alphabet() + dfa_2.get_alphabet()))
        initial_state= states[0]
        accepting_states= [x+y for x in dfa_1.get_accepting_states() for y in dfa_2.get_accepting_states()]

        transitions= []
        for state in states:
            for symbol in alphabet:
                    transition_1 = dfa_1.get_transitions()[f"({state[:1]}, {symbol})"]
                    transition_2 = dfa_2.get_transitions()[f"({state[1:]}, {symbol})"]
                    transitions.append({"from":state, "with": symbol, "to": "".join([transition_1,transition_2])})

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
    def accessible_part(target:str) -> None:
        pass

if __name__ == "__main__":
    DFA_1 = DFA("dfa_1.json")
    DFA_2 = DFA("dfa_2.json")
    DFA_util.parallel_composition(DFA_1, DFA_2)