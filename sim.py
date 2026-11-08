"""Simulate many fights to compare strategy win rates. Run with: python sim.py"""

import contextlib
import io
import random

from combat import enemy_turn, report_attack
from config import HERO_DAMAGE, HERO_HEALTH, HERO_NAME
from entities import Character, create_boss


def always_attack(hero, enemy):
    return "1"


def block_windups(hero, enemy):
    if enemy.winding_up:
        return "2"
    return "1"


def sim_fight(hero, enemy, strategy):
    """Run one fight with a strategy choosing each action; return True if the hero survived."""
    while True:
        action = strategy(hero, enemy)
        if action == "1":
            damage, blocked, crit = hero.attack(enemy)
            report_attack(hero, enemy, damage, blocked, crit)
            if enemy.health <= 0:
                break
            enemy_turn(enemy, hero)
            if hero.health <= 0:
                break
        elif action == "2":
            hero.defending = True
            enemy_turn(enemy, hero)
            if hero.health <= 0:
                break
    return hero.health > 0


def run_strategy(strategy, fights=1000):
    """Run seeded fights against the final boss; return (win rate, average health left on wins)."""
    wins = 0
    health_left = 0
    for i in range(fights):
        random.seed(i)
        hero = Character(HERO_NAME, HERO_HEALTH, HERO_DAMAGE)
        enemy = create_boss(3)
        with contextlib.redirect_stdout(io.StringIO()):
            if sim_fight(hero, enemy, strategy):
                wins += 1
                health_left += hero.health
    return wins / fights, health_left / max(wins, 1)


if __name__ == "__main__":
    for strategy in [always_attack, block_windups]:
        win_rate, avg_health = run_strategy(strategy)
        print(
            f"Strategy: {strategy.__name__}, Win Rate: {win_rate:.1%}, Avg Health Left: {avg_health:.0f}"
        )
