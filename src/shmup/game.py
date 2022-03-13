from importlib import resources
import pygame, sys
from settings import *

class Game:

  __images_path__ = "shmup.assets.images"
  __hero_path__ = "superman.png"
  __screen_size = (640,480)
  __hero_speed = 0.1

  def __init__(self):
    pygame.init()

    self.clock =pygame.time.Clock()
    self.__screen = pygame.display.set_mode(Game.__screen_size, 0, 32)
    pygame.display.set_caption("Gods and wars")

    with resources.path(Game.__images_path__, Game.__hero_path__) as hero_file:
      self.__hero_image = pygame.image.load(hero_file).convert_alpha()

    self.__hero_moving_right = False
    self.__hero_moving_left = False
    self.__hero_moving_up = False
    self.__hero_moving_down = False

    self.__hero_position = pygame.math.Vector2(Game.__screen_size[0]/2, Game.__screen_size[1]/2)

    self.__running = True

  def run(self):
    while self.__running:
      self.clock.tick(FPS)
      self.__process_events()
      self.__update()
      self.__render()

    self.__quit()

  def __process_events(self):
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        self.__running = False
      if event.type == pygame.KEYDOWN:
        self.__handle_player_input(event.key, True)
      elif event.type == pygame.KEYUP:
        self.__handle_player_input(event.key, False)

#se actualiza el estado del juego
  def __update(self):
    movement = pygame.math.Vector2(0.0, 0.0)
    if self.__hero_moving_up:
      movement.y -= Game.__hero_speed
    if self.__hero_moving_down:
      movement.y += Game.__hero_speed
    if self.__hero_moving_left:
      movement.x -= Game.__hero_speed
    if self.__hero_moving_right:
      movement.x += Game.__hero_speed

    self.__hero_position += movement

#se pinta el estado del juego
  def __render(self):
    self.__screen.fill((0,0,0))
    self.__screen.blit(self.__hero_image, self.__hero_position)

    pygame.display.update()

  def __quit(self):
    pygame.quit()

  def __handle_player_input(self, key, is_pressed):
    if key == pygame.K_UP:
      self.__hero_moving_up = is_pressed
    elif key == pygame.K_DOWN:
      self.__hero_moving_down = is_pressed
    elif key == pygame.K_LEFT:
      self.__hero_moving_left = is_pressed
    elif key == pygame.K_RIGHT:
      self.__hero_moving_right = is_pressed