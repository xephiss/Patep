import pygame
import pygame_gui

from main_menu_state import MainMenuState
from settings_state import SettingsState
from game_state import GameState


class GameApp:

    def __init__(self):
        pygame.init()

        self.window_surface = pygame.display.set_mode((800, 600))
        self.ui_manager = pygame_gui.UIManager((800, 600))
        self.clock = pygame.time.Clock()
        self.running = True

        self.states = {'main_menu': MainMenuState(self.window_surface, self.ui_manager),
                       'settings': SettingsState(self.window_surface, self.ui_manager),
                       'game': GameState(self.window_surface, self.clock)}

        self.active_state = self.states['main_menu']  # start the app in the main menu
        self.active_state.start()

    def run(self):
        while self.running:
            time_delta = self.clock.tick(60)/1000.0

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                self.ui_manager.process_events(event)

                self.active_state.handle_events(event)

            self.ui_manager.update(time_delta)

            self.active_state.update(time_delta)

            if self.active_state.transition_target is not None:
                if self.active_state.transition_target in self.states:
                    self.active_state.stop()
                    self.active_state = self.states[self.active_state.transition_target]
                    self.active_state.start()
                elif self.active_state.transition_target == 'quit':
                    self.running = False

            pygame.display.update()


if __name__ == '__main__':
    app = GameApp()
    app.run()
