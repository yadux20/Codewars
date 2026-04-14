def combat(health, damage):
    if health > damage:
        return health - damage
    return 0