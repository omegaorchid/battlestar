import controller
import event_manager
import models.model
import views.view
import pygame

pygame.init()


def run():
    evm = event_manager.EventManager()
    game_model = model.GameEngine(evm)
    keyboard = controller.Keyboard(evm, game_model)
    graphics = view.GraphicalView(evm, game_model)

    game_model.main_loop()

if __name__ == '__main__':
    run()

pygame.quit()
quit()