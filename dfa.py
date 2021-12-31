from json import load

class DFA:
    """
    Deterministic Finite Automaton object
    
    Acceptable input file format:

    - JSON

    Datatypes:

    - states: list of strings
    - alphabet: list of strings
    - transitions: list of dictionaries of string key and value pairs
    - initial state: string
    - accepting states: list of strings

    Example of required JSON structure:

    {
        "states": [ "0", "1" ],\n
        "alphabet": [ "a", "b" ],\n
        "transitions": [ { "from": 0, "with": a, "to": 1}, { "from": 1, "with": b, "to": 1 } ],\n
        "initial_state": 0,\n
        "accepting_states": [ "0", "1" ]

    }
    """
    def __init__(self, filepath:str, verbose:bool=False) -> None:
        with open(filepath) as file:
            data = load(file)
            self.__init_instance(data)
            if verbose:
                print(self)


    #Instance initialization methods below
    def __init_instance(self, data) -> None:
        self.__states=  data["states"]
        self.__alphabet= data["alphabet"]
        self.__build_transition_cache(data["transitions"])
        self.__initial_state= data["initial_state"]
        self.__accepting_states= data["accepting_states"]

    def __build_transition_cache(self, transitions) -> None:
        self.__transitions = {}
        for transition in transitions:
            self.__transitions[transition["from"], transition["with"]]= transition["to"]

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
            state= self._delta((state, symbol))
        return state 
    
    def is_accepting_state(self, state:str) -> bool:
        return state in self.get_accepting_states()

    def is_accepted(self, user_input:str) -> bool:
        return self.is_accepting_state(self._delta_star(user_input))

    def number_of_states(self) -> int:
        return len(self.get_states())

    def __str__(self) -> str:
        return f"""
DFA:
    states: {self.get_states()}
    alphabet: {self.get_alphabet()}
    transitions: {self.get_transitions()}
    initial state: {self.get_initial_state()}
    accepting states: {self.get_accepting_states()}"""



if __name__ == "__main__":
    dfa1 = DFA("dfa_after_ac.json", verbose=True)
    while True:
        try:
            user_input = input("\nPress 'Enter' without any other input to quit the application.\nPlease give me a word: ")
            if user_input=="": break
            print ( "Accepted." if dfa1.is_accepted(user_input) else "Not accepted.")
        except KeyError:
            print("\nYour input contains symbols that aren't included in the alphabet of the DFA.")
