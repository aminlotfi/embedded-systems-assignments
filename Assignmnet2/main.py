fsm = {
    'state1': {'input1': 'state2', 'input2': 'state3'},
    'state2': {'input1': 'state1', 'input2': 'state3'},
    'state3': {'input1': 'state1', 'input2': 'state2'},
}

start_state = 'state1'

inputs = ['input1', 'input2', 'input1', 'input2']

def generate_cpp_code(fsm, start_state):
    states = sorted(fsm.keys())
    input_symbols = sorted({inp for transitions in fsm.values() for inp in transitions.keys()})

    state_enum = {state: idx for idx, state in enumerate(states)}
    input_enum = {inp: idx for idx, inp in enumerate(input_symbols)}

    cpp_code = "#include <iostream>\n#include <string>\nusing namespace std;\n\n"

    # Define enums for states and inputs, including INVALID states/inputs
    cpp_code += "enum State {\n"
    for state in states:
        cpp_code += f"    {state.upper()},\n"
    cpp_code += "    INVALID_STATE\n"
    cpp_code += "};\n\n"

    cpp_code += "enum Input {\n"
    for inp in input_symbols:
        cpp_code += f"    {inp.upper()},\n"
    cpp_code += "    INVALID_INPUT\n"
    cpp_code += "};\n\n"

    # Define transition table with INVALID_STATE for undefined transitions
    cpp_code += f"State transition_table[{len(states)}][{len(input_symbols)}] = {{\n"
    for state in states:
        cpp_code += "    {"
        transitions = fsm[state]
        row = []
        for inp in input_symbols:
            next_state = transitions.get(inp, "INVALID_STATE")
            if next_state == "INVALID_STATE":
                row.append("INVALID_STATE")
            else:
                row.append(next_state.upper())
        cpp_code += ", ".join(row) + "},\n"
    cpp_code += "};\n\n"

    # Function to convert string to Input enum
    cpp_code += "Input get_input(const string& input_str) {\n"
    cpp_code += "    if(false) {}\n"
    for inp in input_symbols:
        cpp_code += f'    else if(input_str == "{inp}") return {inp.upper()};\n'
    cpp_code += "    else return INVALID_INPUT;\n"
    cpp_code += "}\n\n"

    # Function to convert Input enum to string (optional, for debugging)
    cpp_code += "string input_to_string(Input input) {\n"
    cpp_code += "    switch(input) {\n"
    for inp in input_symbols:
        cpp_code += f'        case {inp.upper()}: return "{inp}";\n'
    cpp_code += "        default: return \"INVALID_INPUT\";\n"
    cpp_code += "    }\n"
    cpp_code += "}\n\n"

    # Function to convert State enum to string (optional, for debugging)
    cpp_code += "string state_to_string(State state) {\n"
    cpp_code += "    switch(state) {\n"
    for state in states:
        cpp_code += f'        case {state.upper()}: return "{state}";\n'
    cpp_code += "        default: return \"INVALID_STATE\";\n"
    cpp_code += "    }\n"
    cpp_code += "}\n\n"

    # Main function
    cpp_code += "int main() {\n"
    cpp_code += f"    State current_state = {start_state.upper()};\n"
    cpp_code += "    string input_str;\n\n"

    cpp_code += "    while (true) {\n"
    cpp_code += "        switch(current_state) {\n"
    for state in states:
        cpp_code += f"            case {state.upper()}:\n"
        cpp_code += f'                cout << "Current state: {state}" << endl;\n'
        cpp_code += "                break;\n"
    cpp_code += "            default:\n"
    cpp_code += '                cout << "Unknown state!" << endl;\n'
    cpp_code += "                return 1;\n"
    cpp_code += "        }\n\n"

    cpp_code += '        cout << "Enter input (or type \'exit\' to quit): "; \n'
    cpp_code += '        cin >> input_str;\n\n'

    cpp_code += '        if(input_str == "exit") break;\n\n'

    cpp_code += '        Input input = get_input(input_str);\n\n'

    cpp_code += '        if(input == INVALID_INPUT) {\n'
    cpp_code += '            cout << "Invalid input!" << endl;\n'
    cpp_code += '            continue;\n'
    cpp_code += '        }\n\n'

    cpp_code += f'        if(current_state < 0 || current_state >= {len(states)}) {{\n'
    cpp_code += '            cout << "Current state is invalid!" << endl;\n'
    cpp_code += '            break;\n'
    cpp_code += '        }\n\n'

    cpp_code += '        State next_state = transition_table[current_state][input];\n\n'

    cpp_code += '        if(next_state == INVALID_STATE) {\n'
    cpp_code += '            cout << "Transition not defined for this input in the current state!" << endl;\n'
    cpp_code += '        } else {\n'
    cpp_code += '            current_state = next_state;\n'
    cpp_code += '        }\n'
    cpp_code += "    }\n\n"

    cpp_code += '    cout << "FSM terminated." << endl;\n'
    cpp_code += "    return 0;\n"
    cpp_code += "}\n"

    return cpp_code

# Convert FSM to C++ code
cpp_code = generate_cpp_code(fsm, start_state)

# Output the generated C++ code
print(cpp_code)

# Optionally save to a file
with open("fsm_program.cpp", "w") as f:
    f.write(cpp_code)
