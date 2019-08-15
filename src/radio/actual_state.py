class State:

    def __init__(self, actual_ui, radio_stations, selected_radio_station, play_radio_station):

        # main
        self.actual_ui = actual_ui

        # menu_ui
        self.radio_stations = radio_stations
        self.selected_radio_station = selected_radio_station
        self.play_radio_station = play_radio_station

    def set_selected_radio_station(self, value):
        if self.selected_radio_station is 0 and value is -1:
            self.selected_radio_station = len(self.radio_stations) - 1
        elif self.selected_radio_station is len(self.radio_stations) - 1 and value is 1:
            self.selected_radio_station = 0
        else:
            self.selected_radio_station += value

