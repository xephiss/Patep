# import the libraries pygame and pygame_gui
import pygame
import pygame_gui

# import specific classes from specific files
from main_menu_state import MainMenuState
from settings_state import SettingsState
from game_state import GameState
from tutorial_state import TutorialState


class GameApp:

    def __init__(self):
        pygame.init()  # initialise pygame

        # initialise the window
        self.window_surface = pygame.display.set_mode((800, 600))
        self.ui_manager = pygame_gui.UIManager((800, 600))
        self.clock = pygame.time.Clock()
        self.running = True

        # create a dict object to hold settings
        self.settings = {
            'selected_sprite': 'green_dino'
        }

        # initialise the game states
        self.states = {'main_menu': MainMenuState(self.window_surface, self.ui_manager),
                       'settings': SettingsState(self.window_surface, self.ui_manager, self.settings),
                       'tutorial': TutorialState(self.window_surface, self.ui_manager),
                       'game': GameState(self.window_surface, self.clock, self.settings)}

        self.active_state = self.states['main_menu']  # start the app in the main menu

        # calls start on the active state which is initially main menu
        self.active_state.start()

    def run(self):
        while self.running:  # the main program loop

            time_delta = self.clock.tick(90) / 1000.0   # the time that has passed since the last time around the loop

            # retrive events that have fired since the last time around the loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                self.ui_manager.process_events(event)   # handle any ui events

                self.active_state.handle_events(event)  # pass events to the active state

            self.ui_manager.update(time_delta)  # update the ui manager with time delta as a parameter

            self.active_state.update(time_delta)    # update the active state with time delta as a parameter

            # transition between states if required
            if self.active_state.transition_target is not None:
                if self.active_state.transition_target in self.states:
                    self.active_state.stop()
                    self.active_state = self.states[self.active_state.transition_target]
                    self.active_state.start()
                elif self.active_state.transition_target == 'quit':
                    self.running = False

            pygame.display.update() # update the display

# run the game app
if __name__ == '__main__':
    app = GameApp()
    app.run()
