from json import load
from pathlib import Path

class DFA:
    def __init__(self, filename:str) -> None:
        file_to_search = Path(filename)

        if file_to_search.exists():
            with open(filename) as file:
                data = load(file)
                self.__init_instance(data, filename)
        else:
            self.__default_init(filename)

    #Instance initialization methods below
    def __init_instance(self, data, filename) -> None:
        self.__states = data["states"]
        self.__alphabet = data["alphabet"]
        self.__build_transition_cache(data["transitions"])
        self.__initial_state = data["initial_state"]
        self.__accepting_states = data["accepting_states"]
        print(f"DFA successfully created with the given file '{filename}'.")

    def __build_transition_cache(self, transitions) -> None:
        self.__transitions = {}
        for transition in transitions:
            self.__transitions[f'({transition["from"]}, {transition["with"]})']= transition["to"]

    def __default_init(self, filename:str):
        self.__states = []
        self.__alphabet = []
        self.__transitions = {}
        self.__initial_state = 0
        self.__accepting_states = []
        print(f"The DFA was initialized with default values because the file '{filename}' wasn't found.")

    #Getters below
    def get_states(self) -> list:
        return self.__states

    def get_transitions(self) -> dict:
        return self.__transitions

    def get_alphabet(self) -> list:
        return self.__alphabet

    def get_initial_state(self) -> str:
        return self.__initial_state

    def get_accepting_states(self) -> list:
        return self.__accepting_states

    #Other instance methods below
    def _delta(self, key:str) -> str:
        return self.get_transitions()[key]

    def _delta_star(self, user_input:str) -> int:
        state = self.get_initial_state()
        for symbol in user_input:
            state=self._delta(f"({state}, {symbol})")
        return state 
    
    def is_accepting_state(self, state:str) -> bool:
        return state in self.get_accepting_states()

    def is_accepted(self, user_input:str) -> bool:
        return self.is_accepting_state(self._delta_star(user_input))



if __name__ == "__main__":
    dfa1 = DFA("DFA_1.json")
    print(f"""
        states: {dfa1.get_states()},
        alphabet: {dfa1.get_alphabet()},
        transitions: {dfa1.get_transitions()},
        initial state: {dfa1.get_initial_state()},
        accepting states: {dfa1.get_accepting_states()}
    """)
    # dfa2 = DFA("DFA_2.json")
    # print(f"""
    #     states: {dfa2.get_states()},
    #     alphabet: {dfa2.get_alphabet()},
    #     transitions: {dfa2.get_transitions()},
    #     initial state: {dfa2.get_initial_state()},
    #     accepting states: {dfa2.get_accepting_states()}
    # """)
    # dfa3 = DFA("result.json")
    # print(f"""
    #     states: {dfa3.get_states()},
    #     alphabet: {dfa3.get_alphabet()},
    #     transitions: {dfa3.get_transitions()},
    #     initial state: {dfa3.get_initial_state()},
    #     accepting states: {dfa3.get_accepting_states()}
    # """)
    while True:
        try:
            user_input = input("Please give me a word: ")
            if user_input=="": break
            print ( "Accepted." if dfa1.is_accepted(user_input) else "Not accepted.")
        except KeyError:
            print("Your input contains symbols that aren't included in the alphabet of the DFA.")