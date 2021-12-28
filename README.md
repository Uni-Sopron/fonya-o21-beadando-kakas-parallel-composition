# Formal languages and automatons assignment documentation

## Author

- Name: Adam Kakas
- Neptun-code: U524QJ

## Assignment description

The goal of the project is to create a solution considering the following ascpects:

- The application can read data from files of a directory,
- build DFAs from it,
- create their parallel composition,
- write it into a separate file,
- only select the reachable states and transitions of the selected DFA,
- write it into a separate file again.

## Application usability

The application uses predefined DFA structures in the format of JSONs. If the same structure-logic is applied to build different DFAs the application can use them as well.
In addition the util functions provide help in oprating on DFAs.

The application consists of:

- dfa.py (DFA OOP solution)
- dfa_utils.py (Functions for DFAs, all of them are static methods of this class)

### dfa.py

The class is capable of:

- holding a predefined JSON in a DFA-like object,
- determining whether the user's input is acceptable or not by the DFA

To run / test it open terminal and type the following:

```ps
python dfa.py
```

### dfa_utils.py

The class is capable of:

- creating the parallel composition of two DFAs (static function of the class),
- reducing the DFAs size by removing the unreachable states (static function of the class)

To run / test it open terminal and type the following:

```ps
python dfa_utils.py
```

## Json files description

- dfa_1.json: #a + #b >= 2, Σ = {a, b}
- dfa_2.json: #a <= 3, Σ = {a, b}
- dfa_3.json: #a % 2 == 0, Σ = {a, b}
- dfa_4.json: #b >= 2, Σ = {c, b}
- dfa_5.json: |w| ends with 'a', Σ = {a, b}
- dfa_6.json: re: (a U b U c)\*ab(a U b)\*, Σ = {a, b, c}
- dfa_7.json: re: (abc)\*ab, Σ = {a, b, c}
- dfa_8.json: #a + 2 × #b + 3 × #c ≡ 1;3, Σ = {a, b, c, d}
- paralleled_dfa.json: default file as the result of the parallel composition of two separate dfas
- dfa_after_ac.json: default file as the result of the dfa on which Acc was used on
