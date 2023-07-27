from typing import Optional,Tuple,Dict
Action = str

class State:
    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return self.name

def login_checker(action_param: str, atm_password: str, atm_current_balance: int) -> Tuple[bool, int, Optional[int]]:
    if action_param == atm_password:
        return True, atm_current_balance, None
    else:
        return False, atm_current_balance, None

def logout_checker(action_param: Optional[str], atm_password: str, atm_current_balance: int) -> Tuple[bool, int, Optional[int]]:
    return True, atm_current_balance, None

def deposit_checker(action_param: str, atm_password: str, atm_current_balance: int) -> Tuple[bool, int, Optional[int]]:
    if action_param is not None:
        amount = int(action_param)
        return True, atm_current_balance + amount, None
    return False, atm_current_balance, None

def withdraw_checker(action_param: str, atm_password: str, atm_current_balance: int) -> Tuple[bool, int, Optional[int]]:
    if action_param is not None:
        amount = int(action_param)
        if atm_current_balance >= amount:
            return True, atm_current_balance - amount, None
    return False, atm_current_balance, None

def balance_checker(action_param: Optional[str], atm_password: str, atm_current_balance: int) -> Tuple[bool, int, Optional[int]]:
    return True, atm_current_balance, atm_current_balance

# Implement the transition_table here
transition_table = {
    State("unauthorized"): [
        ("login", login_checker, State("authorized"))
    ],
    State("authorized"): [
        ("logout", logout_checker, State("unauthorized")),
        ("deposit", deposit_checker, State("authorized")),
        ("withdraw", withdraw_checker, State("authorized")),
        ("balance", balance_checker, State("authorized"))
    ]
}

# Look for the implementation of the ATM class in the below Tail section
class ATM:
    def __init__(self, init_state: State, init_balance: int, password: str, transition_table: Dict):
        self.state = init_state
        self._balance = init_balance
        self._password = password
        self._transition_table = transition_table

    def next(self, action: Action, param: Optional[str]) -> Tuple[bool, Optional[int]]:
        try:
            for transition_action, check, next_state in self._transition_table[self.state]:
                if action == transition_action:
                    passed, new_balance, res = check(param, self._password, self._balance)
                    if passed:
                        self._balance = new_balance
                        self.state = next_state
                        return True, res
        except KeyError:
            pass
        return False, None

if __name__ == "__main__":
    # Sample usage:
    input_password = 'hacker' # input()
    init_balance = 10 # int(input())

    # Set the initial state to "unauthorized"
    atm = ATM(State("unauthorized"), init_balance, input_password, transition_table)

    inp = ["login hacker","depoist 10"]  #int(input())
    q=len(inp)
    for i in inp:
        # action_input = input().strip().split()
        action_input=i.split(' ')
        action_name = action_input[0]
        action_param = action_input[1] if len(action_input) > 1 else None

        if action_name in ["deposit", "withdraw"]:
            action_param = int(action_param)

        success, res = atm.next(action_name, action_param)
        if res is not None:
            print(f"Success={success} {atm.state} {res}")
        else:
            print(f"Success={success} {atm.state}")
