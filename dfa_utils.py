from dfa import DFA
from json import dump

class DFA_util:

    @staticmethod
    def parallel_composition( dfa_1:DFA, dfa_2:DFA, filename_for_new_DFA:str="result.json") -> None:
        states= [x+y for x in dfa_1.get_states() for y in dfa_2.get_states()]
        alphabet= list(set(dfa_1.get_alphabet() + dfa_2.get_alphabet()))
        transitions= DFA_util.__transitions_mapper(states, alphabet)
        initial_state= states[0]
        accepting_states= [x+y for x in dfa_1.get_accepting_states() for y in dfa_2.get_accepting_states()]

        result = {
            "states": states,
            "alphabet": alphabet,
            "transitions": transitions,
            "initial_state": initial_state,
            "accepting_states": accepting_states
        }
        with open(filename_for_new_DFA, "w") as file:
            dump(result, file, indent=4)

    @staticmethod
    def __transitions_mapper(states:list, alphabet:list) -> list:
        transitions = []

        for state in states:
            for symbol in alphabet:
                if True:
                    transitions.append({"from":str(state), "with": symbol, "to":1})
        return transitions

    @staticmethod
    def accessible_part(target:str) -> None:
        pass

if __name__ == "__main__":
    DFA_1 = DFA("DFA_1.json")
    DFA_2 = DFA("DFA_2.json")
    DFA_util.parallel_composition(DFA_1, DFA_2)