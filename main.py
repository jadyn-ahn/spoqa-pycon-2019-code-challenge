from turtle import *
import random
import time


class ScreenManager:
    
    def __init__(self, screen_size, bar_size):
        self._screen = Screen()
        self._screen.setup(*screen_size)
        self._screen.bgcolor('black')
        self._pen = Turtle()
        self._pen.penup()
        self._pen.ht()
        self._make_bar(*bar_size)
        self._bar = self._make_bar(*bar_size)
        self._ball = self._make_ball()
        
    def _make_bar(self, w, h):
        self._screen.register_shape(
            'bar',
            ((-w / 2, -h /2),
            (-w / 2, h / 2),
            (w / 2, h / 2),
            (w / 2, -h / 2))
        )
        bar = Turtle()
        bar.ht()
        bar.penup()
        bar.shape('bar')
        bar.color('red')
        bar.setheading(90)
        return bar
    
    def _make_ball(self):
        ball = Turtle()
        ball.penup()
        ball.shape('circle')
        ball.color('blue')
        return ball
    
    def write_text(self, text, position, size, color='white'):
        self._pen.penup()
        self._pen.goto(*position)
        self._pen.color(color)
        self._pen.write(text, font=('', size, 'normal'))

    def erase_text(self):
        self._pen.clear()

    def erase_all(self):
        self._pen.clear()
        self._ball.clear()
        self._bar.clear()
        
    def set_key_funcs(self, funcs):
        self._screen.onkey(funcs[0], 'Left')
        self._screen.onkey(funcs[1], 'Right')
        self._screen.onkey(funcs[2], 's')
        self._screen.listen()
        
    def set_timer(self, func, t=1):
        self._screen.ontimer(func, t)
        
    def move_bar(self, center):
        self._bar.st()
        self._bar.goto(*center)
    
    def move_ball(self, center):
        self._ball.st()
        self._ball.goto(*center)

    def anagram(self):
        def make_turtles(count):
            turtles = [Turtle() for i in range(count)]
            for turtle in turtles:
                turtle.ht()
                turtle.pu()
                turtle.color('white')
            return turtles

        def go_and_write(t, x, y, w, sleep=False):
            t.clear()
            t.goto(x, y)
            t.write(w, font=('', 20))
            if sleep:
                time.sleep(0.1)
        (c1, a, t1, c2, h1, t2, h2, o1, s1, t3, o2, n1, i, e1, s2, t4, p, e2, n2, n3, y) = make_turtles(21)
        go_and_write(c1, -140, 70, 'c')
        go_and_write(a, -125, 70, 'a')
        go_and_write(t1, -110, 70, 't')
        go_and_write(c2, -95, 70, 'c')
        go_and_write(h1, -80, 70, 'h')
        go_and_write(t2, -50, 70, 't')
        go_and_write(h2, -35, 70, 'h')
        go_and_write(o1, -20, 70, 'o')
        go_and_write(s1, -140, 50, 's')
        go_and_write(t3, -125, 50, 't')
        go_and_write(o2, -110, 50, 'o')
        go_and_write(n1, -95, 50, 'n')
        go_and_write(i, -80, 50, 'i')
        go_and_write(e1, -65, 50, 'e')
        go_and_write(s2, -50, 50, 's')
        go_and_write(t4, -35, 50, 't')
        go_and_write(p, -5, 50, 'p')
        go_and_write(e2, 10, 50, 'e')
        go_and_write(n2, 25, 50, 'n')
        go_and_write(n3, 40, 50, 'n')
        go_and_write(y, 55, 50, 'y')
        time.sleep(0.5)
        go_and_write(c1, -140, 30, 'c', True)
        go_and_write(o1, -125, 30, 'o', True)
        go_and_write(n1, -110, 30, 'n', True)
        go_and_write(n2, -95, 30, 'n', True)
        go_and_write(e1, -80, 30, 'e', True)
        go_and_write(c2, -65, 30, 'c', True)
        go_and_write(t1, -50, 30, 't', True)
        go_and_write(t2, -140, 10, 't', True)
        go_and_write(h1, -125, 10, 'h', True)
        go_and_write(e2, -110, 10, 'e', True)
        go_and_write(p, -140, -10, 'p', True)
        go_and_write(y, -125, -10, 'y', True)
        go_and_write(t3, -110, -10, 't', True)
        go_and_write(h2, -95, -10, 'h', True)
        go_and_write(o2, -80, -10, 'o', True)
        go_and_write(n3, -65, -10, 'n', True)
        go_and_write(i, -50, -10, 'i', True)
        go_and_write(s1, -35, -10, 's', True)
        go_and_write(t4, -20, -10, 't', True)
        go_and_write(a, -5, -10, 'a', True)
        go_and_write(s2, 10, -10, 's', True)
        go_and_write(self._pen, 25, -10, '!!!', True)

    def end(self):
        self._screen.bye()
        

