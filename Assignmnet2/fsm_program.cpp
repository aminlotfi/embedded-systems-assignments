#include <iostream>
#include <string>
using namespace std;

enum State {
    STATE1,
    STATE2,
    STATE3,
    INVALID_STATE
};

enum Input {
    INPUT1,
    INPUT2,
    INVALID_INPUT
};

State transition_table[3][2] = {
    {STATE2, STATE3},
    {STATE1, STATE3},
    {STATE1, STATE2},
};

Input get_input(const string& input_str) {
    if(false) {}
    else if(input_str == "input1") return INPUT1;
    else if(input_str == "input2") return INPUT2;
    else return INVALID_INPUT;
}

string input_to_string(Input input) {
    switch(input) {
        case INPUT1: return "input1";
        case INPUT2: return "input2";
        default: return "INVALID_INPUT";
    }
}

string state_to_string(State state) {
    switch(state) {
        case STATE1: return "state1";
        case STATE2: return "state2";
        case STATE3: return "state3";
        default: return "INVALID_STATE";
    }
}

int main() {
    State current_state = STATE1;
    string input_str;

    while (true) {
        switch(current_state) {
            case STATE1:
                cout << "Current state: state1" << endl;
                break;
            case STATE2:
                cout << "Current state: state2" << endl;
                break;
            case STATE3:
                cout << "Current state: state3" << endl;
                break;
            default:
                cout << "Unknown state!" << endl;
                return 1;
        }

        cout << "Enter input (or type 'exit' to quit): "; 
        cin >> input_str;

        if(input_str == "exit") break;

        Input input = get_input(input_str);

        if(input == INVALID_INPUT) {
            cout << "Invalid input!" << endl;
            continue;
        }

        if(current_state < 0 || current_state >= 3) {
            cout << "Current state is invalid!" << endl;
            break;
        }

        State next_state = transition_table[current_state][input];

        if(next_state == INVALID_STATE) {
            cout << "Transition not defined for this input in the current state!" << endl;
        } else {
            current_state = next_state;
        }
    }

    cout << "FSM terminated." << endl;
    return 0;
}
