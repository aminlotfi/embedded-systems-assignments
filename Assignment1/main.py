from enum import Enum, auto

class State(Enum):
    IDLE = auto()
    COOLING = auto()
    HEATING = auto()

class Event(Enum):
    TEMP_ABOVE_35 = 'T>35'
    TEMP_BELOW_15 = 'T<15'
    TEMP_BELOW_25 = 'T<25'
    TEMP_ABOVE_40 = 'T>40'
    TEMP_BELOW_35 = 'T<35'
    TEMP_ABOVE_45 = 'T>45'
    TEMP_BELOW_40 = 'T<40'
    TEMP_ABOVE_30 = 'T>30'
    TEMP_BELOW_10 = 'T<10'
    TEMP_ABOVE_15 = 'T>15'
    TEMP_BELOW_5 = 'T<5'
    TEMP_ABOVE_10 = 'T>10'

class AirConditioningSystem:
    def __init__(self):
        self.current_state = State.IDLE
        self.temperature = 25  # Initial temperature

    def turn_on_heater(self):
        print("Heater: ON")

    def turn_off_heater(self):
        print("Heater: OFF")

    def turn_on_cooler(self):
        print("Cooler: ON")

    def turn_off_cooler(self):
        print("Cooler: OFF")

    def set_crs(self, speed):
        print(f"Cooler Rotational Speed: {speed} RPS")

    def set_hrs(self, speed):
        print(f"Heater Rotational Speed: {speed} RPS")

    def parse_event(self, event_str):
        try:
            return Event(event_str)
        except ValueError:
            print(f"Unknown event: {event_str}")
            return None

    def wait_for_event(self):
        event_str = input("Enter event (e.g., 'T<25', 'T>35'): ").strip().upper()
        return self.parse_event(event_str)

    def handle_idle_state(self, event):
        self.turn_off_heater()
        self.turn_off_cooler()
        if event == Event.TEMP_ABOVE_35:
            return State.COOLING
        elif event == Event.TEMP_BELOW_15:
            return State.HEATING
        return State.IDLE

    def handle_cooling_state(self, event):
        self.turn_off_heater()
        self.turn_on_cooler()

        if event == Event.TEMP_BELOW_25:
            return State.IDLE
        elif event == Event.TEMP_BELOW_35:
            self.set_crs(4)
        elif event == Event.TEMP_ABOVE_40:
            self.set_crs(6)
        elif event == Event.TEMP_ABOVE_45:
            self.set_crs(8)
        return State.COOLING

    def handle_heating_state(self, event):
        self.turn_on_heater()
        self.turn_off_cooler()

        if event == Event.TEMP_ABOVE_30:
            return State.IDLE
        elif event == Event.TEMP_ABOVE_15:
            self.set_hrs(4)
        elif event == Event.TEMP_BELOW_10:
            self.set_hrs(6)
        elif event == Event.TEMP_BELOW_5:
            self.set_hrs(8)
        return State.HEATING

    def state_machine(self):
        state_handlers = {
            State.IDLE: self.handle_idle_state,
            State.COOLING: self.handle_cooling_state,
            State.HEATING: self.handle_heating_state,
        }

        while True:
            print(f"\nCurrent State: {self.current_state.name}")
            event = self.wait_for_event()

            if event is None:
                continue

            handler = state_handlers.get(self.current_state, None)
            if handler:
                next_state = handler(event)
                if next_state != self.current_state:
                    print(f"Transitioning from {self.current_state.name} to {next_state.name}")
                self.current_state = next_state
            else:
                print(f"No handler for state: {self.current_state}")

if __name__ == "__main__":
    ac_system = AirConditioningSystem()
    ac_system.state_machine()