class Game:

    INIT_BALL = (0, 250)
    INIT_BAR = (0, -250)
    
    def __init__(self):
        self._ball_size = 20
        self._ball_center = self.INIT_BALL
        self._ball_diff = (-5, -5)
        self._bar_size = (30, 10)
        self._bar_center = self.INIT_BAR
        self._bar_speed = 6
        self._screen_size = (600, 600)
        self._sm = ScreenManager((600, 600), (30, 10))
        # score data
        self._count = 0
        self._success = 0
          
    def start(self):
        self._sm.write_text(
            'Catch Tho\nStoniest Penny!!',
            (-140, 50),
            30
        )
        self._sm.write_text(
            'S를 눌러주세요!!',
            (-100, 0),
            20
        )
        print('set')
        self._sm.set_key_funcs((None, None, self._explain))
    
    def _explain(self):
        self._sm.erase_text()
        self._sm.move_ball(self._ball_center)
        instructions = [
            '방향키를 연타하면 바구니가 움직여요',
            '동전이 향할 것 같은 위치로 바구니를 옮기고...',
            's를 누르면 동전이 랜덤하게 떨어집니다...',
            '최선을 다해서 동전을 받으세요!',
            '기회는 3번! 이제 시작할까요?',
            's를 누르세요!'
        ]
        for i, inst in enumerate(instructions):
            self._sm.write_text(inst, (-200, 0 - i * 20), 15)
        self._sm.set_key_funcs((None, None, self._ready))
    
    def _ready(self):
        self._sm.erase_text()
        self._ball_diff = (self._ball_diff[0] + random.random(), self._ball_diff[1] + random.random())
        self._ball_center = self.INIT_BALL
        self._sm.move_ball(self._ball_center)
        self._sm.move_bar(self._bar_center)
        self._sm.write_text('준비가 되면 s를 누르세요!', (-40, 0), 10)
        self._sm.set_key_funcs(
            (lambda : self._move_bar(True), lambda : self._move_bar(False), self._go)
        )
    
    def _go(self):
        self._sm.erase_text()
        self._sm.set_key_funcs(
            (lambda : self._move_bar(True), lambda : self._move_bar(False), None)
        )
        self._sm.set_timer(self._on_game)

    def _on_game(self):
        self._move_ball()
        bar_x, bar_y = self._bar_center
        bar_w, bar_h = self._bar_size
        ball_x, ball_y = self._ball_center
        if (bar_x - bar_w // 2 <= ball_x <= bar_x + bar_w // 2):
            if (bar_y - bar_h // 2 <= ball_y <= bar_y + bar_h // 2 + self._ball_size):
                self._success += 1
                self._count += 1
                if self._count == 3:
                    self._sm.set_timer(self._game_finished)
                else:
                    self._sm.set_timer(self._ready)
                return
        if (ball_y <= - self._screen_size[1] // 2):
            self._count += 1
            if self._count == 3:
                self._sm.set_timer(self._game_finished)
            else:
                self._sm.set_timer(self._ready)
            return
        self._sm.set_timer(self._on_game)

    def _game_finished(self):
        self._sm.erase_all()
        self._sm.write_text('DONE!', (-140, 50), 30)
        def d():
            self._sm.erase_all()
            self._sm.write_text('DONE?', (-140, 50), 30)
        self._sm.set_timer(d, 1000)
        def a():
            self._sm.erase_all()
            self._sm.anagram()
        self._sm.set_timer(a, 3000)

    def _move_bar(self, left=False):
        d = -1 if left else 1
        x, y = self._bar_center
        self._bar_center = (x + d * self._bar_speed, y)
        self._sm.move_bar(self._bar_center)

    def _move_ball(self):
        x, y = self._ball_center
        if (x <= - self._screen_size[0] // 2 or x >= self._screen_size[0] // 2):
            self._ball_diff = (-self._ball_diff[0], self._ball_diff[1])
        dx, dy = self._ball_diff
        self._ball_center = (x + dx, y + dy)
        self._sm.move_ball(self._ball_center)
    
    def end(self):
        self._sm.end()

if __name__ == '__main__':
    g = Game()
    g.start()
    g._sm._screen.mainloop()
